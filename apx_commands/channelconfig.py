import re
import utility

async def channel_configLogic(client, firestore, db, channelId, guildId, operation, channel):
    channelList = utility.retrieveDb_data(db, option='channellist', title=guildId)
    await utility.checkChannel(db, firestore, channelList, channelId, guildId)
    availableChannels = '\n'.join('<#{}>'.format(key) for key, value in utility.retrieveDb_data(db, option='channellist', title=guildId).items())

    usageMessage = f'**Usage:**\n\n`!channelconfig authorize [#channel]`\n`!channelconfig revoke [#channel]`\n\n**Authorized Channels:**\n\n{availableChannels}'
    if operation:
        if channel:
            channellist_Db = db.collection('channellist').document(str(guildId))
            try:
                channelSelect = int(re.search(r'\d+', channel).group())
            except:
                return await client.say('Please input the correct channel format, e.g. `#example`.')
            if operation == 'authorize':
                data = {str(channelSelect):str(channelSelect)}
                channellist_Db.update(data)
                return await client.say(f'**Updated authorized channel list.**\n <#{channelSelect}> `is now authorized`')
                
            if operation == 'revoke':
                data = {str(channelSelect): firestore.DELETE_FIELD}
                channellist_Db.update(data)
                return await client.say(f'**Updated authorized channel list.**\n `Revoked access from` <#{channelSelect}>')
    
    return await client.say(usageMessage)
# [APX] Bot
A simple Discord bot to check for ArmA 3 server status.

# About
This project is made to improve players convenience and reduce time spent when checking current mission and number of players of ArmA 3 servers in Battlemetrics through Discord integration.

# Features
The bot is able to show current mission, number of players and active players list on a server when !serverstats command is invoked by a user. Users can browse through the list of servers on Battlemetrics by server name to retrieve the server ID. Channel authorization can be managed by authorized users through !channelconfig command. Respectively, server list can also be managed by authorized users through !serverconfig command. The bot is also containerized using Docker to provide more portability in deployment. It is using Sentry for logging and error tracking, Segment with Amplitude integration for analytics and Google Cloud Firestore to store channel, server list and configuration variables. There are two available runtime modes, each accomodates for production and development purpose.

# Usage
### !apxhelp
Display help message.

![Alt Text](https://github.com/farhannysf/apx_bot/blob/apx/docs/apxhelp.gif)

### !channelconfig
Authorize or revoke bot access to channels.

###### `!channelconfig authorize #example-channel`
Authorize bot access to #example-channel.

###### `!channelconfig revoke #example-channel`
Revoke bot access to #example-channel.

![Alt Text](https://github.com/farhannysf/apx_bot/blob/apx/docs/channelconfig.gif)

### !serverconfig
Assign or remove ArmA 3 servers on Battlemetrics to the bot.

Assigned name must not include any space or special character.

###### `!serverconfig update [name] [battlemetrics id]`
Assign a name to the respective server using Battlemetrics ID and save it to the bot.

###### `!serverconfig delete [name]`
Remove saved server from the bot by the assigned name.

![Alt Text](https://github.com/farhannysf/apx_bot/blob/apx/docs/serverconfig.gif)

### !serverstats
Check status of saved server.

###### `!serverstats [name]`
Check status of a server by the assigned name.

![Alt Text](https://github.com/farhannysf/apx_bot/blob/apx/docs/serverstats.gif)

### !serversearch
Search for ArmA 3 servers Battlemetrics ID.

###### `!serversearch "server name"`
Search for Battlemetrics ID by server name.

![Alt Text](https://github.com/farhannysf/apx_bot/blob/apx/docs/serversearch.gif)

# Sites/Tools used

### Tools
* [aiohttp](https://docs.aiohttp.org/en/stable/)
* [asyncio](https://docs.python.org/3.6/library/asyncio.html)
* [discord.py](https://discordpy.readthedocs.io/en/latest/)
* [sanic](https://sanic.readthedocs.io/en/latest/)
* [python-dotenv](https://github.com/theskumar/python-dotenv)
* [sentry-sdk](https://docs.sentry.io/error-reporting/quickstart/?platform=python)
* [analytics-python](https://segment.com/docs/sources/server/python/)
* [google-cloud-firestore](https://cloud.google.com/firestore/docs/quickstart-servers)

### API
* [Battlemetrics](https://www.battlemetrics.com/developers/documentation)

### Sites
* [Segment](https://segment.com/)
* [Amplitude](https://amplitude.com/)
* [Google Cloud Platform](https://cloud.google.com/)

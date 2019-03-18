FROM python:3.6

WORKDIR /app

RUN set -eux \
  && apt-get update 

RUN pip install requests

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

ENV PORT 8080

CMD ["python", "main.py", "prod"]
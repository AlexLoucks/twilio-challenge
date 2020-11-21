FROM python:3.6.1-alpine

LABEL maintainer = "Alex Loucks"


WORKDIR /twilio-challenge
ADD . /twilio-challenge

RUN pip install -r requirements.txt

CMD ["python","run.py"]
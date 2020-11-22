###############################################
# Base image
###############################################
FROM python:3.8-alpine AS runnable

LABEL maintainer = "Alex Loucks"

WORKDIR /twilio-challenge
ADD . /twilio-challenge

RUN pip install -r requirements.txt

CMD ["python","run.py"]

###############################################
# Unit testing Image
###############################################
FROM runnable AS tests
RUN pip install -r testing-requirements.txt
ENTRYPOINT ["pytest", "-s", "-vv", "--cov", "--cov-report=term-missing", "--cov-report=xml:/tmp/coverage.xml", "--junitxml=/tmp/pytest-report"]
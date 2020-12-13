FROM python:3.8-alpine

COPY . /mobile_automated_tests

WORKDIR /mobile_automated_tests
RUN apk add --no-cache bash
RUN pip3 install pipenv

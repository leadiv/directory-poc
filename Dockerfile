FROM python:slim-bookworm

ENV APP=pictorial_directory
ENV PYTHONPATH="${PYTHONPATH}:${APP}"

RUN apt-get update && apt-get install make
RUN mkdir $APP

COPY scripts/requirements.txt $APP/requirements.txt
RUN pip install -r $APP/requirements.txt

COPY ./Makefile $APP/Makefile
COPY scripts $APP/scripts

WORKDIR $APP

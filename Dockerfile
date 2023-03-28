FROM python:3

MAINTAINER xiaohan


COPY . /chagpt_reply
WORKDIR /chagpt_reply

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV appkey=你的API_KEY
ENV token=token
CMD python /chagpt_reply/server.py

EXPOSE 8080

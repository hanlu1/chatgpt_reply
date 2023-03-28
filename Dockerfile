FROM python:3

MAINTAINER xiaohan


COPY . /chagpt_reply
WORKDIR /chagpt_reply

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV appkey="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"
ENV token="123"
CMD python /chagpt_reply/server.py

EXPOSE 8080
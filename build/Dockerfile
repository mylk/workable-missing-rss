FROM python:3-alpine

ADD . /workable-missing-rss
WORKDIR /workable-missing-rss

RUN apk add make && \
    make deps

CMD ["./build/start.sh"]

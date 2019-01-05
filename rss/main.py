#!/usr/bin/python3
from bottle import route, response, run
from feed import Feed
from page import Page
import settings


@route('/')
def index():
    response.content_type = 'text/xml; charset=utf-8'

    page = Page(settings.URL)
    source = page.crawl()
    jobs = page.parse(source)

    feed = Feed(jobs)

    return feed.generate()


run(host='0.0.0.0', port=8002)

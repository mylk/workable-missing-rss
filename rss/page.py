from bs4 import BeautifulSoup
from job import Job
import settings
import urllib


class Page():

    def __init__(self, url):
        self.url = url

    def crawl(self):
        request = urllib.request.Request(self.url)
        request.add_header('User-Agent', settings.AGENT)
        response = urllib.request.urlopen(request)
        return BeautifulSoup(response.read(), 'html.parser')

    def get_jobs(self, html):
        return html.select('ul > li')

    def parse(self, html):
        jobs = []

        for job in self.get_jobs(html):
            job = Job(job)

            if not job.is_valid():
                continue

            jobs.append(job)

        return jobs

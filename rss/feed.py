from datetime import datetime
import rfeed


class Feed():

    jobs = None

    def __init__(self, jobs):
        self.jobs = jobs

    def generate(self):
        author = 'Workable'
        items = []

        for job in self.jobs:
            title = job.get_position() + ', ' + job.get_company()

            item = rfeed.Item(
                title=title,
                link=job.get_link(),
                description=job.get_description(),
                author=author,
                guid=rfeed.Guid(job.get_link()),
                pubDate=job.get_date()
            )

            items.append(item)

        feed = rfeed.Feed(
            title='Workable\'s missing RSS feed',
            link='http://mylk.wtf/workable-missing-rss',
            description='Workable\'s missing RSS feed',
            language='el-GR',
            lastBuildDate=datetime.now(),
            items=items
        )

        return feed.rss()

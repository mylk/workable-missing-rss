## Workable missing RSS

I love RSS and RSS readers will always be one of my favorite tools.

I follow the feeds of a lot of websites and one of the categories of feeds I follow are "employment" websites.

One of my favorites is [Workable's Greek Start-ups feed](https://workable.com/jobs/greekstartups) which unfortunately stopped working a few months ago,

so I thought I could revive it by scraping and recreate the feed myself.

That's what I did here, just for fun, for a few hours, work on one of my favorite languages, `python3`,

containerization with `Docker` which I also love and enjoy and create my beloved resource, an RSS feed.

Damn, that's too much love for today. 

## Run

You can run the application as standalone, but I always prefer to run my projects on a nice container.

In order to run this application you need `docker` and `docker-compose`.

Use your distro's package manager to install them. You will also, of course, need to clone this project. 

The following commands assume that you are on the source code's root directory. 

To build the Docker image:

```
docker-compose build
```

To start the application's Docker container:

```
docker-compose up
```

Visit `localhost:8002` to view our `Workable Greek start-ups` feed.

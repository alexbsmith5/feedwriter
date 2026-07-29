# feedwriter
[![tests](https://github.com/alexbsmith5/feedwriter/actions/workflows/tests.yaml/badge.svg)](https://github.com/alexbsmith5/feedwriter/actions/workflows/tests.yaml)
[![PyPI Version](https://img.shields.io/pypi/v/feedwriter)](https://pypi.org/project/feedwriter/)
![PyPI Python Version](https://img.shields.io/pypi/pyversions/feedwriter)

A Python library to generate podcast RSS feeds.

Supports all the tags for Apple Podcasts as well as any player with a [PSP Certification](https://podstandards.org/).

## Docs

The main documentation for the project lies in the [docs/build/markdown/](docs/build/markdown/index.md) directory. From there you can find the api documentation as well as the list of post and episode tags. I would recommend starting on the [tags page](docs/build/markdown/tags.md), and going to the [api page](docs/build/markdown/podcastfeed_api.md) for information on the specific functions.

## Quickstart

Install `feedwriter` from [pypi](https://pypi.org/project/feedwriter/).

```bash
pip install feedwriter
```

Below is a code snippet with a simple example of how to use the library. The comments should serve as a short explanation of what is being run.

``` python
# import class from library
from feedwriter import PodcastFeed

# create PodcastFeed object
feed = PodcastFeed()

# add title of show
feed.title("Example")

# create post with title and guid
feed.new_post(title="Lorem ipsum", guid="1234")

# create empty post and add tags later
feed.new_post()
feed.post_title("Lorem ipsum dolor")
feed.post_duration(1800)

# write object to file
feed.write("feed.xml")
```

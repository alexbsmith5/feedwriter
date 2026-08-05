# feedwriter

[![tests](https://github.com/alexbsmith5/feedwriter/actions/workflows/tests.yaml/badge.svg)](https://github.com/alexbsmith5/feedwriter/actions/workflows/tests.yaml)
[![PyPI Version](https://img.shields.io/pypi/v/feedwriter)](https://pypi.org/project/feedwriter/)
![PyPI Python Version](https://img.shields.io/pypi/pyversions/feedwriter)

A Python library to generate podcast RSS feeds.

Supports all the tags for Apple Podcasts as well as any player with a [PSP Certification](https://podstandards.org/).

## Docs

Documentation is found [here](docs/build/markdown/index.md).

I would recommend starting with the [quickstart](##Quickstart), and from there going to the [tags page](docs/build/markdown/tags.md) to find the functions for a specific tag.

For more information on the `PodcastFeed` and `Feed` classes, you can find their respective API documentation below:

- [`PodcastFeed`](docs/build/markdown/podcastfeed_api.md)
- [`Feed`](docs/build/markdown/feed_api.md)

## Quickstart

Install `feedwriter` from [pypi](https://pypi.org/project/feedwriter/).

```bash
pip install feedwriter
```

Below is a code snippet with a simple example of how to use the library. The comments should serve as a short explanation of what is being run.

```python
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

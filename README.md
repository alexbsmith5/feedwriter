# feedwriter
[![tests](https://github.com/alexbsmith5/feedwriter/actions/workflows/tests.yaml/badge.svg)](https://github.com/alexbsmith5/feedwriter/actions/workflows/tests.yaml)

A Python library to generate podcast rss feeds.

Currently, passing Apple Podcasts' feed validation is the main focus, but in the future other platforms will be supported.

## Quickstart

Install `feedwriter` from [pypi](https://pypi.org/project/feedwriter/).

```bash
pip install feedwriter
```

Below is a code snipped with a simple example of how to use the library. The comments should serve as a short explanation of what is being run.

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

## Docs

The main documentation for the project lies in the [docs/build/markdown/](docs/build/markdown/index.md) directory. From there you can find the api documentation as well as the list of post and episode tags. I would recommend starting on the [tags page](docs/build/markdown/tags.md), and going to the [api page](docs/build/markdown/api.md) for information on the specific functions.

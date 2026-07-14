# Guide

## Required Tags

The following tags are required for the channel and for every post. If these tags are missing, the show will fail Apple Podcast’s feed validation blocking it from being listed.

### Channel Tags

The following commands specified below must be called in order to pass validation.

> * [`title`](api.md#feedwriter.podcast_feed.PodcastFeed.title)
> * [`description`](api.md#feedwriter.podcast_feed.PodcastFeed.description)
> * [`image`](api.md#feedwriter.podcast_feed.PodcastFeed.image)
> * [`category`](api.md#feedwriter.podcast_feed.PodcastFeed.category)
> * [`explicit`](api.md#feedwriter.podcast_feed.PodcastFeed.explicit)

### Episode Tags

The following commands must be called for every single episode on the feed to pass validation.

These commands can be run by themselves, defaulting to the last created post or passing the index. Another option is to run the [`new_post`](api.md#feedwriter.podcast_feed.PodcastFeed.new_post) function and pass in the corresponsing kwargs.

> * [`post_title`](api.md#feedwriter.podcast_feed.PodcastFeed.post_title)
> * [`post_enclosure`](api.md#feedwriter.podcast_feed.PodcastFeed.post_enclosure)
> * [`post_guid`](api.md#feedwriter.podcast_feed.PodcastFeed.post_guid)

## Recommended Tags

While these tags are not required to pass Apple Podcast’s feed validation, they can provide helpful information to users.

### Channel Tags

> * [`author`](api.md#feedwriter.podcast_feed.PodcastFeed.author)
> * [`link`](api.md#feedwriter.podcast_feed.PodcastFeed.link)

### Episode Tags

> * [`post_date`](api.md#feedwriter.podcast_feed.PodcastFeed.post_date)
> * [`post_description`](api.md#feedwriter.podcast_feed.PodcastFeed.post_description)
> * [`post_duration`](api.md#feedwriter.podcast_feed.PodcastFeed.post_duration)
> * [`post_link`](api.md#feedwriter.podcast_feed.PodcastFeed.post_link)
> * [`post_image`](api.md#feedwriter.podcast_feed.PodcastFeed.post_image)
> * [`post_explicit`](api.md#feedwriter.podcast_feed.PodcastFeed.post_explicit)

## Situational Tags

Just like recommended tags, these tags are not necessarily required but they can be useful in certain situations.

### Channel Tags

> * [`itunes_title`](api.md#feedwriter.podcast_feed.PodcastFeed.itunes_title)
> * [`type`](api.md#feedwriter.podcast_feed.PodcastFeed.type)
> * [`copyright`](api.md#feedwriter.podcast_feed.PodcastFeed.copyright)
> * [`feed_url_new`](api.md#feedwriter.podcast_feed.PodcastFeed.feed_url_new)
> * [`block`](api.md#feedwriter.podcast_feed.PodcastFeed.block)
> * [`complete`](api.md#feedwriter.podcast_feed.PodcastFeed.complete)
> * [`verify`](api.md#feedwriter.podcast_feed.PodcastFeed.verify)
> * [`generator`](api.md#feedwriter.podcast_feed.PodcastFeed.generator)

### Episode Tags

> * [`post_itunes_title`](api.md#feedwriter.podcast_feed.PodcastFeed.post_itunes_title)
> * [`post_episode`](api.md#feedwriter.podcast_feed.PodcastFeed.post_episode)
> * [`post_season`](api.md#feedwriter.podcast_feed.PodcastFeed.post_season)
> * [`post_type`](api.md#feedwriter.podcast_feed.PodcastFeed.post_type)
> * [`post_chapters`](api.md#feedwriter.podcast_feed.PodcastFeed.post_chapters)
> * [`post_transcript`](api.md#feedwriter.podcast_feed.PodcastFeed.post_transcript)
> * [`post_block`](api.md#feedwriter.podcast_feed.PodcastFeed.post_block)

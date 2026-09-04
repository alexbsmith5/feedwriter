<a id="tags"></a>

# Tags

The information about the show and episodes of a podcast is transmitted with RSS feeds which use XML. The information in an XML document is found and created in it’s tags. For podcast players, there are tags that are required, recommended and situational. For the required tags, they must be present to pass each players feed validation process. For recommended and situational tags, they are not necessarily required, but they can be important depending on the situation.

<a id="required-tags"></a>

## Required Tags

The following tags must be present in order to pass validation. If these tags are missing, the show will fail validation, and not be added to the podcast player’s catalog.

<a id="channel-tags"></a>

### Channel Tags

The following commands specified below must be called to be validated.

> * [`link_feed()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.link_feed)
> * `title()`
> * `description()`
> * [`image()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.image)
> * [`language()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.language)
> * [`category()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.category)
> * [`explicit()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.explicit)
> * [`link_page()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.link_page)

<a id="episode-tags"></a>

### Episode Tags

For every single post they must contain the following tags to be validated.

To add the tags, the following commands can be run by themselves, defaulting to the last created post or passing the index. Another option is to run the [`new_post()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.new_post) function and pass in the corresponding kwargs.

> * [`post_title()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.post_title)
> * [`post_enclosure()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.post_enclosure)
> * [`post_guid()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.post_guid)

<a id="recommended-tags"></a>

## Recommended Tags

While these tags are not required to pass feed validation, they can provide helpful information to users.

<a id="id1"></a>

### Channel Tags

> * [`guid()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.guid)
> * [`author()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.author)

<a id="id2"></a>

### Episode Tags

> * [`post_date()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.post_date)
> * [`post_description()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.post_description)
> * [`post_duration()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.post_duration)
> * [`post_link()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.post_link)
> * [`post_image()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.post_image)
> * [`post_explicit()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.post_explicit)

<a id="situational-tags"></a>

## Situational Tags

Just like recommended tags, these tags are not necessarily required but they can be useful in certain situations.

<a id="id3"></a>

### Channel Tags

> * [`itunes_title()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.itunes_title)
> * [`type()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.type)
> * [`copyright()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.copyright)
> * [`feed_url_new()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.feed_url_new)
> * [`block()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.block)
> * [`complete()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.complete)
> * [`verify()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.verify)
> * [`funding()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.funding)
> * [`generator()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.generator)

<a id="id4"></a>

### Episode Tags

> * [`post_itunes_title()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.post_itunes_title)
> * [`post_episode()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.post_episode)
> * [`post_season()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.post_season)
> * [`post_type()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.post_type)
> * [`post_chapters()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.post_chapters)
> * [`post_transcript()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.post_transcript)
> * [`post_block()`](podcastfeed_api.md#feedwriter.podcast_feed.PodcastFeed.post_block)

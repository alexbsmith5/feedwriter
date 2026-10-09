<a id="tags"></a>

# Tags

The information about the show and episodes of a podcast is transmitted with RSS feeds which use XML. The information in an XML document is found and created in it’s tags. For podcast players, there are tags that are required, recommended and situational. For the required tags, they must be present to pass each players feed validation process. For recommended and situational tags, they are not necessarily required, but they can be important depending on the situation.

<a id="required-tags"></a>

## Required Tags

The following tags must be present in order to pass validation. If these tags are missing, the show will fail validation, and not be added to the podcast player’s catalog.

<a id="channel-tags"></a>

### Channel Tags

The following commands specified below must be called to be validated.

> * `link_feed()`
> * `title()`
> * `description()`
> * `image()`
> * `language()`
> * `category()`
> * `explicit()`
> * `link()`

<a id="episode-tags"></a>

### Episode Tags

For every single post they must contain the following tags to be validated.

To add the tags, the following commands can be run by themselves, defaulting to the last created post or passing the index. Another option is to run the `new_post()` function and pass in the corresponding kwargs.

> * `post_title()`
> * `item_enclosure()`
> * `item_guid()`

<a id="recommended-tags"></a>

## Recommended Tags

While these tags are not required to pass feed validation, they can provide helpful information to users.

<a id="id1"></a>

### Channel Tags

> * `guid()`
> * `author()`

<a id="id2"></a>

### Episode Tags

> * `item_date()`
> * `item_description()`
> * `post_duration()`
> * `item_link()`
> * `post_image()`
> * `post_explicit()`

<a id="situational-tags"></a>

## Situational Tags

Just like recommended tags, these tags are not necessarily required but they can be useful in certain situations.

<a id="id3"></a>

### Channel Tags

> * `itunes_title()`
> * `type()`
> * `copyright()`
> * `feed_url_new()`
> * `block()`
> * `complete()`
> * `verify()`
> * `funding()`
> * `generator()`

<a id="id4"></a>

### Episode Tags

> * `post_itunes_title()`
> * `post_episode()`
> * `post_season()`
> * `post_type()`
> * `post_chapters()`
> * `post_transcript()`
> * `post_block()`

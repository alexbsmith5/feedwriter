# API Reference

### Constructor
```python
PodcastFeed.PodcastFeed()
```
Create the PodcastFeed object.

## Channel tags

### title
```python
title(title: str)
```
Set show title.

**Parameters:**
- `title`: string of channel name.

### description
```python
description(description: str)
```
Set show description.

**Parameters:**
- `description`: string of show description.

### image
```python
image(url: str)
```
Set show artwork.

**Paraters:**
- `image`: string of url pointing to a `.jpg` or `.png`.
<!-- TODO: general section going over image guidelines -->

### language
```python
language(language: str)
```
Set show language.

**Parameters:**
- `language`: string of a lanauge from the [ISO 639](https://www.loc.gov/standards/iso639-2/php/code_list.php) specification.

### category
```python
category(category: str, subcategory: str)
```
Set show category.

**Parameters:**
- `category`: string of category from the [Apple Podcasts categories](https://podcasters.apple.com/support/1691-apple-podcasts-categories) list.

- `subcategory`: string of subcategory from the [Apple Podcasts categories](https://podcasters.apple.com/support/1691-apple-podcasts-categories) list (OPTIONAL).

### explicit
```python
explicit(explicit: bool)
```
Set show as explicit or not.

**Parameters:**
- `explicit`: bool representing explicit status.

### author
```python
author(author: str)
```
Set show author(s).

**Parameters:**
- `author`: string of author name.

### itunes_title
```python
itunes_title(title: str)
```
Set the specific title for show on Apple Podcasts.

**Parameters:**
- `title`: string of show name.

### type
```python
type(type: str)
```
Set the show as either `episodic` or `serial`. If `serial` type is chosen, the `<itunes:episode>` tag must be specified for each post.

**Parameters:**
- `type`: string containing either `episodic` or `serial`.

### copyright
```python
copyright(copyrightd; str)
```
Set show copyright information.

**Parameters:**
- `copyright`: string of copyright information.

### feed_url_new
```python
feed_url_new(url: str)
```
Set url of new rss feed location.
Only necessary if changing url of rss feed.

**Parameters:**
- `url`: string of url pointing to rss feed.

### block
```python
block()
```
Removes show from apple directory.

### complete
```python
complete()
```
Set show as complete, no new episodes will be added.

### verify
```python
verify(token: str)
```
Set token to verify podcast with Apple Podcasts. Token will be provided by Apple.

**Parameters:**
- `token`: string of token.

### generator
```python
generator(url: str)
```
Set url of rss generator.

**Parameters:**
- `url`: string of url.

## Episode Tags

### post_enclosure
```python
post_enclosure(url: str, file_size: int, type: str, index: int = -1):
```
Set url, length, and type of media for post.

**Parameters:**
- `url`: string of url to mp3 file.
- `length`: int of file size in bytes.
- `type`: string of type (usually `audio/mpeg`).
  - Options: `audio/x-m4a`, `audio/mpeg`, `video/quicktime`, `video/mp4`, `video/x-m4v`, `application/pdf`.
- (OPTIONAL) `index`: index int of post. Defaults to post last created.

### post_guid
```python
post_guid(guid: str, index: int = -1):
```
Set guid (globally unique identifier) for post.

**Parameters:**
- `guid`: string of guid.
- (OPTIONAL) `index`: index int of post. Defaults to post last created.

### post_date
```python
post_date(date: str, index: int = -1):
```
Set date of the post's release.

**Parameters:**
- `date`: string of date following the [RFC 2822 specification](https://datatracker.ietf.org/doc/html/rfc2822#section-3.3).
- (OPTIONAL) `index`: index int of post. Defaults to post last created.

### post_description
```python
post_description(description: str, index: int = -1):
```
Set post description.

**Parameters:**
- `description`: string of post description.
- (OPTIONAL) `index`: index int of post. Defaults to post last created.

### post_duration
```python
post_duration(seconds: int, index: int = -1):
```
Set the length of audio, in seconds.

**Parameters:**
- `seconds`: int of seconds.
- (OPTIONAL) `index`: index int of post. Defaults to post last created.

### post_link
```python
post_link(, index: int = -1):
```
Set link to external webpage for post.

**Parameters:**
- `url`: string of url.
- (OPTIONAL) `index`: index int of post. Defaults to post last created.

### post_image
```python
post_image(url: str, index: int = -1):
```
Set image for post.

**Parameters:**
- `url`: string of url pointing to a `.jpg` or `.png`.
- (OPTIONAL) `index`: index int of post. Defaults to post last created.

### post_explicit
```python
post_explicit(explicit: bool, index: int = -1):
```
Set post as explicit or not.

**Parameters:**
- `explicit`: bool representing explicit status.
- (OPTIONAL) `index`: index int of post. Defaults to post last created.

### post_itunes_title
```python
post_itunes_title(title: str, index: int = -1):
```
Set the specific title for post on Apple Podcasts.

**Parameters:**
- `title`: string of post name.
- (OPTIONAL) `index`: index int of post. Defaults to post last created.

### post_episode_number
```python
post_number(num: int, index: int = -1):
```
Add post number. Only required for shows of `serial` type.

**Parameters:**
- `num`: int of episode number.
- (OPTIONAL) `index`: index int of post. Defaults to post last created.

### post_season_number
```python
post_season_number(num: int, index: int = -1):
```
Add season number. Only required for shows of `serial` type.

**Parameters:**
- `num`: int of season number.
- (OPTIONAL) `index`: index int of post. Defaults to post last created.

### post_type
```python
post_type(type: str, index: int = -1):
```
Set episode as `full`, `trailer`, or `bonus`.

**Parameters:**
- `type`: string of type.
  - Options: `full`, `trailer`, `type`.
- (OPTIONAL) `index`: index int of post. Defaults to post last created.

### post_chapters
```python
post_chapters(url: str, index: int = -1):
```
Set url of chapters file. File must follow the [podcastindex.org json chapters format](https://github.com/Podcastindex-org/podcast-namespace/blob/main/docs/examples/chapters/jsonChapters.md).

**Parameters:**
- `url`: string of url pointing to `.json` file.
- (OPTIONAL) `index`: index int of post. Defaults to post last created.

### post_transcript
```python
post_transcript(url: str, index: int = -1):
```
Set url of post file. File must follow the [podcastindex.org json chapters format](https://github.com/Podcastindex-org/podcast-namespace/blob/main/docs/examples/chapters/jsonChapters.md).

**Parameters:**
- `url`: string of url pointing to `.json` file.
- (OPTIONAL) `index`: index int of post. Defaults to post last created.

### post_block
```python
post_block(index: int = -1):
```
Add post block (hides episode in Apple Podcasts). Only call function if trying to block episode.

**Parameters:**
- (OPTIONAL) `index`: index int of post. Defaults to post last created.

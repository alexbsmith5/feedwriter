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

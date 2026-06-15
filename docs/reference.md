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
Set the show title.
**Parameters:**
- `title`: string of channel name.

### description
```python
description(description: str)
```
**Parameters:**
- `description`: string of show description.

### image
```python
image(url: str)
```
Set the show artwork.
**Paramters:**
- `image`: string of url pointing to a `.jpg` or `.png`.
<!-- TODO: general section going over image guidelines -->

### language
```python
language(language: str)
```
Set the language.
**Paramters:**
- `language`: string of a lanauge from the [ISO 639](https://www.loc.gov/standards/iso639-2/php/code_list.php) specification.

### category
```python
category(category: str)
```
Set category.
**Paramters:**
- `category`: string of category from the [Apple Podcasts categories](https://podcasters.apple.com/support/1691-apple-podcasts-categories) list.

### explicit
```python
explicit(explicit: bool)
```
Set show as explicit or not.
**Paramters:**
- `explicit`: bool representing explicit status.

### author
```python
author(author: str)
```
Set the author for the show.
**Paramters:**
- `author`: string of author name.

### itunes_title
```python
itunes_title(title: str)
```
Set the specific title for show on Apple Podcasts.
**Paramters:**
- `title`: string of show name.

### copyright
```python
copyright(copyrightd; str)
```
Set the copyright for the show.
**Paramters:**
- `copyright`: string of copyright information.

### feed_url_new
```python
feed_url_new(url: str)
```
Set url of new rss feed location.
Only necessary if switching urls for rss feed.
**Paramters:**
- `url`: string of url pointing to rss feed.

### block
```python
block()
```
Removes podcast from apple directory.

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
**Paramters:**
- `token`: string of token.

### generator
```python
generator(url: str)
```
Set url of rss generator.
**Paramters:**
- `url`: string of url.

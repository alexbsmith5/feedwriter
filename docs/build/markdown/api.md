<a id="module-feedwriter.podcast_feed"></a>

<a id="api-reference"></a>

# API Reference

<a id="feedwriter.podcast_feed.PodcastFeed"></a>

### *class* feedwriter.podcast_feed.PodcastFeed

PodcastFeed Class.

<a id="feedwriter.podcast_feed.PodcastFeed.link_feed"></a>

#### link_feed(url: str)

Set url of rss feed. Should be a url that points to the `.xml` or `.rss` file where it is hosted.

* **Parameters:**
  **url** (*string*) – url pointing to a `.xml` or `.rss` file.

<a id="feedwriter.podcast_feed.PodcastFeed.title"></a>

#### title(title: str)

Set show title.

* **Parameters:**
  **title** (*string*) – show name.

<a id="feedwriter.podcast_feed.PodcastFeed.description"></a>

#### description(description: str, cdata: bool = False)

Set show description.

* **Parameters:**
  * **description** (*string*) – show description.
  * **cdata** (*bool*) – whether or not rich html is included. Ex. `<a>`, `<p>`, `<li>`, etc.

<a id="feedwriter.podcast_feed.PodcastFeed.image"></a>

#### image(url: str)

Set show artwork.

* **Parameters:**
  **url** (*string*) – url pointing to a `.jpg` or `.png`.

<a id="feedwriter.podcast_feed.PodcastFeed.language"></a>

#### language(language: str)

Set show language.

* **Parameters:**
  **language** (*string*) – language from the [ISO 639](https://www.loc.gov/standards/iso639-2/php/code_list.php) specification.

<a id="feedwriter.podcast_feed.PodcastFeed.category"></a>

#### category(category: str, subcategory: str = '')

Set show category.

* **Parameters:**
  **category** (*string*) – category from the [Apple Podcasts categories](https://podcasters.apple.com/support/1691-apple-podcasts-categories) list.

<a id="feedwriter.podcast_feed.PodcastFeed.explicit"></a>

#### explicit(explicit: bool)

Set show as explicit or not.

* **Parameters:**
  **explicit** (*bool*) – `true` for explicit and `false` for not explicit.

<a id="feedwriter.podcast_feed.PodcastFeed.guid"></a>

#### guid(guid: str)

Set guid (globally unique identifier) for show.

* **Parameters:**
  * **guid** (*string*) – UUIDv5 value.
  * **author** (*string*) – one or multiple author names.

<a id="feedwriter.podcast_feed.PodcastFeed.author"></a>

#### author(author: str)

Set show author(s).

* **Parameters:**
  **author** (*string*) – one or multiple author names.

<a id="feedwriter.podcast_feed.PodcastFeed.link_page"></a>

#### link_page(url: str)

Set link to show’s external website.

* **Parameters:**
  **url** (*string*) – url pointing to a website.

<a id="feedwriter.podcast_feed.PodcastFeed.itunes_title"></a>

#### itunes_title(title: str)

Set specific title for show on Apple Podcasts.

* **Parameters:**
  **title** (*string*) – show name.

<a id="feedwriter.podcast_feed.PodcastFeed.type"></a>

#### type(type: str)

Set show as either `episodic` or `serial`.

If `serial` type is chosen, the `<itunes:episode>` tag must be specified for each post.

* **Parameters:**
  **type** (*string*) – contains either `episodic` or `serial`.

<a id="feedwriter.podcast_feed.PodcastFeed.copyright"></a>

#### copyright(copyright: str)

Set show copyright information.

* **Parameters:**
  **copyright** (*string*) – copyright information.

<a id="feedwriter.podcast_feed.PodcastFeed.feed_url_new"></a>

#### feed_url_new(url: str)

Set url of new rss feed location

Only necessary if changing url of rss feed.

* **Parameters:**
  **url** (*string*) – url pointing to new rss feed location.

<a id="feedwriter.podcast_feed.PodcastFeed.block"></a>

#### block()

Disable importing of show to podcast hosting platforms.

Unless you are trying to block the feed, don’t use this function.
Don’t use if not trying to block.

<a id="feedwriter.podcast_feed.PodcastFeed.complete"></a>

#### complete()

Set show as complete, meaning no new episodes will be added.

<a id="feedwriter.podcast_feed.PodcastFeed.verify"></a>

#### verify(token: str)

Set token to verify podcast with Apple Podcasts.

Token will be provided by Apple during the verification process.

* **Parameters:**
  **token** (*string*) – token provided by Apple.

<a id="feedwriter.podcast_feed.PodcastFeed.funding"></a>

#### funding(url: str, name: str)

Set a donation/funding link for the podcast.

* **Parameters:**
  **url** (*string*) – url pointing to a donation/funding website.

<a id="feedwriter.podcast_feed.PodcastFeed.generator"></a>

#### generator(url: str)

Set url of rss generator website.

* **Parameters:**
  **url** (*string*) – url pointing to rss generator website.

<a id="feedwriter.podcast_feed.PodcastFeed.get_post_index"></a>

#### get_post_index(title: str) → int

Find the index of a post from the title.

* **Parameters:**
  **title** (*string*) – exact title of a post.
* **Returns:**
  Index number of post if found, `-1` if not found.
* **Return type:**
  int

<a id="feedwriter.podcast_feed.PodcastFeed.post_title"></a>

#### post_title(title: str, index: int = -1)

Set title for post.

* **Parameters:**
  * **title** (*string*) – post title.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.podcast_feed.PodcastFeed.post_enclosure"></a>

#### post_enclosure(url: str, file_size: int, type: str, index: int = -1)

Set url, length, and type of media for post.

* **Parameters:**
  * **url** (*string*) – url pointing to a mp3 file.
  * **length** (*int*) – file size of file in bytes.
  * **type** (*string*) – mime type of file (usually `audio/mpeg`). Options `audio/x-m4a`, `audio/mpeg`, `video/quicktime`, `video/mp4`, `video/x-m4v`, `application/pdf`.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.podcast_feed.PodcastFeed.post_guid"></a>

#### post_guid(guid: str, index: int = -1)

Set guid (globally unique identifier) for post.

* **Parameters:**
  * **guid** (*string*) – unique text.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.podcast_feed.PodcastFeed.post_date"></a>

#### post_date(date: str | datetime, index: int = -1)

Set date of the post’s release.

* **Parameters:**
  * **date** (*string* *or* *datetime object*) – Either a string of date following the [RFC 2822 specification](https://datatracker.ietf.org/doc/html/rfc2822#section-3.3) exactly, or datetime object with optional tzinfo (assumes utc).
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.podcast_feed.PodcastFeed.post_description"></a>

#### post_description(description: str, cdata: bool = False, index: int = -1)

Set post description.

* **Parameters:**
  * **description** (*string*) – post description.
  * **cdata** (*bool*) – whether or not rich html is included. Ex. `<a>`, `<p>`, `<li>`, etc.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.podcast_feed.PodcastFeed.post_duration"></a>

#### post_duration(seconds: int, index: int = -1)

Set the length of audio, in seconds.

* **Parameters:**
  * **seconds** (*int*) – number of seconds.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.podcast_feed.PodcastFeed.post_link"></a>

#### post_link(url: str, index: int = -1)

Set link to external website for post.

* **Parameters:**
  * **url** (*string*) – url pointing to a website.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.podcast_feed.PodcastFeed.post_image"></a>

#### post_image(url: str, index: int = -1)

Set image for post.

* **Parameters:**
  * **url** (*string*) – url pointing to a `.jpg` or `.png`.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.podcast_feed.PodcastFeed.post_explicit"></a>

#### post_explicit(explicit: bool, index: int = -1)

Set post as explicit or not.

* **Parameters:**
  * **explicit** (*bool*) – `true` for explicit and `false` for not explicit.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.podcast_feed.PodcastFeed.post_itunes_title"></a>

#### post_itunes_title(title: str, index: int = -1)

Set specific title for post on Apple Podcasts.

* **Parameters:**
  * **title** (*string*) – post name.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.podcast_feed.PodcastFeed.post_episode"></a>

#### post_episode(num: int, index: int = -1)

Add post’s episode number.

Only required for shows of `serial` type.

* **Parameters:**
  * **num** (*int*) – non-zero episode number.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.podcast_feed.PodcastFeed.post_season"></a>

#### post_season(num: int, index: int = -1)

Add post’s season number.

Only required for shows of `serial` type.

* **Parameters:**
  * **num** (*int*) – non-zero season number.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.podcast_feed.PodcastFeed.post_type"></a>

#### post_type(type: str, index: int = -1)

Set episode as `full`, `trailer`, or `bonus`.

* **Parameters:**
  * **type** (*string*) – type of `full`, `trailer`, or `bonus`.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.podcast_feed.PodcastFeed.post_chapters"></a>

#### post_chapters(url: str, type: str, index: int = -1)

Set url of chapters file.

File must follow the [podcastindex.org json chapters format](https://github.com/Podcastindex-org/podcast-namespace/blob/main/docs/examples/chapters/jsonChapters.md).

* **Parameters:**
  * **url** (*string*) – url pointing to a `.json` file.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.podcast_feed.PodcastFeed.post_transcript"></a>

#### post_transcript(url: str, type: str, index: int = -1)

Set url of transcript file.

File must follow the [podcastindex.org transcript format](https://github.com/Podcastindex-org/podcast-namespace/blob/main/docs/examples/transcripts/transcripts.md).

* **Parameters:**
  * **url** (*string*) – url pointing to a transcript file.
  * **type** (*string*) – mime type of file. Options `text/plain`, `text/html`, `text/vtt`, `application/json` or `application/x-subrip`.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.podcast_feed.PodcastFeed.post_block"></a>

#### post_block(index: int = -1)

Add post block (hides epsiode in Apple Podcasts.

Only call function if trying to block episodes.

* **Parameters:**
  **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.podcast_feed.PodcastFeed.new_post"></a>

#### new_post(\*\*kwargs)

Create new post, using optional keyword arguments to add tags. Each parameter is calling a specific episode tag function with `post_{arg}` format.

Parameters can either be passed directly or with a tuple. The tuple type is used when the function takes in more than one paramater.

* **Parameters:**
  * **title** (*string*) – (optional) post title.
  * **enclosure** (*tuple*) – (optional) `(url, length, type)`.
  * **guid** (*string*) – (optional) unique text.
  * **date** (*string* *or* *datetime object*) – (optional) release date of post.
  * **description** (*string*) – (optional) post description.
  * **duration** (*int*) – (optional) length of audio (in seconds).
  * **link** (*string*) – (optional) url of external website.
  * **image** (*string*) – (optional) url of image.
  * **explicit** (*bool*) – (optional) set explicit.
  * **itunes_title** (*string*) – (optional) itunes-specific name.
  * **episode** (*int*) – (optional) episode number.
  * **season** (*int*) – (optional) season number.
  * **type** (*string*) – (optional) episode type.
  * **chapters** (*tuple*) – (optional) `(url, type)`.
  * **transcript** (*tuple*) – (optional) `(url, type)`.
  * **block** (*tuple*) – (optional) hide post. Use empty tuple `()`.

<a id="feedwriter.podcast_feed.PodcastFeed.write"></a>

#### write(path: Path | str)

Write tree to .xml file.

* **Parameters:**
  **path** (*path object* *or* *string*) – location of output file.

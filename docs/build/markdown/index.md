# feedwriter documentation

## API Reference

### *class* feedwriter.podcast_feed.PodcastFeed(test=None)

PodcastFeed Class

#### title(title: str)

Set show title.

* **Parameters:**
  **title** (*string*) – show name.

#### description(description: str, cdata: bool = False)

Set show description.

* **Parameters:**
  * **description** (*string*) – show description.
  * **cdata** (*bool*) – whether or not rich html is included. Ex. `<a>`, `<p>`, `<li>`, etc.

#### image(url: str)

Set show artwork.

* **Parameters:**
  **url** (*string*) – url pointing to a `.jpg` or `.png`.

#### language(language: str)

Set show language.

* **Parameters:**
  **language** (*string*) – language from the [ISO 639](https://www.loc.gov/standards/iso639-2/php/code_list.php) specification.

#### category(category: str, subcategory: str = '')

Set show category.

* **Parameters:**
  **category** (*string*) – category from the [Apple Podcasts categories](https://podcasters.apple.com/support/1691-apple-podcasts-categories) list.

#### explicit(explicit: bool)

Set show as explicit or not.

* **Parameters:**
  **explicit** (*bool*) – `true` for explicit and `false` for not explicit.

#### author(author: str)

Set show author(s).

* **Parameters:**
  **author** (*string*) – one or multiple author names.

#### link(url: str)

Set link to show’s external website.

* **Parameters:**
  **url** (*string*) – url pointing to a website.

#### itunes_title(title: str)

Set specific title for show on Apple Podcasts.

* **Parameters:**
  **title** (*string*) – show name.

#### type(type: str)

Set show as either `episodic` or `serial`.

If `serial` type is chosen, the `<itunes:episode>` tag must be specified for each post.

* **Parameters:**
  **type** (*string*) – contains either `episodic` or `serial`.

#### copyright(copyright: str)

Set show copyright information.

* **Parameters:**
  **copyright** (*string*) – copyright information.

#### feed_url_new(url: str)

Set url of new rss feed location

Only necessary if changing url of rss feed.

* **Parameters:**
  **url** (*string*) – url pointing to new rss feed location.

#### block()

Remove show from Apple Podcasts directory.

Don’t use if not trying to block.

#### complete()

Set show as complete, meaning no new episodes will be added.

#### verify(token: str)

Set token to verify podcast with Apple Podcasts.

Token will be provided by Apple during the verification process.

* **Parameters:**
  **token** (*string*) – token providec by Apple.

#### generator(url: str)

Set url of rss generator website.

* **Parameters:**
  **url** (*string*) – url pointing to rss generator website.

#### get_post_index(title: str) → int

Find the index of a post from the title.

* **Parameters:**
  **title** (*string*) – exact title of a post.
* **Returns:**
  Index number of post if found, `-1` if not found.
* **Return type:**
  int

#### post_title(title: str, index: int = -1)

Set title for post.

* **Parameters:**
  * **title** (*string*) – post title.
  * **index** (*int*) – (optional) index of post; defaults to last created.

#### post_enclosure(url: str, file_size: int, type: str, index: int = -1)

Set url, length, and type of media for post.

* **Parameters:**
  * **url** (*string*) – url pointing to a mp3 file.
  * **length** (*int*) – file size of file in bytes.
  * **type** (*string*) – mime type of file (usually `audio/mpeg`). Options `audio/x-m4a`, `audio/mpeg`, `video/quicktime`, `video/mp4`, `video/x-m4v`, `application/pdf`.
  * **index** (*int*) – (optional) index of post; defaults to last created.

#### post_guid(guid: str, index: int = -1)

Set guid (globally unique identifier) for post.

* **Parameters:**
  * **guid** (*string*) – unique text.
  * **index** (*int*) – (optional) index of post; defaults to last created.

#### post_date(date: str | datetime, index: int = -1)

Set date of the post’s release.

* **Parameters:**
  * **date** (*string* *or* *datetime object*) – Either a string of date following the [RFC 2822 specification](https://datatracker.ietf.org/doc/html/rfc2822#section-3.3) exactly, or datetime object with optional tzinfo (assumes utc).
  * **index** (*int*) – (optional) index of post; defaults to last created.

#### post_description(description: str, cdata: bool = False, index: int = -1)

Set post description.

* **Parameters:**
  * **description** (*string*) – post description.
  * **cdata** (*bool*) – whether or not rich html is included. Ex. `<a>`, `<p>`, `<li>`, etc.
  * **index** (*int*) – (optional) index of post; defaults to last created.

#### post_duration(seconds: int, index: int = -1)

Set the length of audio, in seconds.

* **Parameters:**
  * **seconds** (*int*) – number of seconds.
  * **index** (*int*) – (optional) index of post; defaults to last created.

#### post_link(url: str, index: int = -1)

Set link to external website for post.

* **Parameters:**
  * **url** (*string*) – url pointing to a website.
  * **index** (*int*) – (optional) index of post; defaults to last created.

#### post_image(url: str, index: int = -1)

Set image for post.

* **Parameters:**
  * **url** (*string*) – url pointing to a `.jpg` or `.png`.
  * **index** (*int*) – (optional) index of post; defaults to last created.

#### post_explicit(explicit: bool, index: int = -1)

Set post as explicit or not.

* **Parameters:**
  * **explicit** (*bool*) – `true` for explicit and `false` for not explicit.
  * **index** (*int*) – (optional) index of post; defaults to last created.

#### post_itunes_title(title: str, index: int = -1)

Set specific title for post on Apple Podcasts.

* **Parameters:**
  * **title** (*string*) – post name.
  * **index** (*int*) – (optional) index of post; defaults to last created.

#### post_episode(num: int, index: int = -1)

Add post’s episode number.

Only required for shows of `serial` type.

* **Parameters:**
  * **num** (*int*) – episode number
  * **index** (*int*) – (optional) index of post; defaults to last created.

#### post_season(num: int, index: int = -1)

Add post’s season number.

Only required for shows of `serial` type.

* **Parameters:**
  * **num** (*int*) – season number
  * **index** (*int*) – (optional) index of post; defaults to last created.

#### post_type(type: str, index: int = -1)

Set episode as `full`, `trailer`, or `bonus`.

* **Parameters:**
  * **type** (*string*) – type of `full`, `trailer`, or `bonus`.
  * **index** (*int*) – (optional) index of post; defaults to last created.

#### post_chapters(url: str, type: str, index: int = -1)

Set url of chapters file.

File must follow the [podcastindex.org json chapters format](https://github.com/Podcastindex-org/podcast-namespace/blob/main/docs/examples/chapters/jsonChapters.md).

* **Parameters:**
  * **url** (*string*) – url pointing to a `.json` file.
  * **index** (*int*) – (optional) index of post; defaults to last created.

#### post_transcript(url: str, type: str, index: int = -1)

Set url of transcript file.

File must follow the [podcastindex.org transcript format](https://github.com/Podcastindex-org/podcast-namespace/blob/main/docs/examples/transcripts/transcripts.md).

* **Parameters:**
  * **url** (*string*) – url pointing to a transcript file.
  * **type** (*string*) – mime type of file. Options `text/plain`, `text/html`, `text/vtt`, `application/json` or `application/x-subrip`.
  * **index** (*int*) – (optional) index of post; defaults to last created.

#### post_block(block: bool, index: int = -1)

Add post block (hides epsiode in Apple Podcasts.

Only call function if trying to block episodes.

* **Parameters:**
  **index** (*int*) – (optional) index of post; defaults to last created.

#### new_post(\*\*kwargs)

Create new post, using optional keyword arguments to add tags. Each parameter is calling a specific episode tag function with `post_{arg}` format.

Parameters can either be passed directly or with a tuple. The tuple type is used when the function takes in more than one paramater.

#### write(path: Path)

Write tree to .xml file.

* **Parameters:**
  **path** (*path object*) – location of output file.

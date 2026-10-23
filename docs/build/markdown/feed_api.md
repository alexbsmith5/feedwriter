<a id="module-feedwriter.feed"></a>

<a id="feed-class-api-reference"></a>

# Feed Class API Reference

<a id="feedwriter.feed.Feed"></a>

### *class* feedwriter.feed.Feed(namespaces: dict[str, str] | None = None)

Create Feed class.

* **Parameters:**
  **namespaces** (*dict* *[**str* *,* *str* *]*) – (optional) dictionary with namespace and it’s url.

<a id="feedwriter.feed.Feed.channel_tag"></a>

#### channel_tag(tag: str, content: str | None = None, \*\*kwargs: str)

Create element in channel tag.

* **Parameters:**
  * **tag** (*string*) – name of the element.
  * **content** (*string*) – (optional) value enclosed in between the start and end of the element.
  * **kwargs** (*string*) – (optional) name-value pair in the element.

<a id="feedwriter.feed.Feed.item_tag"></a>

#### item_tag(tag: str, content: str | None = None, index: int = -1, \*\*kwargs: str)

Create element in already exisisting item tag.

* **Parameters:**
  * **tag** (*string*) – name of the element.
  * **content** (*string*) – (optional) value enclosed in between the start and end of the element.
  * **index** (*int*) – (optional) index of item; defaults to last created.
  * **kwargs** (*string*) – (optional) name-value pair in the element.

<a id="feedwriter.feed.Feed.new_item"></a>

#### new_item(tag: str | None = None, content: str | None = None, \*\*kwargs: str)

Create new item item tag and optionally add one element.

* **Parameters:**
  * **tag** (*string*) – (optional) name of the element.
  * **content** (*string*) – (optional) value enclosed in between the start and end of the element.
  * **index** (*int*) – (optional) index of item; defaults to last created.
  * **kwargs** (*string*) – (optional) name-value pair in the element.

<a id="feedwriter.feed.Feed.write"></a>

#### write(path: Path | str)

Write tree to .xml file.

* **Parameters:**
  **path** (*path object* *or* *string*) – location of output file.

<a id="feedwriter.feed.Feed.title"></a>

#### title(text)

Set title.

* **Parameters:**
  **text** (*string*) – title.

<a id="feedwriter.feed.Feed.link"></a>

#### link(url: str)

Set link to show’s external website.

* **Parameters:**
  **url** (*string*) – url pointing to a website.

<a id="feedwriter.feed.Feed.description"></a>

#### description(text: str, cdata: bool = False)

Set description.

* **Parameters:**
  * **text** (*string*) – description.
  * **cdata** (*bool*) – whether or not rich html is included. Ex. `<a>`, `<p>`, `<li>`, etc.

<a id="feedwriter.feed.Feed.language"></a>

#### language(text: str)

Set show language.

* **Parameters:**
  **text** (*string*) – language from the [ISO 639](https://www.loc.gov/standards/iso639-2/php/code_list.php) specification.

<a id="feedwriter.feed.Feed.copyright"></a>

#### copyright(text: str)

Set show copyright information.

* **Parameters:**
  **text** (*string*) – copyright information.

<a id="feedwriter.feed.Feed.web_master"></a>

#### web_master(text: str)

Set the email address for person responsible for technical issues.

Example: [betty@herald.com](mailto:betty@herald.com) (Betty Guernsey)

* **Parameters:**
  **text** (*string*) – email address w/ accompanying text.

<a id="feedwriter.feed.Feed.pub_date"></a>

#### pub_date(date: str | datetime)

Set date of last publication.

* **Parameters:**
  * **date** (*string* *or* *datetime object*) – Either a string of date following the [RFC 2822 specification](https://datatracker.ietf.org/doc/html/rfc2822#section-3.3) exactly, or datetime object with optional tzinfo (assumes utc).
  * **index** – (optional) index of post; defaults to last created.

<a id="feedwriter.feed.Feed.last_build_date"></a>

#### last_build_date(date: str | datetime)

Set date of last time content was changed.

* **Parameters:**
  * **date** (*string* *or* *datetime object*) – 

    Either a string of date following the [RFC 2822 specification](https://datatracker.ietf.org/doc/html/rfc2822#section-3.3) exactly, or datetime object with optional tzinfo (assumes utc).
  * **index** – (optional) index of post; defaults to last created.

<a id="feedwriter.feed.Feed.category"></a>

#### category(text: str)

Set category of channel.

* **Parameters:**
  **category** (*string*) – category name.

<a id="feedwriter.feed.Feed.generator"></a>

#### generator(url: str)

Set url of rss generator website.

* **Parameters:**
  **url** (*string*) – url pointing to rss generator website.

<a id="feedwriter.feed.Feed.docs"></a>

#### docs(url: str)

Set url that points to RSS specification.

* **Parameters:**
  **url** (*string*) – url pointing to the RSS specification.

<a id="feedwriter.feed.Feed.ttl"></a>

#### ttl(num: int)

Set number of minutes a channel can be cached before refreshing from source

* **Parameters:**
  **num** (*int*) – number of minutes

<a id="feedwriter.feed.Feed.image"></a>

#### image(url: str, title: str, link: str)

Set url that points to RSS specification.
Set image that can be displayed with the channel.

* **Parameters:**
  * **url** (*string*) – url pointing to a `.gif`, `.jpg`, or `.png`.
  * **title** (*string*) – name of the image (should be the same as the <title> channel tag).
  * **link** (*string*) – url of the site (should be the same as the <link> channel tag).

<a id="feedwriter.feed.Feed.skip_hours"></a>

#### skip_hours(\*hours: int)

Set hours of the day (GMT) where aggregators should skip updating the feed.

* **Parameters:**
  **hours** (*tuple* *[**int* *,*  *...* *]*) – pass in number for hour (0-24).

<a id="feedwriter.feed.Feed.skip_days"></a>

#### skip_days(\*text: str)

Set hours of the day (GMT) where aggregators should skip updating the feed.
Set days of the week where aggregators should skip updating the feed.

* **Parameters:**
  **text** (*tuple* *[**str* *,*  *...* *]*) – pass in days of week (ex. Monday, Tuesday, etc.).

<a id="feedwriter.feed.Feed.item_title"></a>

#### item_title(title: str, index: int = -1)

Set title for post.

* **Parameters:**
  * **title** (*string*) – post title.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.feed.Feed.item_link"></a>

#### item_link(url: str, index: int = -1)

Set link to an external website, or item.

* **Parameters:**
  * **url** (*string*) – url pointing to a webpage.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.feed.Feed.item_description"></a>

#### item_description(text: str, cdata: bool = False, index: int = -1)

Set item description.

* **Parameters:**
  * **text** (*string*) – description.
  * **cdata** (*bool*) – whether or not rich html is included. Ex. `<a>`, `<p>`, `<li>`, etc.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.feed.Feed.item_enclosure"></a>

#### item_enclosure(url: str, file_size: int, type: str, index: int = -1)

Describe a media object attatched to the item.

* **Parameters:**
  * **url** (*string*) – url pointing to a mp3 file.
  * **length** (*int*) – file size of file in bytes.
  * **type** (*string*) – mime type of file (usually `audio/mpeg`). Options `audio/x-m4a`, `audio/mpeg`, `video/quicktime`, `video/mp4`, `video/x-m4v`, `application/pdf`.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.feed.Feed.item_guid"></a>

#### item_guid(text: str, index: int = -1)

Set guid (globally unique identifier) for an item.

* **Parameters:**
  * **text** (*string*) – unique text.
  * **index** (*int*) – (optional) index of post; defaults to last created.

<a id="feedwriter.feed.Feed.item_date"></a>

#### item_date(date: str | datetime, index: int = -1)

Set date of the post’s release.

* **Parameters:**
  * **date** (*string* *or* *datetime object*) – 

    Either a string of date following the [RFC 2822 specification](https://datatracker.ietf.org/doc/html/rfc2822#section-3.3) exactly, or datetime object with optional tzinfo (assumes utc).
  * **index** (*int*) – (optional) index of post; defaults to last created.

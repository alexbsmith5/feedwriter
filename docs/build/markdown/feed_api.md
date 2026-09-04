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

<a id="feedwriter.feed.Feed.description"></a>

#### description(text: str, cdata: bool = False)

Set description.

* **Parameters:**
  * **text** (*string*) – description.
  * **cdata** (*bool*) – whether or not rich html is included. Ex. `<a>`, `<p>`, `<li>`, etc.

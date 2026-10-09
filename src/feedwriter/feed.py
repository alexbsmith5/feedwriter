import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

from .helpers import _escape


class Feed:
    def __init__(self, namespaces: dict[str, str] | None = None) -> None:
        """
        Create Feed class.

        :param namespaces: (optional) dictionary with namespace and it's url.
        :type namespaces: dict[str, str]
        """
        xml_declaration = {"version": "2.0"}
        if namespaces is not None:
            xml_declaration = xml_declaration | namespaces

        self.root: ET.Element = ET.Element("rss", xml_declaration)
        self.channel: ET.Element = ET.SubElement(self.root, "channel")
        self.tree: ET.ElementTree = ET.ElementTree(self.root)
        self.item_list: list[ET.Element] = []

    def _tag(
        self,
        index: int | ET.Element | None,
        tag: str,
        content: str | None = None,
        **kwargs: str,
    ):

        # initialize empty attribute dictionary
        attributes: dict[str, str] = {}

        # add kwargs to attributes
        for attrib, value in kwargs.items():
            attributes[attrib] = value

        # create element
        def element(
            parent_element: ET.Element,
            tag: str,
            attributes: dict[str, str],
            content: str | None,
        ) -> ET.Element:
            element = ET.SubElement(parent_element, tag, attributes)
            if content is not None:
                element.text = content
            return element

        # set specific parent elements depending on type of index
        if isinstance(index, ET.Element):
            return element(index, tag, attributes, content)
        elif index is None:
            return element(self.channel, tag, attributes, content)
        else:
            return element(self.item_list[index], tag, attributes, content)

    def channel_tag(self, tag: str, content: str | None = None, **kwargs: str):
        """
        Create element in channel tag.

        :param tag: name of the element.
        :type tag: string
        :param content: (optional) value enclosed in between the start and end of the element.
        :type content: string
        :param kwargs: (optional) name-value pair in the element.
        :type kwargs: string
        """
        return self._tag(None, tag, content, **kwargs)

    def item_tag(
        self, tag: str, content: str | None = None, index: int = -1, **kwargs: str
    ):
        """
        Create element in already exisisting item tag.

        :param tag: name of the element.
        :type tag: string
        :param content: (optional) value enclosed in between the start and end of the element.
        :type content: string
        :param index: (optional) index of item; defaults to last created.
        :type index: int
        :param kwargs: (optional) name-value pair in the element.
        :type kwargs: string
        """
        return self._tag(index, tag, content, **kwargs)

    def new_item(
        self, tag: str | None = None, content: str | None = None, **kwargs: str
    ):
        """
        Create new item item tag and optionally add one element.

        :param tag: (optional) name of the element.
        :type tag: string
        :param content: (optional) value enclosed in between the start and end of the element.
        :type content: string
        :param index: (optional) index of item; defaults to last created.
        :type index: int
        :param kwargs: (optional) name-value pair in the element.
        :type kwargs: string
        """
        self.item_list.append(ET.SubElement(self.channel, "item"))
        if tag is not None:
            self.item_tag(tag, content, -1, **kwargs)

    def _parse_kwargs(self, func_map, **kwargs):
        """
        Parse kwargs and run function if in map
        :param func_map: map of names and functions.
        :type func_map: dict[str, func]
        :param kwargs: arguments from function call.
        :type kwargs: dict
        """
        for func, value in kwargs.items():
            if func in func_map:
                mapped_function = func_map[func]
                if isinstance(value, tuple):
                    mapped_function(*value)
                else:
                    mapped_function(value)

    def write(self, path: Path | str):
        """
        Write tree to .xml file.

        :param path: location of output file.
        :type path: path object or string
        """
        self.tree = ET.ElementTree(self.root)
        self.tree.write(path, xml_declaration=True, encoding="UTF-8")

    # shared tags

    def title(self, text):
        """
        Set title.

        :param text: title.
        :type text: string
        """
        self.channel_tag("title", text)

    def description(self, text: str, cdata: bool = False):
        """
        Set description.

        :param text: description.
        :type text: string
        :param cdata: whether or not rich html is included. Ex. ``<a>``, ``<p>``, ``<li>``, etc.
        :type cdata: bool
        """
        if cdata:
            self.channel_tag("description", f"<![CDATA[ {text} ]]>")
        else:
            self.channel_tag("description", text)

    def link(self, url: str):
        """
        Set link to show's external website.

        :param url: url pointing to a website.
        :type url: string
        """
        self.channel_tag("link", quote(url, safe="/:"))

    def generator(self, url: str):
        """
        Set url of rss generator website.

        :param url: url pointing to rss generator website.
        :type url: string
        """
        self.channel_tag("generator", quote(url, safe="/:"))

    # item tags

    def item_title(self, title: str, index: int = -1):
        """
        Set title for post.

        :param title: post title.
        :type title: string
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        self.item_tag("title", title, index=index)

    def item_link(self, url: str, index: int = -1):
        """
        Set link to an external website, or item.

        :param url: url pointing to a webpage.
        :type url: string
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        self.item_tag("link", quote(url, safe="/:"), index=index)

    def item_description(self, text: str, cdata: bool = False, index: int = -1):
        """
        Set item description.

        :param text: description.
        :type text: string
        :param cdata: whether or not rich html is included. Ex. ``<a>``, ``<p>``, ``<li>``, etc.
        :type cdata: bool
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        if cdata:
            self.item_tag("description", f"<![CDATA[ {text} ]]>", index=index)
        else:
            self.item_tag("description", _escape(text), index=index)

    def item_enclosure(self, url: str, file_size: int, type: str, index: int = -1):
        """
        Describe a media object attatched to the item.

        :param url: url pointing to a mp3 file.
        :type url: string
        :param length: file size of file in bytes.
        :type length: int
        :param type: mime type of file (usually ``audio/mpeg``). Options ``audio/x-m4a``, ``audio/mpeg``, ``video/quicktime``, ``video/mp4``, ``video/x-m4v``, ``application/pdf``.

        :type type: string
        :param index: (optional) index of post; defaults to last created.
        :type index: int

        """
        self.item_tag(
            "enclosure",
            index=index,
            url=quote(url, safe="/:"),
            length=str(file_size),
            type=type,
        )

    def item_guid(self, text: str, index: int = -1):
        """
        Set guid (globally unique identifier) for an item.

        :param text: unique text.
        :type text: string
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        self.item_tag("guid", text, index=index)

    def item_date(self, date: str | datetime, index: int = -1):
        """
        Set date of the post's release.

        :param date: Either a string of date following the `RFC 2822 specification <https://datatracker.ietf.org/doc/html/rfc2822#section-3.3>`_ exactly, or datetime object with optional tzinfo (assumes utc).
        :type date: string or datetime object
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        if isinstance(date, str):
            self.item_tag("pubdate", date, index=index)
        else:  # if datetime object
            if date.tzinfo is not None:
                date_str = date.strftime("%a, %d %b %Y %H:%M:%S %z")
            else:
                date_str = date.strftime("%a, %d %b %Y %H:%M:%S +0000")  # assume utc
            self.item_tag("pubdate", date_str, index=index)

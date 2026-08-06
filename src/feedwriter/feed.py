import xml.etree.ElementTree as ET
from pathlib import Path


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
        self.item: list[ET.Element] = []

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
            return element(self.item[index], tag, attributes, content)

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
        self.item.append(ET.SubElement(self.channel, "item"))
        if tag is not None:
            self.item_tag(tag, content, -1, **kwargs)

    def write(self, path: Path | str):
        """
        Write tree to .xml file.

        :param path: location of output file.
        :type path: path object or string
        """
        self.tree = ET.ElementTree(self.root)
        self.tree.write(path, xml_declaration=True, encoding="UTF-8")

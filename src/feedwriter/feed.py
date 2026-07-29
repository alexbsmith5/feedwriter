import xml.etree.ElementTree as ET
from pathlib import Path


class Feed:
    """
    Feed Class.
    """

    def __init__(self) -> None:
        self.root: ET.Element = ET.Element(
            "rss",
            {
                "version": "2.0",
            },
        )
        self.channel: ET.Element = ET.SubElement(self.root, "channel")
        self.tree: ET.ElementTree = ET.ElementTree(self.root)
        self.channel_category: list[ET.Element] = []
        self.item: list[ET.Element] = []

    def _tag(
        self, index: int | None, tag: str, content: str | None = None, **kwargs: str
    ):

        # initialize empty attribute dictionary
        attributes: dict[str, str] = {}

        # add kwargs to attributes
        for attrib, value in kwargs.items():
            attributes[attrib] = value

        if index is None:
            ET.SubElement(self.channel, tag, attributes).text = content
        else:
            ET.SubElement(self.item[index], tag, attributes).text = content

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
        self._tag(None, tag, content, **kwargs)

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
        self._tag(index, tag, content, **kwargs)

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

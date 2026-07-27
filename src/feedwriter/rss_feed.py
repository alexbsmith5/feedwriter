import xml.etree.ElementTree as ET
from pathlib import Path


class RSSFeed:
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

    def new_item(self):
        self.item.append(ET.SubElement(self.channel, "item"))

    def _tag(
        self, index: int | None, tag: str, content: str | None = None, **kwargs: str
    ):

        # initialize empty attribute dictionary
        attributes: dict[str, str] = {}

        # add kwargs to attributes
        for attrib, value in kwargs.items():
            print(f"{attrib}: {value}")
            attributes[attrib] = value

        if index is None:
            ET.SubElement(self.channel, tag, attributes).text = content
        else:
            ET.SubElement(self.item[index], tag, attributes).text = content

    def channel_tag(self, tag: str, content: str | None = None, **kwargs: str):
        self._tag(None, tag, content, **kwargs)

    def item_tag(
        self, tag: str, content: str | None = None, index: int = -1, **kwargs: str
    ):
        self._tag(index, tag, content, **kwargs)

    def write(self, path: Path | str):
        self.tree = ET.ElementTree(self.root)
        self.tree.write(path, xml_declaration=True, encoding="UTF-8")

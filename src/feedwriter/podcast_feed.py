import xml.etree.ElementTree as ET

class PodcastFeed:
    # empty constructor
    def __init__(self):
        self.root = ET.Element("rss", { "version":"2.0", "xmlns:itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd" })
        self.channel = ET.SubElement(self.root, "channel")
        self.tree = ET.ElementTree(self.root)
        self.item = []

    # set title
    def title(self, title: str):
        ET.SubElement(self.channel, "title").text = title

    # set description
    def description(self, description: str):
        ET.SubElement(self.channel, "description").text = description

    # set image
    def image(self, url):
        ET.SubElement(self.channel, "itunes:image", href=url).text

    # set language
    def language(self, language: str):
        ET.SubElement(self.channel, "language").text = language

    # set category
    # TODO: add support for subcategories
    def category(self, category: str):
        ET.SubElement(self.channel, "itunes:category", text=category).text

    # set explicit
    def explicit(self, explicit: bool):
        if explicit:
            text = "true"
        else:
            text = "false"
        ET.SubElement(self.channel, "itunes:explicit").text = text

    # add post with required tags
    def post(self, title, url, file_size, type, guid):
        self.item.append(ET.SubElement(self.channel, "item"))
        ET.SubElement(self.item[-1], "title").text = title
        ET.SubElement(self.item[-1], "enclosure", url=url, length=file_size, type=type)
        ET.SubElement(self.item[-1], "guid").text = guid

    # write tree to xml file
    def write(self, filename):
        self.tree = ET.ElementTree(self.root)
        self.tree.write(filename, xml_declaration=True, encoding="UTF-8")

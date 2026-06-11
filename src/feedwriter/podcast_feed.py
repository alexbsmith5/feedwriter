import xml.etree.ElementTree as ET

class PodcastFeed:
    # empty constructor
    def __init__(self):
        self.root = ET.Element("rss", { "version":"2.0", "xmlns:itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd" })
        self.channel = ET.SubElement(self.root, "channel")
        self.tree = ET.ElementTree(self.root)
        self.item = []

    # write tree to xml file
    def write(self, filename):
        self.tree = ET.ElementTree(self.root)
        self.tree.write(filename, xml_declaration=True, encoding="UTF-8")

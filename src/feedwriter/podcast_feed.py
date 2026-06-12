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

    # set author
    def author(self, author: str):
        ET.SubElement(self.channel, "itunes:author").text = author

    # set link
    def link(self, url: str):
        ET.SubElement(self.channel, "link").text = url

    # set itunes title
    # specific name on apple podcasts
    def itunes_title(self, title: str):
        ET.SubElement(self.channel, "itunes:title").text = title

    # TODO: <itunes:type>
    #  if serial type is chosen, <itunes:episode> tag must be specified for each post

    # set copyright
    def copyright(self, copyright: str):
        ET.SubElement(self.channel, "copyright").text = copyright

    # set url of new feed
    def feed_url_new(self, url: str):
        ET.SubElement(self.channel, "itunes:new-feed-url").text = url

    # set block (removes podcast from apple directory)
    # don't use if not trying to block
    def block(self):
        ET.SubElement(self.channel, "itunes:block").text = "Yes"

    # set complete, no more new episodes will be added
    def complete(self):
        ET.SubElement(self.channel, "itunes:complete").text = "Yes"

    # set token to verify podcast with apple podcasts
    def verify(self, token: str):
        ET.SubElement(self.channel, "itunes:applepodcastsverify").text = token

    # set name of rss-generator
    def generator(self, url: str):
        ET.SubElement(self.channel, "generator").text = url

    # find post index given title
    def get_post_index(self, title: str) -> int:
        index = 0
        for item in self.root.findall(".//item"):
            if item.find('title').text == title:
                return index
            index += 1
        return -1 # if title not found return -1 index

    # add enclosure to post from index
    def post_enclosure(self, url: str, file_size: str, type: str, index: int = -1):
        ET.SubElement(self.item[index], "enclosure", url=url, length=file_size, type=type)

    # add enclosure to post from index
    def post_guid(self, guid: str, index: int = -1):
        ET.SubElement(self.item[index], "guid").text = guid

    # add post with title
    def new_post(self, title: str):
        self.item.append(ET.SubElement(self.channel, "item"))
        ET.SubElement(self.item[-1], "title").text = title

    # add post with required tags
    def new_post_required(self, title: str, url: str, file_size: str, type: str, guid: str):
        self.item.append(ET.SubElement(self.channel, "item"))
        ET.SubElement(self.item[-1], "title").text = title
        self.post_enclosure(url, file_size, type)
        self.post_guid(guid)

    # write tree to xml file
    def write(self, filename):
        self.tree = ET.ElementTree(self.root)
        self.tree.write(filename, xml_declaration=True, encoding="UTF-8")

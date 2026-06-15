import xml.etree.ElementTree as ET

class PodcastFeed:
    # empty constructor
    def __init__(self):
        self.root = ET.Element("rss", { "version":"2.0", "xmlns:itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd", "xmlns:podcast": "https://podcastindex.org/namespace/1.0" })
        self.channel = ET.SubElement(self.root, "channel")
        self.tree = ET.ElementTree(self.root)
        self.item = []

    # channel tags

    # set title
    def title(self, title: str):
        ET.SubElement(self.channel, "title").text = title

    # set description
    def description(self, description: str):
        ET.SubElement(self.channel, "description").text = description

    # set image
    def image(self, url: str):
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
        ET.SubElement(self.channel, "podcast:txt", purpose="applepodcastsverify").text = token

    # set name of rss-generator
    def generator(self, url: str):
        ET.SubElement(self.channel, "generator").text = url

    # episode tags

    # find post index given title
    def get_post_index(self, title: str) -> int:
        index = 0
        for item in self.root.findall(".//item"):
            if item.find('title').text == title:
                return index
            index += 1
        return -1 # if title not found return -1 index

    # add post enclosure to post from index
    def post_enclosure(self, url: str, file_size: int, type: str, index: int = -1):
        ET.SubElement(self.item[index], "enclosure", url=url, length=str(file_size), type=type)

    # add post enclosure
    def post_guid(self, guid: str, index: int = -1):
        ET.SubElement(self.item[index], "guid").text = guid

    # add post date
    # date format according to RFC 2822 specification
    def post_date(self, date: str, index: int = -1):
        # TODO: better way for user to input date
        #  option to input date object?
        ET.SubElement(self.item[index], "pubdate").text = date

    # add post description
    def post_description(self, description: str, index: int = -1):
        ET.SubElement(self.item[index], "description").text = description

    # add post duration (in seconds)
    def post_duration(self, seconds: int, index: int = -1):
        # TODO: add more formats?
        #  itunes docs mention other formats (recommended to stay in seconds
        ET.SubElement(self.item[index], "itunes:duration").text = str(seconds)

    # add post url
    # use when post has corresponsing webpage
    def post_link(self, url: str, index: int = -1):
        ET.SubElement(self.item[index], "link").text = url

    # add post image url
    def post_image(self, url: str, index: int = -1):
        ET.SubElement(self.item[index], "itunes:image", href=url).text

    # add explicit tag
    def post_explicit(self, explicit: bool, index: int = -1):
        if explicit:
            text = "true"
        else:
            text = "false"
        ET.SubElement(self.item[index], "itunes:explicit").text = text

    # add itunes title
    # specific episode name for apple podcasts
    def post_itunes_title(self, title: str, index: int = -1):
        ET.SubElement(self.item[index], "itunes:title").text = title

    # add post number
    # not needed for episodic shows (default)
    def post_episode_number(self, num: int, index: int = -1):
        ET.SubElement(self.item[index], "itunes:episode").text = str(num)

    # add season number
    # not needed for episodic shows (default)
    def post_season_number(self, num: int, index: int = -1):
        ET.SubElement(self.item[index], "itunes:season").text = str(num)

    # add post type
    # options: full, trailer, bonus
    def post_type(self, type: str, index: int = -1):
        ET.SubElement(self.item[index], "itunes:episodeType").text = type

    # add post chapters url
    # url points to file that follows podcastindex.org json chapters format
    def post_chapters(self, url: str, type: str, index: int = -1):
        ET.SubElement(self.item[index], "podcast:chapters", url=url, type=type).text

    # add transcript url
    # url point to file that follows either VTT or SRT transcript format
    def post_transcript(self, url: str, type: str, index: int = -1):
        ET.SubElement(self.item[index], "podcast:transcript", url=url, type=type).text

    # add post block
    # add post block (removes episode from apple directory)
    # don't use if not trying to block
    def post_block(self, block: bool, index: int = -1):
        ET.SubElement(self.item[index], "itunes:block").text = "Yes"

    # add post
    def new_post(self, title: str, url: str, file_size: int, audio_type: str="audio/mpeg", **kwargs):
        self.item.append(ET.SubElement(self.channel, "item"))
        ET.SubElement(self.item[-1], "title").text = title
        self.post_enclosure(url, file_size, audio_type)

        func_map = {
                'guid': self.post_guid,
                'date': self.post_date,
                'link': self.post_link,
                'description': self.post_description,
                'duration': self.post_duration,
                'link': self.post_link,
                'image': self.post_image,
                'explicit': self.post_explicit,
                'itunes_title': self.post_itunes_title,
                'episode_num': self.post_episode_number,
                'seasion_num': self.post_season_number,
                'type': self.post_type,
                # TODO: post_chapters + post_transcript
                #  functions take in two parameters
                'block': self.post_block
        }

        for func, value in kwargs.items():
            if func in func_map:
                mapped_function = func_map[func]
                mapped_function(value)

    # write tree to xml file
    def write(self, filename):
        self.tree = ET.ElementTree(self.root)
        self.tree.write(filename, xml_declaration=True, encoding="UTF-8")

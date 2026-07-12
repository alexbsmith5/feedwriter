import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime


class PodcastFeed:
    """
    PodcastFeed Class
    """

    def __init__(self, test=None):
        self.root = ET.Element(
            "rss",
            {
                "version": "2.0",
                "xmlns:itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
                "xmlns:podcast": "https://podcastindex.org/namespace/1.0",
            },
        )
        self.channel = ET.SubElement(self.root, "channel")
        self.tree = ET.ElementTree(self.root)
        self.channel_category = []
        self.item = []

    # channel tags

    # set title
    def title(self, title: str):
        """
        Set show title.

        :param title: show name.
        :type title: string
        """
        ET.SubElement(self.channel, "title").text = title

    # set description
    def description(self, description: str, cdata: bool = False):
        """
        Set show description.

        :param description: show description.
        :type description: string
        :param cdata: whether or not rich html is included. Ex. ``<a>``, ``<p>``, ``<li>``, etc.
        :type cdata: bool
        """
        if cdata:
            ET.SubElement(
                self.channel, "description"
            ).text = f"<!CDATA[ {description} ]]>"
        else:
            ET.SubElement(self.channel, "description").text = description

    # set image
    def image(self, url: str):
        """
        Set show artwork.

        :param url: url pointing to a ``.jpg`` or ``.png``.
        :type url: string
        """
        ET.SubElement(self.channel, "itunes:image", href=url).text

    # set language
    def language(self, language: str):
        """
        Set show language.

        :param language: language from the `ISO 639 <https://www.loc.gov/standards/iso639-2/php/code_list.php>`_ specification.
        :type language: string
        """
        ET.SubElement(self.channel, "language").text = language

    # set category
    def category(self, category: str, subcategory: str = ""):
        """
        Set show category.

        :param category: category from the `Apple Podcasts categories <https://podcasters.apple.com/support/1691-apple-podcasts-categories>`_ list.
        :type category: string
        """
        self.channel_category.append(
            ET.SubElement(self.channel, "itunes:category", text=category)
        )
        if subcategory != "":
            ET.SubElement(
                self.channel_category[-1], "itunes:category", text=subcategory
            ).text

    # set explicit
    def explicit(self, explicit: bool):
        """
        Set show as explicit or not.

        :param explicit: ``true`` for explicit and ``false`` for not explicit.
        :type explicit: bool
        """
        if explicit:
            text = "true"
        else:
            text = "false"
        ET.SubElement(self.channel, "itunes:explicit").text = text

    # set author
    def author(self, author: str):
        """
        Set show author(s).

        :param author: one or multiple author names.
        :type author: string
        """
        ET.SubElement(self.channel, "itunes:author").text = author

    # set link
    def link(self, url: str):
        """
        Set link to show's external website.

        :param url: url pointing to a website.
        :type url: string
        """
        ET.SubElement(self.channel, "link").text = url

    # set itunes title
    # specific name on apple podcasts
    def itunes_title(self, title: str):
        """
        Set specific title for show on Apple Podcasts.

        :param title: show name.
        :type title: string
        """
        ET.SubElement(self.channel, "itunes:title").text = title

    # set type
    def type(self, type: str):
        """
        Set show as either ``episodic`` or ``serial``.

        If ``serial`` type is chosen, the ``<itunes:episode>`` tag must be specified for each post.

        :param type: contains either ``episodic`` or ``serial``.
        :type type: string
        """
        ET.SubElement(self.channel, "itunes:type").text = type

    # set copyright
    def copyright(self, copyright: str):
        """
        Set show copyright information.

        :param copyright: copyright information.
        :type copyright: string
        """
        ET.SubElement(self.channel, "copyright").text = copyright

    # set url of new feed
    def feed_url_new(self, url: str):
        """
        Set url of new rss feed location

        Only necessary if changing url of rss feed.

        :param url: url pointing to new rss feed location.
        :type url: string
        """
        ET.SubElement(self.channel, "itunes:new-feed-url").text = url

    # set block (removes podcast from apple directory)
    # don't use if not trying to block
    def block(self):
        """
        Remove show from Apple Podcasts directory.
        """
        ET.SubElement(self.channel, "itunes:block").text = "Yes"

    # set complete, no more new episodes will be added
    def complete(self):
        """
        Set show as complete, meaning no new episodes will be added.
        """
        ET.SubElement(self.channel, "itunes:complete").text = "Yes"

    # set token to verify podcast with apple podcasts
    def verify(self, token: str):
        """
        Set token to verify podcast with Apple Podcasts.

        Token will be provided by Apple during the verification process.

        :param token: token providec by Apple.
        :type token: string
        """
        ET.SubElement(
            self.channel, "podcast:txt", purpose="applepodcastsverify"
        ).text = token

    # set name of rss-generator
    def generator(self, url: str):
        """
        Set url of rss generator website.

        :param url: url pointing to rss generator website.
        :type url: string
        """
        ET.SubElement(self.channel, "generator").text = url

    # episode tags

    # find post index given title
    def get_post_index(self, title: str) -> int:
        """
        Find the index of a post from the title.

        :param title: exact title of a post.
        :type title: string
        :return: Index number of post if found, ``-1`` if not found.
        :rtype: int
        """
        index = 0
        for item in self.root.findall(".//item"):
            if item.find("title").text == title:
                return index
            index += 1
        return -1  # if title not found return -1 index

    def post_title(self, title: str, index: int = -1):
        """
        Set title for post.

        :param title: post title.
        :type title: string
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        ET.SubElement(self.item[index], "title").text = title

    # add post enclosure to post from index
    def post_enclosure(self, url: str, file_size: int, type: str, index: int = -1):
        """
        Set url, length, and type of media for post.

        :param url: url pointing to a mp3 file.
        :type url: string
        :param length: file size of file in bytes.
        :type length: int
        :param type: mime type of file (usually ``audio/mpeg``). Options ``audio/x-m4a``, ``audio/mpeg``, ``video/quicktime``, ``video/mp4``, ``video/x-m4v``, ``application/pdf``.

        :type type: string
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        ET.SubElement(
            self.item[index], "enclosure", url=url, length=str(file_size), type=type
        )

    # add post enclosure
    def post_guid(self, guid: str, index: int = -1):
        """
        Set guid (globally unique identifier) for post.

        :param guid: unique text.
        :type guid: string
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        ET.SubElement(self.item[index], "guid").text = guid

    # add post date
    # date format according to RFC 2822 specification
    def post_date(self, date: str | datetime, index: int = -1):
        """
        Set date of the post's release.

        :param date: Either a string of date following the `RFC 2822 specification <https://datatracker.ietf.org/doc/html/rfc2822#section-3.3>`_ exactly, or datetime object with optional tzinfo (assumes utc).
        :type date: string or datetime object
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        if isinstance(date, str):
            ET.SubElement(self.item[index], "pubdate").text = date
        elif isinstance(date, datetime):
            if date.tzinfo is not None:
                date_str = date.strftime("%a, %d %b %Y %H:%M:%S %z")
            else:
                date_str = date.strftime("%a, %d %b %Y %H:%M:%S +0000")  # assume utc
            ET.SubElement(self.item[index], "pubdate").text = date_str

    # add post description
    def post_description(self, description: str, cdata: bool = False, index: int = -1):
        """
        Set post description.

        :param description: post description.
        :type description: string
        :param cdata: whether or not rich html is included. Ex. ``<a>``, ``<p>``, ``<li>``, etc.
        :type cdata: bool
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        if cdata:
            ET.SubElement(
                self.item[index], "description"
            ).text = f"<!CDATA[ {description} ]]>"
        else:
            ET.SubElement(self.item[index], "description").text = description

    # add post duration (in seconds)
    def post_duration(self, seconds: int, index: int = -1):
        """
        Set the length of audio, in seconds.

        :param seconds: number of seconds.
        :type seconds: int
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        ET.SubElement(self.item[index], "itunes:duration").text = str(seconds)

    # add post url
    # use when post has corresponsing webpage
    def post_link(self, url: str, index: int = -1):
        """
        Set link to external website for post.

        :param url: url pointing to a website.
        :type url: string
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        ET.SubElement(self.item[index], "link").text = url

    # add post image url
    def post_image(self, url: str, index: int = -1):
        """
        Set image for post.

        :param url: url pointing to a ``.jpg`` or ``.png``.
        :type url: string
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        ET.SubElement(self.item[index], "itunes:image", href=url).text

    # add explicit tag
    def post_explicit(self, explicit: bool, index: int = -1):
        """
        Set post as explicit or not.

        :param explicit: ``true`` for explicit and ``false`` for not explicit.
        :type explicit: bool
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        if explicit:
            text = "true"
        else:
            text = "false"
        ET.SubElement(self.item[index], "itunes:explicit").text = text

    # add itunes title
    # specific episode name for apple podcasts
    def post_itunes_title(self, title: str, index: int = -1):
        """
        Set specific title for post on Apple Podcasts.

        :param title: post name.
        :type title: string
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        ET.SubElement(self.item[index], "itunes:title").text = title

    # add post number
    # not needed for episodic shows (default)
    def post_episode(self, num: int, index: int = -1):
        """
        Add post's episode number.

        Only required for shows of ``serial`` type.

        :param num: episode number
        :type num: int
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        ET.SubElement(self.item[index], "itunes:episode").text = str(num)

    # add season number
    # not needed for episodic shows (default)
    def post_season(self, num: int, index: int = -1):
        """
        Add post's season number.

        Only required for shows of ``serial`` type.

        :param num: season number
        :type num: int
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        ET.SubElement(self.item[index], "itunes:season").text = str(num)

    # add post type
    # options: full, trailer, bonus
    def post_type(self, type: str, index: int = -1):
        """
        Set episode as ``full``, ``trailer``, or ``bonus``.

        :param type: type of ``full``, ``trailer``, or ``bonus``.
        :type type: string
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        ET.SubElement(self.item[index], "itunes:episodeType").text = type

    # add post chapters url
    # url points to file that follows podcastindex.org json chapters format
    def post_chapters(self, url: str, type: str, index: int = -1):
        """
        Set url of chapters file.

        File must follow the `podcastindex.org json chapters format <https://github.com/Podcastindex-org/podcast-namespace/blob/main/docs/examples/chapters/jsonChapters.md>`_.

        :param url: url pointing to a ``.json`` file.
        :type url: string
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        ET.SubElement(self.item[index], "podcast:chapters", url=url, type=type).text

    # add transcript url
    # url point to file that follows either VTT or SRT transcript format
    def post_transcript(self, url: str, type: str, index: int = -1):
        """
        Set url of transcript file.

        File must follow the `podcastindex.org transcript format <https://github.com/Podcastindex-org/podcast-namespace/blob/main/docs/examples/transcripts/transcripts.md>`_.

        :param url: url pointing to a transcript file.
        :type url: string
        :param type: mime type of file. Options ``text/plain``, ``text/html``, ``text/vtt``, ``application/json`` or ``application/x-subrip``.
        :type type: string
        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        ET.SubElement(self.item[index], "podcast:transcript", url=url, type=type).text

    # add post block
    # add post block (removes episode from apple directory)
    # don't use if not trying to block
    def post_block(self, block: bool, index: int = -1):
        """
        Add post block (hides epsiode in Apple Podcasts.

        Only call function if trying to block episodes.

        :param index: (optional) index of post; defaults to last created.
        :type index: int
        """
        ET.SubElement(self.item[index], "itunes:block").text = "Yes"

    # add post
    def new_post(self, **kwargs):
        """
        Create new post, using optional keyword arguments to add tags. Each parameter is calling a specific episode tag function with ``post_{arg}`` format.

        Parameters can either be passed directly or with a tuple. The tuple type is used when the function takes in more than one paramater.
        """
        self.item.append(ET.SubElement(self.channel, "item"))

        func_map = {
            "title": self.post_title,
            "enclosure": self.post_enclosure,
            "guid": self.post_guid,
            "date": self.post_date,
            "description": self.post_description,
            "duration": self.post_duration,
            "link": self.post_link,
            "image": self.post_image,
            "explicit": self.post_explicit,
            "itunes_title": self.post_itunes_title,
            "episode": self.post_episode,
            "season": self.post_season,
            "type": self.post_type,
            "chapters": self.post_chapters,
            "transcript": self.post_transcript,
            "block": self.post_block,
        }

        for func, value in kwargs.items():
            if func in func_map:
                mapped_function = func_map[func]
                if isinstance(value, tuple):
                    mapped_function(*value)
                else:
                    mapped_function(value)

    def write(self, path: Path):
        """
        Write tree to .xml file.

        :param path: location of output file.
        :type path: path object
        """
        self.tree = ET.ElementTree(self.root)
        self.tree.write(path, xml_declaration=True, encoding="UTF-8")

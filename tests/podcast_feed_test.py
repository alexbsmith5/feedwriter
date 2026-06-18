import xml.etree.ElementTree as ET

from feedwriter.podcast_feed import PodcastFeed

def test_podcast_feed(tmp_path):
    feed_file = tmp_path / "feed.xml"

    feed = PodcastFeed()
    title_text = "Testing Title"
    feed.title(title_text)
    feed.write(feed_file)

    tree = ET.parse(feed_file)
    root = tree.getroot()

    title_element = root.find("./channel/title")

    assert title_element != None
    assert title_element.text == title_text

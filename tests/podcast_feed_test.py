import xml.etree.ElementTree as ET
import pytest

from feedwriter.podcast_feed import PodcastFeed

# return xml root
@pytest.fixture
def get_root(tmp_path):

    def generate(feed_object):
        feed_file = tmp_path / "feed.xml"
        feed_object.write(feed_file)
        return ET.parse(feed_file).getroot()

    return generate

def test_title(get_root):
    feed = PodcastFeed()

    feed.title(test_title)
    test_title = "Testing Title"

    root = get_root(feed)

    assert root.find("./channel/title").text == test_title

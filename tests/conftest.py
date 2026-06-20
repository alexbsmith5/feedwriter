import xml.etree.ElementTree as ET
import pytest

from feedwriter.podcast_feed import PodcastFeed


# create base rss feed
@pytest.fixture
def base_feed(tmp_path):
    return PodcastFeed()


# ns = {"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd" }


# test xml output for text or attrib
@pytest.fixture
def assert_xml(tmp_path):
    def _assert_xml(feed, xpath, expected_text=None, expected_attrib=None):
        tmp_file = tmp_path / "feed.xml"
        feed.write(tmp_file)

        tree = ET.parse(tmp_file)
        root = tree.getroot()

        namespaces = {
            "itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
            "podcast": "https://podcastindex.org/namespace/1.0",
        }

        element = root.find(xpath, namespaces=namespaces)
        assert element is not None, f"Element {xpath} is not found in the XML output."

        if expected_text is not None:
            assert (
                element.text == expected_text
            ), f"Expected {element.tag} to contain {expected_text}, got {element.text}."

        if expected_attrib is not None:
            for key, value in expected_attrib.items():
                assert (
                    element.get(key) == value
                ), f"Expected {key} to contain {value}, got {element.get(key)}."

    return _assert_xml

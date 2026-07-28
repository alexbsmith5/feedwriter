import xml.etree.ElementTree as ET
from pathlib import Path
import pytest

from feedwriter import Feed
from feedwriter import PodcastFeed


# create rss_feed object
@pytest.fixture
def rss_feed() -> Feed:
    return Feed()


# create podcast_feed object
@pytest.fixture
def podcast_feed() -> PodcastFeed:
    return PodcastFeed()


# return element given xpath
def _get_xml_element(rss_feed: Feed, xpath: str, tmp_path: Path) -> ET.Element | None:
    # write tmp_file
    tmp_file = tmp_path / "feed.xml"
    rss_feed.write(tmp_file)

    # load tmp_file in memory
    tree = ET.parse(tmp_file)
    root = tree.getroot()

    # set namespaces
    namespaces: dict[str, str] = {
        "itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
        "podcast": "https://podcastindex.org/namespace/1.0",
        "content": "http://purl.org/rss/1.0/modules/content/",
        "atom": "http://www.w3.org/2005/Atom",
    }

    # return element (if found)
    return root.find(xpath, namespaces)


@pytest.fixture
def assert_xml(tmp_path: Path):
    def _assert_xml(
        rss_feed: Feed,
        func_name: str,
        func_kwargs: dict[str, str],
        xpath: str,
        expected_text: str | None,
        expected_attrib: dict[str, str] | None,
    ):
        # run function w/ kwargs
        mapped_func = getattr(rss_feed, func_name)
        mapped_func(**func_kwargs)

        # check if element exists
        element: ET.Element | None = _get_xml_element(rss_feed, xpath, tmp_path)
        assert element is not None, f"Element {xpath} is not found in the XML output."

        # check expected content
        if expected_text is not None:
            assert element.text == expected_text, (
                f"Expected {element.tag} to contain {expected_text}, got {element.text}."
            )

        # check expected attributes
        if expected_attrib is not None:
            for attrib, value in expected_attrib.items():
                assert element.get(attrib) == value, (
                    f"Expected {attrib} to contain {value}, got {element.get(attrib)}."
                )

    return _assert_xml

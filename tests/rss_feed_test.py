import xml.etree.ElementTree as ET
from pathlib import Path
import pytest

from feedwriter.rss_feed import RSSFeed


# create rss_feed object
@pytest.fixture
def rss_feed() -> RSSFeed:
    return RSSFeed()


# return element given xpath
def _get_xml_element(
    rss_feed: RSSFeed, xpath: str, tmp_path: Path
) -> ET.Element | None:
    # write tmp_file
    tmp_file = tmp_path / "feed.xml"
    rss_feed.write(tmp_file)

    # load tmp_file in memory
    tree = ET.parse(tmp_file)
    root = tree.getroot()

    # return element (if found)
    return root.find(xpath)


@pytest.mark.parametrize(
    ("func_name", "func_kwargs", "xpath", "expected_text", "expected_attrib"),
    [
        (
            "channel_tag",
            {"tag": "title", "content": "Lorem Ipsum"},
            "./channel/title",
            "Lorem Ipsum",
            None,
        ),
        (
            "channel_tag",
            {"tag": "image", "href": "https://example.com/image.jpg"},
            "./channel/image",
            None,
            {"href": "https://example.com/image.jpg"},
        ),
    ],
)
def test_element(
    tmp_path: Path,
    rss_feed: RSSFeed,
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

import xml.etree.ElementTree as ET
from pathlib import Path
import pytest

from feedwriter.rss_feed import RSSFeed


@pytest.fixture
def rss_feed(tmp_path) -> RSSFeed:
    return RSSFeed()


@pytest.fixture
def assert_xml(
    tmp_path: Path,
    rss_feed: RSSFeed,
    xpath: str,
    expected_text: str | None = None,
    expected_attrib: dict[str, str] | None = None,
):
    # write tmp_file
    tmp_file = tmp_path / "feed.xml"
    rss_feed.write(tmp_file)

    # load tmp_file in memory
    tree = ET.parse(tmp_file)
    root = tree.getroot()
    ET.dump(root)

    # TODO: return if assertion fails (element is not found)
    element: ET.Element[str] | None = root.find(xpath)
    assert element is not None, f"Element {xpath} is not found in the XML output."

    if expected_text is not None:
        print("Expected text")
        assert element.text == expected_text, (
            f"Expected {element.tag} to contain {expected_text}, got {element.text}."
        )

    if expected_attrib is not None:
        for attrib, value in expected_attrib.items():
            assert element.get(attrib) == value, (
                f"Expected {attrib} to contain {value}, got {element.get(attrib)}."
            )


@pytest.mark.parametrize(
    ("func_name", "func_kwargs", "xpath", "expected_text", "expected_attrib"),
    [
        (
            "channel_tag",
            {"tag": "title", "content": "Lorem Ipsum"},
            "./channel/title",
            "lorem ipsum",
            None,
        )
    ],
)
def test_element(
    assert_xml,
    rss_feed: RSSFeed,
    func_name: str,
    func_kwargs: dict[str, str],
    xpath: str,
    expected_text: str | None,
    expected_attrib: str | None,
):
    # run function w/ kwargs
    mapped_func = getattr(rss_feed, func_name)
    mapped_func(**func_kwargs)
    rss_feed.write("text.xml")

    # test xml
    assert_xml(rss_feed, xpath, expected_text, expected_attrib)

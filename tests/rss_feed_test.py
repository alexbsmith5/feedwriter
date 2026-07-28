import pytest

from feedwriter import Feed


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
def test_function(
    rss_feed: Feed,
    assert_xml,
    func_name: str,
    func_kwargs: dict[str, str],
    xpath: str,
    expected_text: str | None,
    expected_attrib: dict[str, str] | None,
):
    assert_xml(rss_feed, func_name, func_kwargs, xpath, expected_text, expected_attrib)

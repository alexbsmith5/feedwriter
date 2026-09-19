import pytest

from feedwriter import ArticleFeed


@pytest.mark.parametrize(
    "func_name, func_kwargs, xpath, expected_text, expected_attrib",
    [
        (
            "item",
            {"title": "Lorem Ipsum"},
            "./channel/item/title",
            "Lorem Ipsum",
            None,
        ),
    ],
)
def test_function(
    article_feed: ArticleFeed,
    assert_xml,
    func_name: str,
    func_kwargs: dict[str, str],
    xpath: str,
    expected_text: str | None,
    expected_attrib: dict[str, str] | None,
):
    assert_xml(
        article_feed, func_name, func_kwargs, xpath, expected_text, expected_attrib
    )

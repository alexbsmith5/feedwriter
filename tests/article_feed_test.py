import pytest

from feedwriter import ArticleFeed


@pytest.mark.parametrize(
    "func_name, func_kwargs, xpath, expected_text, expected_attrib",
    [
        # channel tags
        ("title", {"text": "Lorem Ipsum"}, "./channel/title", "Lorem Ipsum", None),
        (  # description w/o cdata
            "description",
            {"text": "Lorem ipsum dolor sit amet."},
            "./channel/description",
            "Lorem ipsum dolor sit amet.",
            None,
        ),
        (  # description w/ cdata
            "description",
            {
                "text": '<a href="example.com">Lorem</a> ipsum dolor sit amet.',
                "cdata": True,
            },
            "./channel/description",
            '<![CDATA[ <a href="example.com">Lorem</a> ipsum dolor sit amet. ]]>',
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

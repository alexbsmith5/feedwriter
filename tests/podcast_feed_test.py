import pytest

@pytest.mark.parametrize(
        "func_name, func_kwargs, xpath, expected_text, expected_attrib",
        [
            # channel tags
            (
                "title",
                {"title": "Lorem Ipsum"},
                "./channel/title",
                "Lorem Ipsum",
                None
            ),
            (
                "description",
                {"description": "Lorem ipsum dolor sit amet."},
                "./channel/description",
                "Lorem ipsum dolor sit amet.",
                None
            ),
            (
                "image",
                {"url": "https://example.com/image.jpg"},
                "./channel/itunes:image",
                None,
                { "href": "https://example.com/image.jpg" }
            ),
            (
                "language",
                {"language": "eng"},
                "./channel/language",
                "eng",
                None
            ),
            (
                "category",
                {"category": "Education"},
                "./channel/itunes:category",
                None,
                { "text": "Education" }
            ),
            ( # category w/ subcategory
                "category",
                {"category": "Fiction", "subcategory": "Drama"},
                "./channel/itunes:category",
                None,
                { "text": "Fiction" }
            ),
            ( # subcategory
                "category",
                {"category": "Fiction", "subcategory": "Drama"},
                "./channel/itunes:category/itunes:category",
                None,
                { "text": "Drama" }
            ),
            (
                "explicit",
                {"explicit": True},
                "./channel/itunes:explicit",
                "true",
                None
            ),
            (
                "author",
                {"author": "Lorem Ipsum"},
                "./channel/itunes:author",
                "Lorem Ipsum",
                None
            ),
            (
                "link",
                {"url": "https://example.com/webpage.html"},
                "./channel/link",
                "https://example.com/webpage.html",
                None
            ),
            (
                "itunes_title",
                {"title": "Lorem Ipsum"},
                "./channel/itunes:title",
                "Lorem Ipsum",
                None
            ),
            (
                "itunes_title",
                {"title": "Lorem Ipsum"},
                "./channel/itunes:title",
                "Lorem Ipsum",
                None
            ),
            (
                "type",
                {"type": "episodic"},
                "./channel/itunes:type",
                "episodic",
                None
            ),
            (
                "feed_url_new",
                {"url": "https://example.com/new_feed.xml"},
                "./channel/itunes:new-feed-url",
                "https://example.com/new_feed.xml",
                None
            ),
            (
                "block",
                { },
                "./channel/itunes:block",
                "Yes",
                None
            ),
            (
                "complete",
                { },
                "./channel/itunes:complete",
                "Yes",
                None
            ),
            (
                "verify",
                { "token": "token" },
                "./channel/podcast:txt",
                "token",
                { "purpose": "applepodcastsverify" }
            ),
            (
                "generator",
                { "url": "https://github.com/alexbsmith5/feedwriter" },
                "./channel/generator",
                "https://github.com/alexbsmith5/feedwriter",
                None
            ),
            (
                "new_post",
                { "title": "Lorem Ipsum" },
                "./channel/item/title",
                "Lorem Ipsum",
                None
            ),
        ]
)

def test_element(base_feed, assert_xml, func_name, func_kwargs, xpath, expected_text, expected_attrib):
    mapped_func = getattr(base_feed, func_name)
    mapped_func(**func_kwargs)

    assert_xml(base_feed, xpath, expected_text=expected_text, expected_attrib=expected_attrib)

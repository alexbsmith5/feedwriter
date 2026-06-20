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
            (
                "new_post",
                { "enclosure": ("https://website.com/post.mp3", 5650880, "audio/mpeg")},
                "./channel/item/enclosure",
                None,
                { "url": "https://website.com/post.mp3", "length": "5650880", "type": "audio/mpeg" }
            ),
            (
                "new_post",
                { "date": "Thu, 11 Jun 2026 10:00:00 +0000" },
                "./channel/item/pubdate",
                "Thu, 11 Jun 2026 10:00:00 +0000",
                None
            ),
            (
                "new_post",
                { "description": "Lorem ipsum dolor sit amet." },
                "./channel/item/description",
                "Lorem ipsum dolor sit amet.",
                None
            ),
            (
                "new_post",
                { "duration": 6536 },
                "./channel/item/itunes:duration",
                "6536",
                None
            ),
            (
                "new_post",
                { "link": "https://example.com/post.html" },
                "./channel/item/link",
                "https://example.com/post.html",
                None
            ),
            (
                "new_post",
                { "image": "https://example.com/post.jpg" },
                "./channel/item/itunes:image",
                None,
                { "href": "https://example.com/post.jpg" }
            ),
            (
                "new_post",
                { "explicit": True },
                "./channel/item/itunes:explicit",
                "true",
                None
            ),
            (
                "new_post",
                { "itunes_title": "Lorem Ipsum" },
                "./channel/item/itunes:title",
                "Lorem Ipsum",
                None
            ),
            (
                "new_post",
                { "episode": 1 },
                "./channel/item/itunes:episode",
                "1",
                None
            ),
            (
                "new_post",
                { "season": 1 },
                "./channel/item/itunes:season",
                "1",
                None
            ),
            (
                "new_post",
                { "type": "full" },
                "./channel/item/itunes:episodeType",
                "full",
                None
            ),
            (
                "new_post",
                { "chapters": ("https://example.com/post-chapters.json", "application/json+chapters") },
                "./channel/item/podcast:chapters",
                None,
                { "url": "https://example.com/post-chapters.json", "type": "application/json+chapters" }
            ),
            (
                "new_post",
                { "transcript": ("https://example.com/post-transcript.vtt", "text/vtt") },
                "./channel/item/podcast:transcript",
                None,
                { "url": "https://example.com/post-transcript.vtt", "type": "text/vtt" }
            ),
            (
                "new_post",
                { "block": True },
                "./channel/item/itunes:block",
                "Yes",
                None
            ),
        ]
)

def test_element(base_feed, assert_xml, func_name, func_kwargs, xpath, expected_text, expected_attrib):
    mapped_func = getattr(base_feed, func_name)
    mapped_func(**func_kwargs)

    assert_xml(base_feed, xpath, expected_text=expected_text, expected_attrib=expected_attrib)

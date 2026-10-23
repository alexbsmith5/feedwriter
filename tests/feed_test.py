from datetime import datetime
from zoneinfo import ZoneInfo

import pytest

from feedwriter import Feed


@pytest.mark.parametrize(
    "func_name, func_kwargs, xpath, expected_text, expected_attrib",
    [
        # channel tags
        ("title", {"text": "Lorem Ipsum"}, "./channel/title", "Lorem Ipsum", None),
        (
            "link",
            {"url": "https://example.com/webpage.html"},
            "./channel/link",
            "https://example.com/webpage.html",
            None,
        ),
        (
            "link",
            {"url": "https://example.com/lorem ipsum.html"},
            "./channel/link",
            "https://example.com/lorem%20ipsum.html",
            None,
        ),
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
        ("language", {"text": "eng"}, "./channel/language", "eng", None),
        (
            "copyright",
            {"text": "© Lorem Ipsum"},
            "./channel/copyright",
            "&#xA9; Lorem Ipsum",
            None,
        ),
        (
            "web_master",
            {"text": "mail@example.com"},
            "./channel/webMaster",
            "mail@example.com",
            None,
        ),
        (  # date w/ string
            "pub_date",
            {"date": "Thu, 11 Jun 2026 10:00:00 +0000"},
            "./channel/pubDate",
            "Thu, 11 Jun 2026 10:00:00 +0000",
            None,
        ),
        (  # date w/ datetime object (no tz)
            "pub_date",
            {"date": datetime(2001, 1, 1, hour=1, minute=1, second=1)},
            "./channel/pubDate",
            "Mon, 01 Jan 2001 01:01:01 +0000",
            None,
        ),
        (  # date w/ datetime object (EST tz)
            "pub_date",
            {"date": datetime(2001, 1, 1, tzinfo=ZoneInfo("America/New_York"))},
            "./channel/pubDate",
            "Mon, 01 Jan 2001 00:00:00 -0500",
            None,
        ),
        # TODO: update tests when new helper function is added for dates
        (  # date w/ string
            "last_build_date",
            {"date": "Thu, 11 Jun 2026 10:00:00 +0000"},
            "./channel/lastBuildDate",
            "Thu, 11 Jun 2026 10:00:00 +0000",
            None,
        ),
        (  # date w/ datetime object (no tz)
            "last_build_date",
            {"date": datetime(2001, 1, 1, hour=1, minute=1, second=1)},
            "./channel/lastBuildDate",
            "Mon, 01 Jan 2001 01:01:01 +0000",
            None,
        ),
        (  # date w/ datetime object (EST tz)
            "last_build_date",
            {"date": datetime(2001, 1, 1, tzinfo=ZoneInfo("America/New_York"))},
            "./channel/lastBuildDate",
            "Mon, 01 Jan 2001 00:00:00 -0500",
            None,
        ),
        (
            "category",
            {"text": "Newspapers"},
            "./channel/category",
            "Newspapers",
            None,
        ),
        (
            "generator",
            {"url": "https://github.com/alexbsmith5/feedwriter"},
            "./channel/generator",
            "https://github.com/alexbsmith5/feedwriter",
            None,
        ),
        (
            "docs",
            {"url": "https://example.com/docs"},
            "./channel/docs",
            "https://example.com/docs",
            None,
        ),
        (
            "ttl",
            {"num": 60},
            "./channel/ttl",
            "60",
            None,
        ),
        (
            "image",
            {
                "url": "https://example.com/image.png",
                "title": "Example Image",
                "link": "https://example.com",
            },
            "./channel/image/url",
            "https://example.com/image.png",
            None,
        ),
        (
            "skip_hours",
            {(0, 1, 2, 3)},
            "./channel/skipHours/hour",
            "(0, 1, 2, 3)",
            None,
        ),
        # TODO: skip_days function
        # (
        #     "skip_days",
        #     {("Monday", "Tuesday")},
        #     "./channel/skipDays/day",
        #     "(Monday, Tuesday)",
        #     None,
        # ),
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

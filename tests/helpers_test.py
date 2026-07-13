import pytest

from feedwriter.helpers import _escape  # pyright: ignore[reportPrivateUsage]


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ("&", "&amp;"),
        ("<", "&lt;"),
        (">", "&gt;"),
        ("'", "&apos;"),
        ('"', "&quot;"),
        ("©", "&#xA9;"),
        ("℗", "&#x2117;"),
        ("™", "&#x2122;"),
    ),
)
def test_escape(input: str, expected: str):
    assert _escape(input) == expected

def test_title(base_feed, assert_xml):
    base_feed.title("Testing Title")
    assert_xml(base_feed, "./channel/title", expected_text="Testing Title")

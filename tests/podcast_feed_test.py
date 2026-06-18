import pytest

@pytest.mark.parametrize(
        "func_name, func_kwargs, xpath, expected_text, expected_attrib",
        [
            (
                "title",
                {"title": "Testing Title"},
                "./channel/title",
                "Testing Title",
                None
            ),
        ]
)

def test_element(base_feed, assert_xml, func_name, func_kwargs, xpath, expected_text, expected_attrib):
    mapped_func = getattr(base_feed, func_name)
    mapped_func(**func_kwargs)

    assert_xml(base_feed, xpath, expected_text=expected_text, expected_attrib=expected_attrib)

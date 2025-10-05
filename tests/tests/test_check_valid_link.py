import pytest
from streamsnatch import check_valid_link

@pytest.mark.parametrize("url,expected", [
    # ✅ Valid YouTube URLs
    ("https://www.youtube.com/watch?v=dQw4w9WgXcQ", True),
    ("http://youtu.be/dQw4w9WgXcQ", True),
    ("www.youtube.com/watch?v=dQw4w9WgXcQ", True),
    ("youtube.com/watch?v=dQw4w9WgXcQ", True),

    # ❌ Invalid YouTube URLs
    ("https://www.youtubee.com/watch?v=dQw4w9WgXcQ", False),
    ("https://example.com/watch?v=dQw4w9WgXcQ", False),
    ("", False),
    ("not a url", False),
])
def test_check_valid_link(url, expected):
    assert check_valid_link(url) == expected

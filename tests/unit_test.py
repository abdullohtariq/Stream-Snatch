# tests/test_main.py
from unittest.mock import patch, MagicMock
from main import check_valid_link, download_yt

def test_download_yt_valid_choice():
    fake_info = {
        "title": "Test Video",
        "formats": [
            {"format_id": "18", "format_note": "360p", "ext": "mp4", "filesize": 1048576, "acodec": "aac", "vcodec": "h264"},
            {"format_id": "22", "format_note": "720p", "ext": "mp4", "filesize": 2097152, "acodec": "aac", "vcodec": "h264"}
        ]
    }

    # Mock YoutubeDL and shutil.which
    with patch("main.YoutubeDL") as mock_ydl, patch("main.shutil.which", return_value=True):
        instance = mock_ydl.return_value.__enter__.return_value
        instance.extract_info.return_value = fake_info
        instance.download.return_value = None  # simulate download

        # Patch input to select first format
        with patch("builtins.input", return_value="1"):
            download_yt("https://youtu.be/dQw4w9WgXcQ")

        # Check if extract_info and download were called
        instance.extract_info.assert_called_once_with("https://youtu.be/dQw4w9WgXcQ", download=False)
        instance.download.assert_called_once_with(["https://youtu.be/dQw4w9WgXcQ"])

# valid URLs
def test_valid_link():

    assert check_valid_link("https://youtu.be/dQw4w9WgXcQ") is True
    assert check_valid_link("http://www.youtube.com/watch?v=dQw4w9WgXcQ") is True
    assert check_valid_link("www.youtube.com/watch?v=dQw4w9WgXcQ") is True

#Invalid Links
def test_invalid_link():
    # invalid URLs
    assert check_valid_link("https://vimeo.com/123456") is False
    assert check_valid_link("https://example.com") is False
    assert check_valid_link("not_a_link") is False

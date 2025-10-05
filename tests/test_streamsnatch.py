import pytest
from unittest.mock import patch, MagicMock
from streamsnatch import download_yt

@patch("streamsnatch.YoutubeDL")
def test_yt_downloader_valid(mock_yt_dlp):
    # Mock YoutubeDL instance and its methods
    mock_instance = MagicMock()
    mock_yt_dlp.return_value.__enter__.return_value = mock_instance

    mock_instance.extract_info.return_value = {
        "title": "Test Video",
        "formats": [
            {"format_id": "18", "acodec": "mp4a.40.2", "vcodec": "avc1.42001E", "format_note": "360p", "ext": "mp4", "filesize": 1048576}
        ]
    }

    with patch("builtins.input", return_value="1"):
        download_yt("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    mock_instance.extract_info.assert_called_once()
    mock_instance.download.assert_called_once()

@patch("streamsnatch.YoutubeDL", side_effect=Exception("Invalid link"))
def test_yt_downloader_invalid(mock_yt_dlp):
    # Since download_yt handles exceptions internally and prints them,
    # we just ensure it doesn't crash or raise.
    download_yt("invalid-link")
    mock_yt_dlp.assert_called_once()

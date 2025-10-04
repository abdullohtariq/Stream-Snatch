
# Stream Snatch 🎬

**Stream Snatch** is a CLI-based YouTube video downloader that allows users to download videos in multiple resolutions, store them locally, and organize metadata. The project is designed with future-proofing in mind, including potential automation for updates and robustness against library changes.

---

## Features

- Download YouTube videos via command-line input.
- List available resolutions and formats before download.
- Handles both audio and video (progressive formats).
- Checks if `ffmpeg` is installed for best-quality downloads.
- Robust error handling and logging.
- Easy-to-extend for future GUI or SaaS versions.
- Designed for CI/CD pipelines and automated testing.

---

## Getting Started

### Requirements

- Python 3.10+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- Optional: [ffmpeg](https://ffmpeg.org/) for merged audio-video formats

### Installation

1. Clone the repository:

```bash
git clone https://github.com/<abdullohtariq>/stream-snatch.git
cd stream-snatch
````

2. (Optional but recommended) Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python stream_snatch.py <youtube_video_url>
```

* Follow the prompts to select video resolution.
* Download will be saved in `Downloads/` folder.
* Metadata and other enhancements will be added in future releases.

---

## Testing

Unit tests are located in the `tests/` folder. Run tests with:

```bash
pytest
```

---

## Project Roadmap

* [x] CLI-based video downloader
* [x] Format selection and metadata display
* [x] Unit tests for core functionality
* [ ] GUI version using PySide6 / PyQt
* [ ] Self-updating pipeline with CI/CD
* [ ] Store metadata, thumbnails, and auto-organize downloads
* [ ] Publish as a packaged executable `.exe`

---

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests. Ensure tests pass and code is documented.

---

## License

This project is licensed under MIT License.

---

## Notes / Future Ideas

* Implement auto-update of yt-dlp for robustness.
* Add self-healing pipelines for outdated libraries.
* Enhance metadata storage: save title, description, thumbnails, and other info in structured format.
* Explore SaaS/GUI implementation for easier access.

```


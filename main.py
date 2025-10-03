# =========================
# Stream Snatch - YouTube Downloader
# Phase 1: CLI → then GUI
# =========================

# Imports (to be installed later)
# from pytube import YouTube
# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
# import sys, os

# -------------------------
# STEP 1 - CLI TOOL
# TODO: Take YouTube URL input from command line
# TODO: Fetch video metadata (title, streams)
# TODO: Let user pick resolution
# TODO: Download video to Downloads folder
# TODO: Show success/failure in terminal
#
# Milestone Commit: "feat: basic CLI YouTube downloader"
# -------------------------

# -------------------------
# STEP 2 - MIGRATE TO GUI
# TODO: Setup basic PyQt window
# TODO: Add input field for YouTube URL
# TODO: Add "Fetch Video" button
# TODO: Show video title + thumbnail
# TODO: Dropdown for resolution selection
# TODO: Add "Download" button + progress bar
#
# Milestone Commit: "feat: initial GUI with URL input"
# -------------------------

# -------------------------
# STEP 3 - BRANDING + POLISH
# TODO: Add logo + custom stylesheet (QSS)
# TODO: Add footer ("VidFetch v1.0")
# TODO: Package app into .exe with PyInstaller
#
# Milestone Commit: "chore: branding + first release build"
# -------------------------


def main():
    yt_link = input("Give Link to download Your video: ")
    download_yt(yt_link)

def download_yt(link):
    ...


if __name__ == "__main__":
    main()

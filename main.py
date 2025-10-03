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


#imports:
from sys import exit, argv
import re
from yt_dlp import YoutubeDL


#main function
def main():
    #exit if there is no ClI Argument
    if len(argv) != 2:
        exit("To Run Paste the link of youtube Video")
    link = argv[1]

    #exit if our regex reject it
    if not check_valid_link(link):
        exit("The Link Is Not Valid....")


    #trying to download except error
    download_yt(link)


#checking the input
def check_valid_link(link):
    pattern = r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+"
    return re.match(pattern, link) is not None


#downloading if the link is valid
def download_yt(link):
    try:
        # Options for yt-dlp
        ydl_opts = {
            "outtmpl": "Downloads/%(title)s.%(ext)s",  # Save in Downloads with video title
            "format": "best",      # Get best quality available
            "quiet": True,  # Suppress most logs
            "no_warnings": True
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=False)   # Fetch metadata without downloading
            title = info.get("title", "Unknown Title")

            select = input(f"Is this the title of yt video you want to download: {title} [y/n] ").strip().lower()
            if select not in ["y", "yes"]:
                exit("❌ Cancelled. Choose another link.")

            print("⬇️ Downloading your video...")
            ydl.download([link])  # Actually download
            print("✅ Download complete!")

    except Exception as e:
        print(f"⚠️ Something went wrong: {e}")



if __name__ == "__main__":
    main()

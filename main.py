# =========================
# Stream Snatch - YouTube Downloader
# Phase 1: CLI → then GUI
# =========================

# Imports (to be installed later)
# from dLP import YouTube ✅
# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
# import sys✅, os

# -------------------------
# STEP 1 - CLI TOOL
# TODO: Take YouTube URL input from command line✅
# TODO: Fetch video metadata (title, streams)✅
# TODO: Let user pick resolution
# TODO: Download video to Downloads folder✅
# TODO: Show success/failure in terminal✅
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
import shutil


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

#class logger to gernate errors
class MyLogger:
    def debug(self, msg):
        pass  # ignore debug
    def warning(self, msg):
        pass  # ignore warnings
    def error(self, msg):
        print(f"⚠️ {msg}")  # only show errors

#downloading if the link is valid

def download_yt(link):
    try:
        # check if ffmpeg exists
        ffmpeg_found = shutil.which("ffmpeg") is not None
        if not ffmpeg_found:
            print("⚠️ ffmpeg not found → Only limited formats may be available.\n")

        # step 1: extract info without download
        with YoutubeDL({"quiet": True, "no_warnings": True}) as ydl:
            info = ydl.extract_info(link, download=False)
            title = info.get("title", "Unknown Title")
            print(f"\n🎬 Title: {title}\n")

            # get formats
            formats = info.get("formats", [])
            display_formats = []

            for f in formats:
                # prefer those with resolution info
                note = f.get("format_note") or f.get("resolution") or "Unknown"
                ext = f.get("ext", "mp4")
                size = f.get("filesize") or f.get("filesize_approx")
                size_str = f"{round(size / 1024 / 1024, 2)} MB" if size else "?"
                # only list formats that have either resolution or audio+video
                if f.get("acodec") != "none" and f.get("vcodec") != "none":
                    display_formats.append((f["format_id"], note, ext, size_str))

            if not display_formats:
                print("⚠️ No valid formats found. (Install ffmpeg for best results)")
                return

            # show choices
            for i, f in enumerate(display_formats, 1):
                print(f"{i}. {f[1]} - {f[2]} - {f[3]}")

            # safe input
            choice = input("\nEnter the number of the resolution you want: ").strip()
            if not choice.isdigit() or not (1 <= int(choice) <= len(display_formats)):
                print("❌ Invalid choice.")
                return
            selected_format_id = display_formats[int(choice) - 1][0]

        # step 2: download with chosen format
        ydl_opts = {
            "outtmpl": "Downloads/%(title)s.%(ext)s",
            "format": selected_format_id,
            "logger": MyLogger(),
            "quiet": False,
            "no_warnings": True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            print("\n⬇️ Downloading...")
            ydl.download([link])
            print("✅ Done!")

    except Exception as e:
        print(f"⚠️ Something went wrong: {e}")





if __name__ == "__main__":
    main()

#!/usr/bin/env python3


# YouTube Videos Downloader Tool
# Made By Ruben Leonardo Sigalingging.
# Created On Thursday, January 5, 2023, At 10:06 PM.
# Using the Python Programming Language Version 3.8.10
# -> Keep Enthusiastic and Don't Give Up


import os
# https://docs.python.org/3/library/os.html
import sys
# https://docs.python.org/3/library/sys.html
if "Windows" in os.uname() or sys.platform=="win32":
	os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
	os.system("python get-pip.py")
	os.system("pip -V")
	os.system("pip --version")
	os.system("cls")
	os.system("pip install pytube")
	os.system("pip install pyfiglet")
	os.system("cls")
elif "macOS" in os.uname() or sys.platform=="darwin":
	os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
	os.system("python3 get-pip.py")
	os.system("clear")
	# https://macosx-faq.com/how-to-clear-terminal-screen/
	os.system("pip install pyfiglet")
	os.system("pip install pytube")
	os.system("clear")
elif "Linux" in os.uname() or sys.platform=="linux":
	os.system("sudo apt-get update && sudo apt-get upgrade")
	os.system("sudo apt-get install python3-pip")
	os.system("pip3 --version")
	os.system("pip install pytube")
	os.system("pip install pyfiglet")
	os.system("sudo apt-get update && sudo apt-get upgrade")
	os.system("chmod 777 YouTubeVideosDownloaderTool.py")
	os.system("clear")
import pytube
import pyfiglet


def YouTube_Videos_Downloader_Tool(code_by="Ruben Leonardo Sigalingging"):
	Style=pyfiglet.Figlet(font="cybermedium")
	print(Style.renderText("pytube"))
	print("[!] Code By Ruben Leonardo Sigalingging")
	print("[!] Created On Thursday, January 5, 2023, At 10:06 PM.")
	print("[!] Functions: To Download YouTube Videos\n")


	# Get Input From User
	Input_Video_URL=str(input("[!] Search Or Paste Link Here: "))
	Download_My_YouTube_Videos=pytube.YouTube(Input_Video_URL)
	print(f"[!] Results About My YouTube Videos Downloaded: {Download_My_YouTube_Videos}")
	print(f"[!] Title Of The Video: {Download_My_YouTube_Videos.title}")
	print(f"[!] Thumbnail URL From The YouTube Video: {Download_My_YouTube_Videos.thumbnail_url}")
	print(f"[!] Viewers Total From The YouTube Video: {Download_My_YouTube_Videos.views}")


	Download_My_YouTube_Videos=Download_My_YouTube_Videos.streams.get_highest_resolution()
	Download_My_YouTube_Videos.download()
YouTube_Videos_Downloader_Tool()
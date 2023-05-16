from pytube import YouTube
from pytube.exceptions import VideoUnavailable, AgeRestrictedError, VideoRegionBlocked, LiveStreamError, RecordingUnavailable, MembersOnly, VideoPrivate
from requests.exceptions import HTTPError, ConnectTimeout, InvalidURL
from urllib3.exceptions import ProtocolError
from http.client import RemoteDisconnected
from pytube.cli import on_progress
import os, shutil
from tkinter import messagebox as mb


def deleteData():
    folder = './download'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def download(videolist):
    vedio_dir = './download'
    print("Start Program...Please wait...")
    for video_url in videolist:
        print(f"Downloading: {video_url}")
        try:
            YouTube(video_url, on_progress_callback = on_progress, use_oauth = True).streams.get_highest_resolution().download(vedio_dir)
        except (VideoUnavailable, HTTPError, ConnectionError,RemoteDisconnected, ConnectTimeout, InvalidURL, ProtocolError, AgeRestrictedError, VideoRegionBlocked, LiveStreamError, RecordingUnavailable, MembersOnly, VideoPrivate, Exception):
            try:
                YouTube(video_url).streams.get_highest_resolution().download(vedio_dir)
            except (VideoUnavailable, HTTPError, ConnectionError,RemoteDisconnected, ConnectTimeout, InvalidURL, ProtocolError, AgeRestrictedError, VideoRegionBlocked, LiveStreamError, RecordingUnavailable, MembersOnly, VideoPrivate, Exception):
                print(video_url)

def main():
    videolist = []
    with open('./target-video.txt', 'r') as file:
        content = file.readlines()
        videolist = [f.strip()  for f in content]
    download(videolist)
    mb.showwarning(title = "HI", message = "Download complete!")


if __name__ == '__main__':
    main()


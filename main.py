from pytube import YouTube
import shutil
# https://www.youtube.com/watch?v=dQw4w9WgXcQ

url = YouTube(input("Video url: "))
path = input("Path: ")
print(f"Downloading {url.title}...")

video = url.streams.get_highest_resolution().download()
print("Done!")

shutil.move(video, path)

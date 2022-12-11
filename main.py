from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
print(video.title)

video.streams.get_highest_resolution().download()

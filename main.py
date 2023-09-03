from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=vWBpzveKvGA"

yt = YouTube(video_url)


stream = yt.streams.get_highest_resolution()

download_folder = "./"

stream.download(output_path=download_folder)

print("Video downloaded successfully!")


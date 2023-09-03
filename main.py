from pytube import YouTube

video_url = input("Enter the URL of the YouTube video: ")

try:
    yt = YouTube(video_url)

    print("Available stream options:")
    for i, stream in enumerate(yt.streams):
        print(f"{i + 1}. {stream}")

    stream_index = int(input("Select a stream to download (enter the index): ")) - 1
    selected_stream = yt.streams[stream_index]

    download_folder = input("Enter the directory where you want to save the video: ")

    selected_stream.download(output_path=download_folder)

    print("Video downloaded successfully!")

except Exception as e:
    print(f"An error occurred: {str(e)}")

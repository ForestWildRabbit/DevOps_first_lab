from pytube import YouTube, exceptions
import os
import sys


def main():
    running = True
    application_path = ""

    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    while running:
        link = input("Enter YOUTUBE link with a video: ")
        try:
            youtube = YouTube(link)
            title = youtube.title.replace("/", "")

            output_path = os.path.join(application_path, "audiofiles")
            if not os.path.exists(output_path):
                os.mkdir(output_path)

            youtube.streams.get_audio_only().download(output_path=output_path, filename=f"{title}.mp3")
            print(f"Successfully loaded to {output_path}/{title}.mp3")
        except exceptions.RegexMatchError:
            print("You entered an invalid url.")

    return 0


if __name__ == '__main__':
    main()

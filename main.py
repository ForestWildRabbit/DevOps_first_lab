from pytube import YouTube, exceptions
import os
import sys


def main():
    length_of_parameters = len(sys.argv)
    if length_of_parameters == 1:
        print("Enter a link to youtube video after this script name")
        return 1

    link = sys.argv[1]

    application_path = ""

    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    try:
        youtube = YouTube(link)
        title = youtube.title.replace("/", "")

        output_path = os.path.join(application_path, "audiofiles")
        if not os.path.exists(output_path):
            os.mkdir(output_path)

        youtube.streams.get_audio_only().download(output_path=output_path, filename=f"{title}.mp3")
        print(f"Successfully loaded to {output_path}/{title}.mp3")
    except exceptions.RegexMatchError:
        print(f"You entered an invalid url \'{link}\'.")

    return 0


if __name__ == '__main__':
    main()

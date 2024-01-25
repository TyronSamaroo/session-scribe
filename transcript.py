
import argparse
from utils import meeting_minutes, save_as_docx

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transcribe an audio file and generate meeting minutes.')
    parser.add_argument('--audio', type=str, default='default_audio.mp3', help='The path to the audio file to transcribe.')
    parser.add_argument('--output', type=str, default='meeting_minutes.docx', help='The filename to save the meeting minutes as.')

    args = parser.parse_args()

    minutes = meeting_minutes(args.audio)
    print(minutes)
    save_as_docx(minutes, args.output)
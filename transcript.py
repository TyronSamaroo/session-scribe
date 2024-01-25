
import argparse
from datetime import datetime
from utils import meeting_minutes, save_as_docx, transcribe_audio

def transcribe_audio_if_confirmed(audio_file):
    print("Please note that transcribing the audio will incur charges to your OpenAI account.")
    confirm_transcription = input("Are you sure you want to transcribe the audio? (yes/no): ")
    if confirm_transcription.lower() == 'yes':
        return transcribe_audio(audio_file)
    else:
        print("Transcription cancelled.")
        return None

def generate_minutes_if_confirmed(transcription):
    if transcription is None:
        return None

    print("Please note that generating meeting minutes with GPT-4 will incur charges to your OpenAI account.")
    confirm_minutes = input("Are you sure you want to generate meeting minutes? (yes/no): ")
    if confirm_minutes.lower() == 'yes':
        return meeting_minutes(transcription)
    else:
        print("Meeting minutes generation cancelled.")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transcribe an audio file and generate meeting minutes.')
    parser.add_argument('--audio', type=str, default='default_audio.mp3', help='The path to the audio file to transcribe.')
    parser.add_argument('--output', type=str, default='meeting_minutes.docx', help='The filename to save the meeting minutes as.')
    parser.add_argument('--custom', action='store_true', help='Whether to use a custom filename or not.')

    args = parser.parse_args()

    transcription = transcribe_audio_if_confirmed(args.audio)
    minutes = generate_minutes_if_confirmed(transcription)

    if args.custom and minutes is not None:
        print("Using custom filename.")
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        args.output = f"meeting_minutes_{current_time}.docx"
        print(f"Output filename: {args.output}")

    if isinstance(minutes, dict):
        save_as_docx(minutes, args.output)
    else:
        print("No document was saved because meeting minutes were not generated.")
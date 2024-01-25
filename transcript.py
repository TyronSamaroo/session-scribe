
import argparse
from datetime import datetime
from utils import SaveAsDocxInput, TranscriptionInput, generate_minutes_if_confirmed, meeting_minutes, save_as_docx, transcribe_audio, transcribe_audio_if_confirmed



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transcribe an audio file and generate meeting minutes.')
    parser.add_argument('--audio', type=str, default='default_audio.mp3', help='The path to the audio file to transcribe.')
    parser.add_argument('--output', type=str, default='meeting_minutes.docx', help='The filename to save the meeting minutes as.')
    parser.add_argument('--custom', action='store_true', help='Whether to use a custom filename or not.')

    args = parser.parse_args()

    transcription_input = TranscriptionInput(audio_file_path=args.audio)
    transcription = transcribe_audio_if_confirmed(transcription_input)

    if transcription is not None:
        minutes = generate_minutes_if_confirmed(transcription)

        if args.custom and minutes is not None:
            print("Using custom filename.")
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            args.output = f"meeting_minutes_{current_time}.docx"
            print(f"Output filename: {args.output}")

        if minutes is not None:
            save_as_docx_input = SaveAsDocxInput(minutes=minutes, filename=args.output)
            save_as_docx(save_as_docx_input)
        else:
            print("No document was saved because meeting minutes were not generated.")
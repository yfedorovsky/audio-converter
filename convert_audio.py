from pydub import AudioSegment
import os

def convert_audio(input_file, output_file):
    try:
        audio = AudioSegment.from_file(input_file)
        audio.export(output_file, format="mp3")
        print(f"Converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Oops, something went wrong: {e}")

# Example use
if __name__ == "__main__":
    convert_audio("sample.wav", "sample.mp3")
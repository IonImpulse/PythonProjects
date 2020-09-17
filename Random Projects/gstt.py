import argparse
import podcast_transcriber

# parse the CLI arguments
parser = argparse.ArgumentParser(prog="python podcast_transcriber.py")
parser.add_argument("input_file", help="input audio file")
args = parser.parse_args()

podcast_transcriber.transcribe(args.input_file)
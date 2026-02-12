#!/usr/bin/env python3
"""
Batch transcribe audio files from a folder to text files.

Usage:
    python batch_transcribe.py <input_folder> [output_folder] [--model MODEL] [--language LANG]

Examples:
    python batch_transcribe.py ./recordings
    python batch_transcribe.py ./recordings ./transcripts
    python batch_transcribe.py ./recordings ./transcripts --model medium --language en

If output_folder is omitted, text files are written next to the originals.
"""
import argparse
import os
import sys
from pathlib import Path

from transcribe import transcribe

AUDIO_EXTENSIONS = {".webm", ".wav", ".mp3", ".m4a", ".ogg", ".mp4", ".flac", ".aac", ".wma"}


def batch_transcribe(input_dir: str, output_dir: str | None, model: str, language: str) -> None:
    input_path = Path(input_dir)
    if not input_path.is_dir():
        print(f"Error: '{input_dir}' is not a directory", file=sys.stderr)
        sys.exit(1)

    if output_dir:
        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)
    else:
        out_path = None

    audio_files = sorted(
        f for f in input_path.iterdir()
        if f.is_file() and f.suffix.lower() in AUDIO_EXTENSIONS
    )

    if not audio_files:
        print(f"No audio files found in '{input_dir}'")
        print(f"Supported extensions: {', '.join(sorted(AUDIO_EXTENSIONS))}")
        return

    print(f"Found {len(audio_files)} audio file(s) in '{input_dir}'")
    print(f"Model: {model} | Language: {language}")
    print("-" * 60)

    succeeded = 0
    failed = 0

    for i, audio_file in enumerate(audio_files, 1):
        txt_name = audio_file.stem + ".txt"
        if out_path:
            txt_file = out_path / txt_name
        else:
            txt_file = audio_file.with_suffix(".txt")

        print(f"[{i}/{len(audio_files)}] {audio_file.name} -> {txt_file.name} ... ", end="", flush=True)

        try:
            text = transcribe(str(audio_file), model, language)
            if text:
                txt_file.write_text(text, encoding="utf-8")
                print(f"OK ({len(text)} chars)")
                succeeded += 1
            else:
                txt_file.write_text("", encoding="utf-8")
                print("OK (empty — no speech detected)")
                succeeded += 1
        except Exception as e:
            print(f"FAILED: {e}")
            failed += 1

    print("-" * 60)
    print(f"Done: {succeeded} succeeded, {failed} failed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch transcribe audio files to text.")
    parser.add_argument("input_folder", help="Folder containing audio files")
    parser.add_argument("output_folder", nargs="?", default=None,
                        help="Output folder for .txt files (default: same as input)")
    parser.add_argument("--model", default="small", help="Whisper model size (default: small)")
    parser.add_argument("--language", default="en", help="Language code (default: en)")
    args = parser.parse_args()

    batch_transcribe(args.input_folder, args.output_folder, args.model, args.language)

#!/usr/bin/env python3
"""
Transcribe audio using faster-whisper.
Usage: python transcribe.py <audio_file> [model_size] [language]
Outputs transcribed text to stdout.
"""
import sys
import os
from faster_whisper import WhisperModel

# Filter out common Whisper hallucinations on short/silent audio
HALLUCINATION_FILTERS = {
    "you", "you.", "thank you.", "thanks for watching.",
    "thanks for watching!", "subscribe", "bye.", "bye",
    "", " ", "...", "♪", "♪♪", "♪♪♪",
}

def transcribe(audio_path: str, model_size: str = "small", language: str = "en") -> str:
    """Transcribe audio file to text."""
    # Check if file exists and has content
    if not os.path.exists(audio_path):
        print(f"Error: File not found: {audio_path}", file=sys.stderr)
        return ""

    file_size = os.path.getsize(audio_path)
    if file_size < 1000:  # Less than 1KB is likely too short
        print(f"Warning: Audio file very small ({file_size} bytes)", file=sys.stderr)
        return ""

    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    # Use language hint and VAD filter to reduce hallucinations
    segments, info = model.transcribe(
        audio_path,
        beam_size=5,
        language=language,
        vad_filter=True,  # Filter out non-speech
        vad_parameters=dict(
            min_silence_duration_ms=500,  # Minimum silence to split
            speech_pad_ms=200,  # Padding around speech
        ),
    )

    # Collect segments
    texts = []
    for segment in segments:
        text = segment.text.strip()
        # Filter out known hallucinations
        if text.lower() not in HALLUCINATION_FILTERS:
            texts.append(text)

    result = " ".join(texts)

    # Final check for hallucination
    if result.lower().strip() in HALLUCINATION_FILTERS:
        return ""

    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <audio_file> [model_size] [language]", file=sys.stderr)
        sys.exit(1)

    audio_file = sys.argv[1]
    model_size = sys.argv[2] if len(sys.argv) > 2 else "small"
    language = sys.argv[3] if len(sys.argv) > 3 else "en"

    text = transcribe(audio_file, model_size, language)
    print(text)

"""
VoiceLex - Voice-Based Dictionary using Automatic Speech Recognition.

A command-line ASR dictionary tool using OpenAI Whisper.
It transcribes a spoken word/audio file and looks up its meaning
using the Free Dictionary API.
"""

import argparse
import json
import sys
from pathlib import Path

import requests
import whisper

SUPPORTED_AUDIO = {
    ".wav", ".mp3", ".m4a", ".flac", ".ogg", ".webm", ".mp4"
}


def validate_audio_path(audio_path):
    """Validate that the input audio file exists and has a supported type."""
    path = Path(audio_path)

    if not path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    if path.suffix.lower() not in SUPPORTED_AUDIO:
        supported = ", ".join(sorted(SUPPORTED_AUDIO))
        raise ValueError(
            f"Unsupported audio type: {path.suffix}. Supported: {supported}"
        )

    return path


def transcribe_audio(audio_path, model_name="base", language=None):
    """Transcribe an audio file using Whisper."""
    path = validate_audio_path(audio_path)
    model = whisper.load_model(model_name)

    options = {}
    if language:
        options["language"] = language

    result = model.transcribe(str(path), **options)
    return result


def lookup_word(word):
    """Get dictionary information for a word."""
    word = word.strip().lower()

    if not word:
        raise ValueError("Word cannot be empty.")

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url, timeout=10)

    if response.status_code == 404:
        return None

    response.raise_for_status()
    return response.json()


def format_dictionary_result(word, data):
    """Format dictionary API data for terminal output."""
    if not data:
        return f"No dictionary entry found for: {word}"

    entry = data[0]
    phonetic = entry.get("phonetic", "Not available")
    lines = [
        f"Word: {word}",
        f"Pronunciation: {phonetic}",
        ""
    ]

    count = 0
    for meaning in entry.get("meanings", []):
        part_of_speech = meaning.get("partOfSpeech", "unknown")

        for item in meaning.get("definitions", [])[:2]:
            count += 1
            definition = item.get("definition", "Definition unavailable.")
            example = item.get("example", "No example available.")

            lines.append(f"{count}. {part_of_speech}: {definition}")
            lines.append(f"   Example: {example}")
            lines.append("")

            if count >= 4:
                break

        if count >= 4:
            break

    return "\n".join(lines).rstrip()


def save_result(output_path, result):
    """Save a result to a text or JSON file."""
    path = Path(output_path)

    if path.suffix.lower() == ".json":
        path.write_text(
            json.dumps(result, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
    else:
        path.write_text(str(result), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(
        description="VoiceLex: Whisper ASR + dictionary lookup."
    )
    parser.add_argument("audio", help="Input audio file")
    parser.add_argument(
        "--model",
        choices=["tiny", "base", "small", "medium", "large"],
        default="base",
        help="Whisper model size (default: base)"
    )
    parser.add_argument(
        "--language",
        default=None,
        help="Language code, for example en"
    )
    parser.add_argument(
        "--no-dictionary",
        action="store_true",
        help="Only transcribe the audio; skip dictionary lookup"
    )
    parser.add_argument(
        "-o", "--output",
        help="Save result to a .txt or .json file"
    )

    args = parser.parse_args()

    try:
        result = transcribe_audio(
            args.audio,
            model_name=args.model,
            language=args.language
        )

        transcript = result.get("text", "").strip()
        if not transcript:
            raise ValueError("No speech was detected.")

        print("Recognized speech:")
        print(transcript)

        output_data = {
            "recognized_text": transcript,
            "dictionary": None
        }

        if not args.no_dictionary:
            # VoiceLex is designed for a single spoken word.
            words = transcript.split()

            if len(words) != 1:
                print(
                    "\nVoiceLex expects one English word for dictionary lookup."
                )
            else:
                try:
                    dictionary_data = lookup_word(words[0])
                    output_data["dictionary"] = dictionary_data

                    print("\nDictionary Result:")
                    print(format_dictionary_result(words[0], dictionary_data))
                except requests.RequestException as exc:
                    print(f"\nDictionary lookup failed: {exc}")

        if args.output:
            save_result(args.output, output_data)
            print(f"\nSaved result to: {args.output}")

    except (FileNotFoundError, ValueError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

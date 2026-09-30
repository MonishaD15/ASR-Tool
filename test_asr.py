from pathlib import Path
import pytest

from asr import format_dictionary_result, lookup_word, validate_audio_path


def test_validate_audio_path_accepts_supported_type(tmp_path):
    audio = tmp_path / "sample.wav"
    audio.write_bytes(b"test")
    assert validate_audio_path(audio) == audio


def test_validate_audio_path_rejects_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        validate_audio_path(tmp_path / "missing.wav")


def test_validate_audio_path_rejects_unsupported_type(tmp_path):
    image = tmp_path / "sample.jpg"
    image.write_bytes(b"test")

    with pytest.raises(ValueError):
        validate_audio_path(image)


def test_format_dictionary_result():
    data = [{
        "phonetic": "/ˈælgərɪðəm/",
        "meanings": [{
            "partOfSpeech": "noun",
            "definitions": [{
                "definition": "A procedure for solving a problem.",
                "example": "The algorithm sorts the data."
            }]
        }]
    }]

    result = format_dictionary_result("algorithm", data)

    assert "algorithm" in result.lower()
    assert "A procedure for solving a problem." in result
    assert "The algorithm sorts the data." in result


def test_format_missing_dictionary_result():
    result = format_dictionary_result("unknownword", None)
    assert "No dictionary entry found" in result

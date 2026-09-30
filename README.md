# VoiceLex – Voice-Based Dictionary using Automatic Speech Recognition

## Team Members

| Name | Register Number |
|---|---|
| [YOUR NAME] | [YOUR REGISTER NUMBER] |
| [TEAM MEMBER 2] | [REGISTER NUMBER] |
| [TEAM MEMBER 3] | [REGISTER NUMBER] |

## Tool Purpose

**VoiceLex** is an Automatic Speech Recognition (ASR) tool that converts spoken English from an audio file into text using OpenAI Whisper. For a single recognized English word, it then retrieves the word's pronunciation, definitions, and examples from the Free Dictionary API.

The project is designed as a command-line tool and can run locally after the Whisper model has been downloaded.

## Features

- Transcribes `.wav`, `.mp3`, `.m4a`, `.flac`, `.ogg`, `.webm`, and `.mp4` audio files
- Uses OpenAI Whisper for speech recognition
- Supports Whisper model sizes: `tiny`, `base`, `small`, `medium`, and `large`
- Optional language selection
- Recognizes a spoken word and retrieves its dictionary meaning
- Displays pronunciation and example sentences
- Saves results as TXT or JSON
- Includes input validation and error handling
- Includes unit tests using pytest
- Runs locally; after the Whisper model is downloaded, transcription can be performed offline

## Tools and Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.9+ | Programming language |
| OpenAI Whisper | Automatic Speech Recognition model |
| PyTorch | Deep learning backend used by Whisper |
| FFmpeg | Audio decoding |
| Requests | Dictionary API communication |
| Free Dictionary API | Word meanings, pronunciation and examples |
| pytest | Unit testing |
| Git and GitHub | Version control and project hosting |

## Project Structure

```text
VoiceLex-ASR/
├── asr.py              # ASR tool and dictionary functions
├── test_asr.py         # Unit tests
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignored files
├── history.txt         # Sample history
└── README.md           # Project documentation
```

## Setup Instructions

### 1. Install Python

Install Python 3.9 or newer.

Check the installation:

```bash
python --version
```

### 2. Install FFmpeg

Whisper uses FFmpeg to decode audio files.

**Windows:**

```bash
winget install ffmpeg
```

or:

```bash
choco install ffmpeg
```

**macOS:**

```bash
brew install ffmpeg
```

Check that FFmpeg works:

```bash
ffmpeg -version
```

### 3. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd VoiceLex-ASR
```

### 4. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## How to Run

Place an audio file such as `sample.wav` in the project folder.

### Basic ASR + dictionary lookup

```bash
python asr.py sample.wav
```

### Select a smaller Whisper model

```bash
python asr.py sample.wav --model tiny
```

### Use English explicitly

```bash
python asr.py sample.wav --model base --language en
```

### ASR transcription only

```bash
python asr.py sample.wav --no-dictionary
```

### Save the result as text

```bash
python asr.py sample.wav -o result.txt
```

### Save the result as JSON

```bash
python asr.py sample.wav -o result.json
```

## First Run

The first time a Whisper model is selected, Whisper downloads the model. This requires an internet connection and can take some time depending on the model size.

After the model is downloaded, Whisper can perform transcription locally.

## Testing

Run the unit tests with:

```bash
pytest -v
```

The tests cover:

- Audio file validation
- Unsupported file handling
- Missing file handling
- Dictionary result formatting
- Missing dictionary result handling

The unit tests do not require an actual microphone.

## Example Run

```text
$ python asr.py sample.wav

Recognized speech:
algorithm

Dictionary Result:
Word: algorithm
Pronunciation: /ˈælgərɪðəm/

1. noun: A procedure or set of rules used to solve a problem.
   Example: The algorithm sorts the data.
```

## How It Works

```text
Audio File
    ↓
FFmpeg
    ↓
Whisper ASR Model
    ↓
Recognized Speech
    ↓
Single Word Validation
    ↓
Free Dictionary API
    ↓
Pronunciation + Definition + Example
    ↓
Terminal / TXT / JSON
```

## ASR Process

1. The user provides an audio file.
2. The application validates the file path and extension.
3. Whisper loads the selected speech recognition model.
4. The audio is decoded using FFmpeg.
5. Whisper converts the speech into text.
6. If one English word is recognized, VoiceLex sends it to the Dictionary API.
7. The application displays the word's pronunciation, definitions, and examples.
8. The result can optionally be saved as TXT or JSON.

## Supported Audio Formats

- WAV
- MP3
- M4A
- FLAC
- OGG
- WEBM
- MP4

## Project Testing Plan

| Test Case | Input | Expected Result |
|---|---|---|
| TC01 | Clear audio saying `algorithm` | Word is transcribed and dictionary result is displayed |
| TC02 | Clear audio saying `computer` | Word is transcribed and definition is displayed |
| TC03 | Unsupported `.jpg` file | Validation error is displayed |
| TC04 | Missing audio file | File-not-found error is displayed |
| TC05 | Unknown dictionary word | No dictionary entry message is displayed |
| TC06 | `--no-dictionary` | Only ASR transcription is displayed |

## Limitations

- Dictionary lookup requires an internet connection.
- Whisper model download is required the first time a model is used.
- Larger Whisper models require more storage and processing time.
- Dictionary lookup is designed for a single English word.
- Recognition accuracy depends on audio quality, pronunciation, background noise, and selected model.

## Future Enhancements

- Add microphone/live speech input.
- Add text-to-speech pronunciation.
- Add support for multiple dictionary languages.
- Add a graphical user interface.
- Add search history management.
- Add offline dictionary data.
- Add automatic language detection for dictionary lookup.

## GitHub Upload

After testing the project:

```bash
git init
git add .
git commit -m "Initial VoiceLex ASR project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your GitHub repository URL.

## Student Details

**Name:** [YOUR NAME]

**Register Number:** [YOUR REGISTER NUMBER]

**Class:** [YOUR CLASS]

**Department:** [YOUR DEPARTMENT]

**Team Members:** [ADD TEAM MEMBERS]

**Institution:** [YOUR INSTITUTION]

## Conclusion

VoiceLex demonstrates a practical application of Automatic Speech Recognition by combining Whisper-based speech transcription with dictionary lookup. The project provides a simple command-line workflow, automated testing, API integration, and GitHub-ready documentation.

# Jarvis Laptop Controller

A lightweight voice-controlled Windows laptop controller built with Python.

## V1 Features

- Microphone voice input
- Speech-to-text using Google Speech Recognition
- Open Google Chrome
- Open VS Code
- Open File Explorer
- Open This PC
- Open Downloads
- Jarvis greeting and wake commands
- Voice commands to stop Jarvis
- Automatic retry when speech is not understood

## Requirements

- Windows
- Python 3.14+
- Working microphone
- Internet connection for Google Speech Recognition

## Setup

1. Create a virtual environment: python -m venv venv
2. Activate it: .\\venv\\Scripts\\Activate.ps1
3. Install dependencies: python -m pip install -r requirements.txt
4. Run: python main.py

## Example Commands

Open Chrome
Open VS Code
Open File Explorer
Open This PC
Open Downloads
Hello Jarvis
Stop Jarvis

## Notes

This project uses sounddevice for microphone recording instead of PyAudio.

## Roadmap

- V2: Window control
- V3: Mouse gestures
- V4: Smart window layout
- V5: Custom commands
- V6: AI/Jarvis mode

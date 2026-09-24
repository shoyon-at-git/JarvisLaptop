import sounddevice as sd
import numpy as np
import speech_recognition as sr
import subprocess
import os


SAMPLE_RATE = 16000
DURATION = 5


def listen():
    print("\n🎤 Jarvis is listening...")
    print("Speak something...")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    audio_int16 = np.int16(audio.flatten() * 32767)

    audio_data = sr.AudioData(
        audio_int16.tobytes(),
        SAMPLE_RATE,
        2
    )

    recognizer = sr.Recognizer()

    try:
        text = recognizer.recognize_google(
            audio_data,
            language="en-US"
        )

        text = text.lower().strip()

        print("🗣️ You said:", text)

        return text

    except sr.UnknownValueError:
        return ""

    except sr.RequestError as e:
        print("❌ Speech recognition error:", e)
        return ""


def execute_command(command):

    if "open chrome" in command:
        print("🌐 Opening Chrome...")

        subprocess.Popen(
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        )

        return

    if (
        "open vs code" in command
        or "open vscode" in command
        or "open visual studio code" in command
    ):
        print("💻 Opening VS Code...")

        subprocess.Popen(
            "code",
            shell=True
        )

        return

    if "open downloads" in command:
        print("📁 Opening Downloads...")

        downloads = os.path.join(
            os.path.expanduser("~"),
            "Downloads"
        )

        os.startfile(downloads)

        return

    if (
        "open file explorer" in command
        or "open explorer" in command
        or command == "file explorer"
    ):
        print("📂 Opening File Explorer...")

        subprocess.Popen(
            "explorer.exe"
        )

        return

    if (
        "open this pc" in command
        or "open my computer" in command
    ):
        print("🖥️ Opening This PC...")

        subprocess.Popen(
            "explorer.exe shell:MyComputerFolder",
            shell=True
        )

        return

    if command in [
        "hello",
        "hello jarvis",
        "jarvis",
        "hey jarvis",
        "hi jarvis"
    ]:
        print("🤖 Yes, I'm listening.")

        return

    print("❓ Command not recognized:", command)


def main():

    print("================================")
    print("🤖 JARVIS LAPTOP CONTROLLER")
    print("================================")

    while True:

        command = listen()

        if command == "":
            continue

        if command in [
            "exit",
            "exit jarvis",
            "stop jarvis",
            "stop service",
            "exit service",
            "quit",
            "quit jarvis",
            "bye jarvis"
        ]:
            print("👋 Jarvis shutting down...")
            break

        execute_command(command)


if __name__ == "__main__":
    main()

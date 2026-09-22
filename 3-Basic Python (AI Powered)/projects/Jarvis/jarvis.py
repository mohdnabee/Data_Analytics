"""
jarvis.py
Build Your Own Jarvis with Python — Complete Voice Assistant

Wake word:      "jarvis"
Libraries used: pyttsx3, SpeechRecognition, PyAudio, openai, datetime,
                webbrowser, urllib.parse, os
"""

import datetime
import os
import urllib.parse
import webbrowser

import pyttsx3
import speech_recognition as sr

# Optional AI fallback (only used if OPENAI_API_KEY is set)
try:
    import openai
except ImportError:
    openai = None


# ---------------------------------------------------------------------
# B. TEXT-TO-SPEECH
# ---------------------------------------------------------------------
engine = pyttsx3.init()
engine.setProperty("rate", 175)


def speak(text):
    """Print the text and speak it out loud."""
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()


# ---------------------------------------------------------------------
# C. VOICE RECOGNITION
# ---------------------------------------------------------------------
recognizer = sr.Recognizer()


def take_command():
    """Listen through the microphone and convert speech to text."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"You: {query}")
        return query.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable right now.")
        return ""


# ---------------------------------------------------------------------
# F. AI FALLBACK
# ---------------------------------------------------------------------
def ask_ai(prompt):
    """Send unmatched queries to OpenAI when an API key is configured."""
    api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key or openai is None:
        return "AI mode is not configured. Set OPENAI_API_KEY to enable it."

    try:
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception:
        return "Sorry, I could not reach the AI service right now."


# ---------------------------------------------------------------------
# E. COMMAND HANDLER
# ---------------------------------------------------------------------
def handle_command(query):
    """Match the recognized text to an action, or fall back to AI."""

    if "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "date" in query:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    elif "open youtube" in query:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in query:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open facebook" in query:
        speak("Opening Facebook.")
        webbrowser.open("https://www.facebook.com")

    elif "open linkedin" in query:
        speak("Opening LinkedIn.")
        webbrowser.open("https://www.linkedin.com")

    elif "play" in query:
        song = query.replace("play", "").strip()
        speak(f"Playing {song} on YouTube.")
        search_query = urllib.parse.quote(song)
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")

    elif "google search" in query:
        term = query.replace("google search", "").strip()
        speak(f"Searching Google for {term}.")
        search_query = urllib.parse.quote(term)
        webbrowser.open(f"https://www.google.com/search?q={search_query}")

    elif "search youtube for" in query:
        term = query.replace("search youtube for", "").strip()
        speak(f"Searching YouTube for {term}.")
        search_query = urllib.parse.quote(term)
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")

    elif "hello" in query:
        speak("Hello! How can I help you today?")

    elif any(word in query for word in ["exit", "quit", "stop"]):
        speak("Goodbye!")
        raise SystemExit

    else:
        answer = ask_ai(query)
        speak(answer)


# ---------------------------------------------------------------------
# D. WAKE WORD + MAIN LOOP
# ---------------------------------------------------------------------
def main():
    speak("Initializing Jarvis.")
    speak("Say Jarvis to wake me up.")

    while True:
        query = take_command()

        if "jarvis" in query:
            speak("Ya. I am listening.")
            command = take_command()
            if command:
                try:
                    handle_command(command)
                except SystemExit:
                    break


if __name__ == "__main__":
    main()

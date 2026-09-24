import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import os
from openai import OpenAI

# Register Brave browser
brave_path = r"C:\Users\farha\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()  # init once, globally
    engine.setProperty('rate', 130)      # speech speed (default ~200)
    engine.setProperty('volume', 1.0)    # 0.0 to 1.0
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
    )

    completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant in brief."},
        {"role": "user", "content": command}
    ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    c = c.lower()
    print(f"Processing command: {c}")  # debug
    if "open google" in c:
        speak("Opening Google")
        webbrowser.get('brave').open("https://google.com")

    elif "open youtube" in c:
        speak("Opening youtube")
        webbrowser.get('brave').open("https://youtube.com")

    elif "open chess" in c:
        speak("Opening chess")
        webbrowser.get('brave').open("https://www.chess.com/home")

    elif "open erp" in c:
        speak("Opening your ERP")
        webbrowser.open("http://globalinstitutes.in/")

    elif "open github" in c:
        speak("Opening github")
        webbrowser.get('brave').open("https://github.com/")

    elif "open linkedin" in c:
        speak("Opening linkedin")
        webbrowser.open("https://www.linkedin.com/in/farhanalam0605")

    elif c.startswith("play"):
        song = c.split(" ")[1]
        speak(f"Playing {song}")
        link = musiclibrary.music[song]
        webbrowser.get('brave').open(link)

    else:
        # Let OpenAI handles the request
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
            word = recognizer.recognize_google(audio)

            if "jarvis" in word.lower():
                speak("Yes Sir")
                with sr.Microphone() as source:
                    print("Jarvis Active.....")
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
                try:
                    command = recognizer.recognize_google(audio)
                    processCommand(command)
                except sr.UnknownValueError:
                    print("Could not understand the command")
                except sr.RequestError as e:
                    print(f"API error: {e}")

        except sr.WaitTimeoutError:
            print("Listening timed out, no speech detected")
        except sr.UnknownValueError:
            print("Could not understand wake word")
        except Exception as e:
            print("Error: {0}".format(e))
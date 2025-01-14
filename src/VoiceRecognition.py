import threading

import speech_recognition as sr

from src.PlaySound import playSound

recognizer = sr.Recognizer()

def voiceRecognition():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Listening continuously... Press Ctrl+C to stop.")
        while True:
            try:
                audio = recognizer.listen(source)
                threading.Thread(target=processAudio, args=(recognizer, audio)).start()
            except KeyboardInterrupt:
                print("Stopped listening.")
                break

def processAudio(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        playSound("GameSelectLive", text)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
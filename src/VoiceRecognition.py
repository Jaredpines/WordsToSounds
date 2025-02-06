import ast
import json
import pyaudio
from vosk import Model, KaldiRecognizer
from src.PlaySound import playSound

previous = ""
def voiceRecognition():
    global previous
    model = Model("../Model/vosk-model-small-en-us-0.15")  # Download from https://alphacephei.com/vosk/models
    recognizer = KaldiRecognizer(model, 16000)

    # Set up microphone stream using pyaudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=8000)

    print("Voice Assistant is listening...")

    # Function to handle commands

    while True:
        data = stream.read(4000)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result = ast.literal_eval(result)
            playSound("GameSelectLive", result["text"])



#past voicerecognition
# import threading
#
# import speech_recognition as sr
#
# from src.PlaySound import playSound
#
# recognizer = sr.Recognizer()
#
# def voiceRecognition():
#     with sr.Microphone(2) as source:
#         print("Adjusting for ambient noise... Please wait.")
#         recognizer.adjust_for_ambient_noise(source, duration=1)
#
#         print("Listening continuously... Press Ctrl+C to stop.")
#         while True:
#             try:
#                 audio = recognizer.listen(source)
#                 threading.Thread(target=processAudio, args=(recognizer, audio)).start()
#             except KeyboardInterrupt:
#                 print("Stopped listening.")
#                 break
#
# def processAudio(recognizer, audio):
#     try:
#         text = recognizer.recognize_google(audio)
#         print(f"You said: {text}")
#         playSound("GameSelectLive", text)
#     except sr.UnknownValueError:
#         pass
#     except sr.RequestError as e:
#         print(f"Could not request results from Google Speech Recognition service; {e}")
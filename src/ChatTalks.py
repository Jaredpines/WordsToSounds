import pyttsx3
from ctypes import windll
import tkinter as tk
from PIL import Image, ImageTk
# import torch
# import sounddevice as sd
# from TTS.api import TTS
# from TTS.tts.configs.xtts_config import XttsConfig
# from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs
# from TTS.config.shared_configs import BaseDatasetConfig
# torch.serialization.add_safe_globals([XttsConfig, XttsAudioConfig, BaseDatasetConfig, XttsArgs])
# device = "cuda" if torch.cuda.is_available() else "cpu"
# model_path = "tts_models/multilingual/multi-dataset/xtts_v2"
#model_path = "tts_models/de/thorsten/tacotron2-DDC"
# tts = TTS(model_path).to(device)
# def Load():
#     global tts
#     tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

images = []
startX = 500
startY = 1115
mode = "idle"
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0

def chatTalks(message):
    global mode
    engine = pyttsx3.init()


    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.8)
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0")

    engine.say(message)

    engine.runAndWait()


    # sentence = message
    #
    # speaker = "../Model/peter/peter.wav"  # Replace with the actual speaker name or ID
    #
    # audio = tts.tts(text=sentence, speaker_wav=speaker, language="es")
    #
    # # Play the audio
    # sample_rate = 22050  # Check model documentation for correct rate
    # sd.play(audio, samplerate=sample_rate)
    # sd.wait()  # Wait until audio has finished playing
    #
    # print("Speech played.")



def chat(root):
    global images, mode, startX, startY
    windowWidth = 300
    windowHeight = 400
    canvas = tk.Canvas(root, width=windowWidth, height=windowHeight, bd=0, highlightthickness=0, bg="#010203")

    colorkey = 0x00030201
    hwnd = canvas.winfo_id()
    wnd_exstyle = windll.user32.GetWindowLongA(hwnd, -20)  # GWL_EXSTYLE
    new_exstyle = wnd_exstyle | 0x00080000  # WS_EX_LAYERED
    windll.user32.SetWindowLongA(hwnd, -20, new_exstyle)  # GWL_EXSTYLE
    windll.user32.SetLayeredWindowAttributes(hwnd, colorkey, 255, 0x00000001)

    # Load GIF
    image = Image.open("../Images/chat.gif")

    desiredWidth = 250
    desiredHeight = 250
    frames = []

    try:
        while True:
            resizedFrame = image.copy().resize((desiredWidth, desiredHeight), Image.Resampling.NEAREST)
            frames.append(ImageTk.PhotoImage(resizedFrame.convert("RGBA"), master=root))
            image.seek(len(frames))
    except EOFError:
        pass

    # Save frames to prevent garbage collection
    global currentFrames
    currentFrames = frames

    # Display first frame by default
    frameId = canvas.create_image(0, 0, image=currentFrames[0], anchor='nw')

    def updateFrame(index):
        if not canvas.winfo_exists():
            return  # Stop if the window is closed

        if mode == "idle":
            canvas.itemconfig(frameId, image=currentFrames[0])  # Keep first frame
        else:
            canvas.itemconfig(frameId, image=currentFrames[index])
            next_index = (index + 1) % len(currentFrames)
            root.after(100, updateFrame, next_index)

    # Ensure first frame stays visible
    canvas.itemconfig(frameId, image=currentFrames[0])
    canvas.place(x=startX, y=startY)

    # Start updating only if mode is not idle
    if mode != "idle":
        updateFrame(0)
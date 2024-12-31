import asyncio
import os
import re
import time
from datetime import datetime
import vlc
import threading
from PIL import Image, ImageTk
import tkinter as tk
from googletrans import Translator
import random
import cv2

POLLINGINTERVAL = 5
translator = Translator()
excludedNames = {"Tio", "Gio"}
p = vlc.MediaPlayer("../Sounds/metalpipe.mp3")
today = datetime.today()
christmasTimeStart = datetime(today.year, 12, 18)
christmasTimeEnd = datetime(today.year + 1, 1, 1)
content = 1


def translateToEnglish(text):
    placeholderMap = {}
    words = text.split()
    for i, word in enumerate(words):
        cleanWord = word.strip("!,.?")  # Remove punctuation for matching
        if cleanWord.capitalize() in excludedNames:
            placeholder = f"__name_{i}__"
            placeholderMap[placeholder] = word
            words[i] = placeholder

    textWithPlaceholders = " ".join(words)
    detectedLang = translator.detect(textWithPlaceholders).lang

    if detectedLang != "en":
        translatedText = translator.translate(textWithPlaceholders, dest="en").text
    else:
        translatedText = textWithPlaceholders

    for placeholder, originalName in placeholderMap.items():
        print(placeholder)
        print(originalName)
        translatedText = translatedText.replace(placeholder, originalName)

    return translatedText


def playSound(message):
    global p, content
    # message = translateToEnglish(message)
    message = message.lower()
    print(message)
    if "steal" in message or "steel" in message:
        p = vlc.MediaPlayer("../Sounds/metalpipe.mp3")
        p.play()

    if "vine boom" in message or "vineboom" in message:
        p = vlc.MediaPlayer("../Sounds/vineboom.mp3")
        p.play()

    if "get out" in message or re.search(rf"\bget ou\b", message) or "getout" in message or re.search(rf"\bgetou\b",
                                                                                                      message):
        p = vlc.MediaPlayer("../Sounds/getout.mp3")
        p.play()

    if "butter dog" in message or "butterdog" in message or "🧈🐶" in message:
        p = vlc.MediaPlayer("../Sounds/butterdog.mp3")
        p.play()

    if "gamese39omg" in message or "omg" in message:
        p = vlc.MediaPlayer("../Sounds/omg.mp3")
        p.play()

    if "pikmin" in message:
        rand = random.randint(0, 4)
        if rand == 0:
            p = vlc.MediaPlayer("../Sounds/pikmin.mp3")
        elif rand == 1:
            p = vlc.MediaPlayer("../Sounds/pikmindeath.mp3")
        elif rand == 2:
            p = vlc.MediaPlayer("../Sounds/pikminfall.mp3")
        elif rand == 3:
            p = vlc.MediaPlayer("../Sounds/pikminpluck.mp3")
        elif rand == 4:
            p = vlc.MediaPlayer("../Sounds/pikminthrow.mp3")
        p.play()
        multipleTriggers("../Images/pikminy.gif", duration=2)

    if "gamese39yippee" in message or "yippee" in message:
        p = vlc.MediaPlayer("../Sounds/yippee.mp3")
        p.play()

    if "door" in message:
        p = vlc.MediaPlayer("../Sounds/door.mp3")
        p.play()

    if "gamese39mariodisapproves" in message:
        p = vlc.MediaPlayer("../Sounds/mario.mp3")
        p.play()

    if "gamese39rollinggiant" in message or "gamese39rg" in message:
        p = vlc.MediaPlayer("../Sounds/rolling.mp3")
        p.play()

    if "gambling" in message:
        rand = random.randint(1, 10)
        if 0 < rand < 10:
            multipleTriggers("../Videos/gamblinglose.mp4")
        else:
            multipleTriggers("../Videos/gamblingwin.mp4")

    if "fnaf" in message or "five night's at freddy's" in message or "five nights at freddys" in message \
            or "freddy" in message or "animatronic" in message or "foxy" in message or "bonnie" in message \
            or "chica" in message or "baby" in message or "ennard" in message or "springtrap" in message \
            or "afton" in message or "purple guy" in message or "fazbear" in message or "mangle" in message \
            or "puppet" in message or "jj" in message or "rwqfsfasxc" in message or "shadow bb" in message \
            or "xor" in message or "springlock" in message or "fredbear" in message or "phantom bb" in message \
            or "nightmare" in message or "plushtrap" in message or "balloon boy" in message or "nightmarionne" in message \
            or "freddles" in message or "dreadbear" in message or "ballora" in message or "bidybab" in message \
            or "minireena" in message or "bon-bon" in message or "lolbit" in message or "electrobab" in message \
            or "bonnet" in message or "music man" in message or "lefty" in message or "rockstar foxy's parrot" in message \
            or "carnie" in message or "happy frog" in message or "mr. hippo" in message or "pigpatch" in message \
            or "nedd bear" in message or "orville elephant" in message or "mystic hippo" in message \
            or "monty" in message or "montgomery gator" in message or "roxxy" in message or "roxanne wolf" in message \
            or "endo" in message or "the mimic" in message or "tangle" in message or "helpy" in message:
        rand = random.randint(1, 8)
        if rand == 1:
            multipleTriggers("../Videos/fnaf1.mp4")
        elif rand == 2:
            multipleTriggers("../Videos/fnaf2.mp4")
        elif rand == 3:
            multipleTriggers("../Videos/fnaf3.mp4", duration=8)
        elif rand == 4:
            multipleTriggers("../Videos/fnaf4.mp4")
        elif rand == 5:
            multipleTriggers("../Videos/fnaf5.mp4")
        elif rand == 6:
            multipleTriggers("../Videos/fnaf6.mp4")
        elif rand == 7:
            multipleTriggers("../Videos/fnafs.mp4")
        elif rand == 8:
            multipleTriggers("../Videos/fnafj.mp4")

    if "one piece" in message or "onepiece" in message:
        p = vlc.MediaPlayer("../Sounds/onepiece.mp3")
        p.play()
        multipleTriggers("../Images/onepiece.gif", duration=12)

    if "sorry" in message or "sowwy" in message or "gamese39sowwy" in message:
        p = vlc.MediaPlayer("../Sounds/sad.mp3")
        p.play()

    if "pog" in message or "poggers" in message or "gamese39gslpog" in message:
        p = vlc.MediaPlayer("../Sounds/pog.mp3")
        p.play()

    if re.search(rf"\bcar\b",
                 message) or "gamese39happycar" in message or "gamese39car" in message or "gamese39shinycar" in message:
        p = vlc.MediaPlayer("../Sounds/car.mp3")
        p.play()

    if "cool" in message or "gamese39goodjoke" in message or "garnular" in message or "gamese39shinygoodjoke" in message:
        p = vlc.MediaPlayer("../Sounds/garnular.mp3")
        p.play()

    if "bad" in message or "gamese39badjoke" in message:
        p = vlc.MediaPlayer("../Sounds/bad.mp3")
        p.play()

    if "bored" in message or "gamese39imbored" in message:
        p = vlc.MediaPlayer("../Sounds/bored.mp3")
        p.play()

    if re.search(rf"\bgsl\b", message) or "gamese39livegslreaction" in message:
        p = vlc.MediaPlayer("../Sounds/erm.mp3")
        p.play()

    if "gamese39scarygsl" in message:
        p = vlc.MediaPlayer("../Sounds/scary.mp3")
        p.play()

    if "gamese39disapprove" in message:
        p = vlc.MediaPlayer("../Sounds/boowomp.mp3")
        p.play()

    if "gamese39thescung" in message:
        p = vlc.MediaPlayer("../Sounds/hellnaw.mp3")
        p.play()

    if "bruh" in message:
        p = vlc.MediaPlayer("../Sounds/bruh.mp3")
        p.play()

    if "gamese39disgust" in message:
        p = vlc.MediaPlayer("../Sounds/shutdown.mp3")
        p.play()

    if "gamese39dance" in message:
        p = vlc.MediaPlayer("../Sounds/dance.mp3")
        p.play()

    if re.search(rf"\bgamese39grin\b", message):
        p = vlc.MediaPlayer("../Sounds/happy.mp3")
        p.play()

    if "die" in message or "death" in message or "dying" in message:
        p = vlc.MediaPlayer("../Sounds/lego.mp3")
        p.play()

    if "hi gio" in message or "hi past gio" in message or "hi future gio" in message:
        p = vlc.MediaPlayer("../Sounds/hello.mp3")
        p.play()

    if "hi tio" in message or "hi past tio" in message or "hi future tio" in message:
        p = vlc.MediaPlayer("../Sounds/hello2.mp3")
        p.play()

    if "bye tio" in message:
        p = vlc.MediaPlayer("../Sounds/seeya.mp3")
        # multipleTriggers("../Images/moist.png", duration=2)

    if "bye gio" in message:
        p = vlc.MediaPlayer("../Sounds/byeosu.mp3")
        p.play()

    if christmasTimeStart <= today <= christmasTimeEnd:
        if "christmas" in message:
            multipleTriggers("../Videos/christmas.mp4")

    if "freeze" in message:
        multipleTriggers("../Videos/freeze.mp4")

    if "soccer" in message:
        multipleTriggers("../Videos/soccer.mp4", duration=12)

    if "jeff" in message:
        multipleTriggers("../Videos/jeff.mp4")

    if "content" in message and content == 1:
        content -= 1

        p = vlc.MediaPlayer("../Sounds/silent.mp3")
        p.play()
    elif "content" in message and content != 1:
        p.stop()


root = None
images = []
videos = []


def setupTkinter():
    """Initialize the Tkinter root window."""
    global root
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.attributes('-fullscreen', True)
    root.attributes('-transparentcolor', 'purple')
    root.configure(bg='purple')


def flashImage(imagePath, duration=3):
    """Flash an image on the screen."""
    global root, images
    if root is None:
        raise RuntimeError("Tkinter root is not initialized. Call setupTkinter first.")

    # Load the image
    image = Image.open(imagePath)
    imageWidth, imageHeight = image.size
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    # Random position on screen
    xPos = random.randint(0, screenWidth - imageWidth)
    yPos = random.randint(0, screenHeight - imageHeight)

    # Create a label for the image
    label = tk.Label(root, bg='purple')
    label.place(x=xPos, y=yPos)

    if ".gif" in imagePath:
        # Load frames for GIF
        frames = []
        try:
            while True:
                frames.append(ImageTk.PhotoImage(image.copy(), master=root))
                image.seek(len(frames))
        except EOFError:
            pass

        def updateFrame(index):
            if label.winfo_exists():
                try:
                    label.config(image=frames[index])
                    label.image = frames[index]  # Keep a reference to avoid garbage collection
                    if index + 1 < len(frames):
                        root.after(100, updateFrame, index + 1)
                    else:
                        root.after(100, updateFrame, 0)
                except tk.TclError:
                    pass

        updateFrame(0)
    else:
        # Single frame image
        img = ImageTk.PhotoImage(image, master=root)
        label.config(image=img)
        label.image = img  # Keep a reference

    # Add the label to the active list and schedule its removal
    images.append(label)
    root.after(int(duration * 1000), lambda: removeImage(label))


def flashVideo(videoPath, duration=None):
    """Flash an MP4 video with sound on the screen, playing for its entire length."""
    global root, videos
    if root is None:
        raise RuntimeError("Tkinter root is not initialized. Call setupTkinter first.")

    # Create a new VLC instance for playback
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(videoPath)
    player.set_media(media)

    cap = cv2.VideoCapture(videoPath)
    videoWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    videoHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()

    # Scale video dimensions to fit within maxWidth and maxHeight
    scale = min(640 / videoWidth, 360 / videoHeight)  # default max size 640x360
    scaledWidth = int(videoWidth * scale)
    scaledHeight = int(videoHeight * scale)

    # Random position on the screen
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    xPos = random.randint(0, screenWidth - scaledWidth)
    yPos = random.randint(0, screenHeight - scaledHeight)

    # Create a canvas for the video
    canvas = tk.Canvas(root, width=scaledWidth, height=scaledHeight, bg='purple', highlightthickness=0)
    canvas.place(x=xPos, y=yPos)

    # Set the VLC video output to the canvas
    hwnd = canvas.winfo_id()  # Windows handle ID
    player.set_hwnd(hwnd)

    # Start playback
    player.play()

    time.sleep(1)

    # Get the video duration in seconds
    videoDuration = player.get_length() / 1000  # VLC gives duration in milliseconds

    # If the video duration is not provided, use the video’s actual length
    if not duration:
        duration = videoDuration

    # Schedule the video stop based on the video's actual length
    def stopVideo():
        player.stop()
        canvas.destroy()
        videos.remove(canvas)

    root.after(int(duration * 940), stopVideo)

    videos.append(canvas)


def removeImage(label):
    """Remove an image from the screen."""
    global images
    if label in images and label.winfo_exists():
        label.destroy()
        images.remove(label)


def runTkinter():
    """Run the Tkinter event loop in an async-compatible way."""
    global root
    setupTkinter()
    root.mainloop()


def multipleTriggers(mediaPath, duration=None):
    if mediaPath.endswith(".mp4"):
        threading.Thread(target=flashVideo, args=(mediaPath, duration), daemon=True).start()
    else:
        threading.Thread(target=flashImage, args=(mediaPath, duration), daemon=True).start()

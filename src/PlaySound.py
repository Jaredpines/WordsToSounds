import asyncio
import json
import os
import re
import time
from datetime import datetime
import vlc
import threading
from PIL import Image, ImageTk
import tkinter as tk
# from googletrans import Translator
import random
import cv2
from ctypes import windll

POLLINGINTERVAL = 5
# translator = Translator()
excludedNames = {"Tio", "Gio"}
today = datetime.today()
christmasTimeStart = datetime(today.year, 12, 18)
christmasTimeEnd = datetime(today.year + 1, 1, 1)
jan = datetime(today.year, 1, 1)
content = 1
ss = 1
win = False
groan = 0
jeff = 0
maxPoints = 50


# def translateToEnglish(text):
#     placeholderMap = {}
#     words = text.split()
#     for i, word in enumerate(words):
#         cleanWord = word.strip("!,.?")  # Remove punctuation for matching
#         if cleanWord.capitalize() in excludedNames:
#             placeholder = f"__name_{i}__"
#             placeholderMap[placeholder] = word
#             words[i] = placeholder
#
#     textWithPlaceholders = " ".join(words)
#     detectedLang = translator.detect(textWithPlaceholders).lang
#
#     if detectedLang != "en":
#         translatedText = translator.translate(textWithPlaceholders, dest="en").text
#     else:
#         translatedText = textWithPlaceholders
#
#     for placeholder, originalName in placeholderMap.items():
#         print(placeholder)
#         print(originalName)
#         translatedText = translatedText.replace(placeholder, originalName)
#
#     return translatedText


def playSound(author, message):
    today = datetime.today()
    p = None
    global players, content, ss, win, groan, videos, jeff, maxPoints, stockPrices
    # message = translateToEnglish(message)
    message = message.lower()
    print(message)

    if jeff > 0 and len(videos) <= 1:
        jeff = 0


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
        multipleTriggers("../Videos/butter.mp4")

    if "gamese39omg" in message or "omg" in message:
        p = vlc.MediaPlayer("../Sounds/omg.mp3")
        p.play()

    if "pikmin" in message:
        rand = random.randint(0, 4)
        if rand == 0:
            p = vlc.MediaPlayer("../Sounds/pikmin.mp3")
            pikmin()
        elif rand == 1:
            p = vlc.MediaPlayer("../Sounds/pikmindeath.mp3")
            multipleTriggers("../Images/pikminy.gif", duration=2)
        elif rand == 2:
            p = vlc.MediaPlayer("../Sounds/pikminfall.mp3")
            multipleTriggers("../Images/pikminy.gif", duration=2)
        elif rand == 3:
            p = vlc.MediaPlayer("../Sounds/pikminpluck.mp3")
            pikmin()
        elif rand == 4:
            p = vlc.MediaPlayer("../Sounds/pikminthrow.mp3")
            multipleTriggers("../Images/pikminy.gif", duration=2)
        p.play()

    if "gamese39yippee" in message or "yippee" in message:
        count = message.count("yippee") + message.count("gamese39yippee")
        rand = random.randint(0, 1)
        if rand == 0:
            for _ in range(count):
                p = vlc.MediaPlayer("../Sounds/yippee.mp3")
                p.play()
        else:
            multipleTriggers("../Videos/yippee.mp4")

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
            win = False
        else:
            multipleTriggers("../Videos/gamblingwin.mp4")
            win = True

        inputOutputFilePath = "../Leaderboard/saves.txt"
        try:
            with open(inputOutputFilePath, 'r+', encoding='utf-8') as inoutfile:
                lines = inoutfile.readlines()  # Read all lines into a list

                author_found = False
                for i, line in enumerate(lines):
                    if author in line and win==True:
                        author_found = True
                        # Extract the current win count from the line
                        current_wins = int(line.split(":")[1].split()[0])  # Get the current win count as an integer
                        # Increment the wins by 1
                        lines[i] = f"{author}: {current_wins + 1} wins\n"  # Update the line with new win count
                        break  # Exit the loop once the author is found
                    elif author in line and win==False:
                        author_found = True
                        current_wins = int(line.split(":")[1].split()[0])
                        lines[i] = f"{author}: {current_wins} wins\n"
                if not author_found and win == True:
                    # If the author is not found, add a new line with 1 win
                    lines.append(f"{author}: 1 win\n")
                elif not author_found and win == False:
                    lines.append(f"{author}: 0 wins\n")

                # Go back to the beginning of the file and overwrite the content
                inoutfile.seek(0)
                inoutfile.writelines(lines)  # Write the modified content back to the file
                inoutfile.truncate()  # Ensure the file is truncated to the correct size
                win = False

        except FileNotFoundError:
            print(f"File not found: {inputOutputFilePath}")
        except Exception as e:
            print(f"An error occurred: {e}")
        leaderboard()
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
        p.play()
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
        count = message.count("soccer")
        for _ in range(count):
            multipleTriggers("../Videos/soccer.mp4", duration=12)

    if "jeff" in message and jeff == 0:
        multipleTriggers("../Videos/jeff.mp4")
        jeff += 1

    if "content" in message and content == 1:
        content -= 1

        p = vlc.MediaPlayer("../Sounds/silent.mp3")
        p.play()
    elif "content" in message and content != 1:
        p.stop()

    if "subway surfers" in message and ss == 1:
        ss -= 1
        multipleTriggers("../Videos/subway.mp4")

    if "before" in message:
        multipleTriggers("../Videos/squid.mp4")

    if "grown tube" in message or "growntube" in message or "groan tube" in message or "groantube" in message or "aaaaaeeeeeuuuuu" in message or "uuuuueeeeeaaaaa" in message:
        groan = random.randint(0, 1)
        if groan == 0:
            p = vlc.MediaPlayer("../Sounds/groanUp.mp3")
            p.play()
            increasePrice(stockPrices, maxPoints)
        else:
            p = vlc.MediaPlayer("../Sounds/groanDown.mp3")
            p.play()
            decreasePrice(stockPrices, maxPoints)

    if "jerma" in message:
        multipleTriggers("../Videos/jerma.mp4")

    if "glorp" in message:
        multipleTriggers("../Videos/glorp.mp4")

    if "huh" in message:
        multipleTriggers("../Videos/huh.mp4")

    if "donate" in message or "donation" in message or "donating" in message or "give me your money" in message:
        count = message.count("donate") + message.count("donation") + message.count("donating") + message.count("give me your money")
        for _ in range(count):
            multipleTriggers("../Videos/give.mp4")

    if "i'm dead" in message:
        multipleTriggers("../Videos/imdead.mp4")

    if "flashbang" in message or "flash bang" in message:
        count = message.count("flashbang") + message.count("flash bang")
        for _ in range(count):
            multipleTriggers("../Videos/thinkfast.mp4")

    if "happy new year" in message:
        multipleTriggers("../Videos/jeff.mp4")
        multipleTriggers("../Videos/soccer.mp4", duration=12)
        multipleTriggers("../Videos/freeze.mp4")
        multipleTriggers("../Videos/christmas.mp4")
        multipleTriggers("../Videos/gamblinglose.mp4")
        multipleTriggers("../Videos/gamblingwin.mp4")
        multipleTriggers("../Videos/fnaf1.mp4")
        multipleTriggers("../Videos/fnaf2.mp4")
        multipleTriggers("../Videos/fnaf3.mp4")
        multipleTriggers("../Videos/fnaf4.mp4")
        multipleTriggers("../Videos/fnaf5.mp4")
        multipleTriggers("../Videos/fnaf6.mp4")
        multipleTriggers("../Videos/fnafs.mp4")
        multipleTriggers("../Videos/fnafj.mp4")

    if "some of this on your that" in message:
        multipleTriggers("../Videos/rett.mp4")

    if "peanut butter and jelly the long way" in message:
        multipleTriggers("../Videos/peanutbutter.mp4")

    if "fish" in message:
        rand = random.randint(1, 8)
        if rand < 8:
            multipleTriggers("../Videos/fish.mp4")
        else:
            multipleTriggers("../Videos/fish2.mp4")

    if "what the dog doing" in message:
        multipleTriggers("../Videos/what.mp4")

    if "salami lid" in message:
        multipleTriggers("../Videos/lid.mp4")


    if "bird up" in message:
        multipleTriggers("../Videos/bird.mp4")

    if "boom" in message:
        multipleTriggers("../Videos/boom.mp4")

    if "yellow" in message:
        count = message.count("yellow")
        for _ in range(count):
            multipleTriggers("../Videos/yellow.mp4")

    if "our table" in message:
        multipleTriggers("../Videos/table.mp4")

    if "meow" in message:
        multipleTriggers("../Videos/meow.mp4")

    if "water" in message:
        multipleTriggers("../Videos/water.mp4")

    if "mr. beast" in message or "mr beast" in message or "mrbeast" in message:
        multipleTriggers("../Videos/beast.mp4")

    if "kill all" in message or (len(videos) > 5 and "yellow" not in message):
        for image in images:
            image.destroy()
        for video in videos:
            video.destroy()
        for player in players:
            player.stop()
        ss = 1
        content = 1

    if p != None:
        players.append(p)



root = None
images = []
videos = []
players = []


def setupTkinter():
    global root
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.attributes('-fullscreen', True)
    root.attributes('-transparentcolor', 'purple')
    root.configure(bg='purple')
    root.after(1, leaderboard)
    root.after(1, groanTubeEconomy)


def flashImage(imagePath, duration=3, flip=False):
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
    if flip == False:
        label.place(x=xPos, y=yPos)
    else:
        label.place(x=root.winfo_screenwidth() - imageWidth, y=0)

    if ".gif" in imagePath and flip == False:
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
    elif ".gif" in imagePath and flip == True:
        img = ImageTk.PhotoImage(image, master=root)
        label.config(image=img)
        label.image = img
    else:
        # Single frame image
        img = ImageTk.PhotoImage(image, master=root)
        label.config(image=img)
        label.image = img  # Keep a reference

    # Add the label to the active list and schedule its removal
    images.append(label)
    if flip == False:
        root.after(int(duration * 1000), lambda: removeImage(label))


def flashVideo(videoPath, duration=None):
    """Flash an MP4 video with sound on the screen, playing for its entire length."""
    global root, videos, players
    if root is None:
        raise RuntimeError("Tkinter root is not initialized. Call setupTkinter first.")

    # Create a new VLC instance for playback
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(videoPath)
    player.set_media(media)
    players.append(player)
    player.audio_set_volume(100)
    player.audio_set_mute(False)
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
    if "subway" in videoPath:
        xPos = 0
        yPos = 0
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


def pikmin():
    global root, images
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    windowWidth = 150
    windowHeight = 185

    # Create a canvas for each Pikmin
    canvas = tk.Canvas(root, width=windowWidth, height=windowHeight, bd=0, highlightthickness=0, bg="#010203")
    colorkey = 0x00030201
    hwnd = canvas.winfo_id()
    wnd_exstyle = windll.user32.GetWindowLongA(hwnd, -20)  # GWL_EXSTYLE
    new_exstyle = wnd_exstyle | 0x00080000  # WS_EX_LAYERED
    windll.user32.SetWindowLongA(hwnd, -20, new_exstyle)  # GWL_EXSTYLE
    windll.user32.SetLayeredWindowAttributes(hwnd, colorkey, 255, 0x00000001)
    canvas.place(x=screenWidth - windowWidth, y=screenHeight - windowHeight)

    # Open the GIF
    rand = random.randint(0, 2)
    if rand == 0:
        image = Image.open("../Images/pikminwalk.gif")
    elif rand == 1:
        image = Image.open("../Images/pikminwalkb.gif")
    elif rand == 2:
        image = Image.open("../Images/pikminwalky.gif")

    # Set the desired size for the image
    desiredWidth = 150
    desiredHeight = 200

    frames = []
    flippedFrames = []
    try:
        while True:
            # Resize and store original frames
            resizedFrame = image.copy().resize((desiredWidth, desiredHeight))
            frames.append(ImageTk.PhotoImage(resizedFrame, master=root))

            # Create flipped frames
            flippedFrame = resizedFrame.transpose(Image.FLIP_LEFT_RIGHT)
            flippedFrames.append(ImageTk.PhotoImage(flippedFrame, master=root))

            image.seek(len(frames))
    except EOFError:
        pass

    currentFrames = frames  # Start with original frames

    frameId = canvas.create_image(0, 0, image=frames[0], anchor='nw')

    def updateFrame(index):
        if canvas.winfo_exists():
            try:
                canvas.itemconfig(frameId, image=currentFrames[index])
                if index + 1 < len(currentFrames):
                    root.after(100, updateFrame, index + 1)
                else:
                    root.after(100, updateFrame, 0)
            except tk.TclError:
                pass

    updateFrame(0)
    images.append(canvas)

    dx = 5
    direction = -1
    startX = screenWidth - windowWidth

    def move():
        nonlocal startX, direction, currentFrames
        if canvas.winfo_exists():
            # Update position
            startX += dx * direction
            canvas.place(x=startX, y=screenHeight - windowHeight)

            # Reverse direction and flip frames at screen edges
            if startX <= 0:
                direction = 1
                currentFrames = flippedFrames
            elif startX >= (screenWidth - desiredWidth):
                direction = -1
                currentFrames = frames

            # Schedule next move
            root.after(50, move)

    move()

canvass = []
def leaderboard():
    global root
    windowWidth = 250
    windowHeight = 285
    xPos = 0
    yPos = 0
    canvas = tk.Canvas(root, width=windowWidth, height=windowHeight, background="#010203", bd=0, highlightthickness=0)
    canvass.append(canvas)
    colorkey = 0x00030201
    hwnd = canvas.winfo_id()
    wnd_exstyle = windll.user32.GetWindowLongA(hwnd, -20)  # GWL_EXSTYLE
    new_exstyle = wnd_exstyle | 0x00080000  # WS_EX_LAYERED
    windll.user32.SetWindowLongA(hwnd, -20, new_exstyle)  # GWL_EXSTYLE
    windll.user32.SetLayeredWindowAttributes(hwnd, colorkey, 255, 0x00000001)
    text = canvas.create_text(0, 0, text="Gambling Leaderboard", font=('Helvetica', 20), fill="Black", anchor="center")
    if len(canvass) > 1:
        canvass.pop(0).delete("all")
    bbox = canvas.bbox(text)  # Returns (x1, y1, x2, y2)
    textWidth = bbox[2] - bbox[0]
    textHeight = bbox[3] - bbox[1]
    canvas.config(width=textWidth, height=textHeight)
    canvas.coords(text, textWidth / 2, textHeight / 2)
    inputOutputFilePath = "../Leaderboard/saves.txt"
    try:
        with open(inputOutputFilePath, 'r', encoding='utf-8') as inoutfile:
            lineCount = 2
            for line in inoutfile:
                addLineOfText(canvas, line,lineCount)
                lineCount += 1
    except FileNotFoundError:
        print(f"File not found: {inputOutputFilePath}")
    except Exception as e:
        print(f"An error occurred: {e}")

    canvas.place(x=xPos, y=yPos)



def addLineOfText(canvas, lineText, lineCount):
    textItem = canvas.create_text(0, 0, text=lineText.strip(), font=('Helvetica', 16), fill="Black", anchor="w")

    # Get bounding box of the new text line
    bbox = canvas.bbox(textItem)
    textHeight = bbox[3] - bbox[1]

    # Resize the canvas height to fit all the text lines
    canvas.config(height=(textHeight * lineCount + 20))  # Add a little padding

    # Place the text at a vertical position based on the lineCount
    canvas.coords(textItem, 10, textHeight * lineCount)  # 10px padding from the left

def drawGraph(canvas, stockPrices, graphWidth, graphHeight, margin, maxPoints, lineColor):
    """Draws the stock market graph."""
    canvas.delete("all")

    # Draw axes
    canvas.create_line(margin, margin, margin, graphHeight - margin, width=2)
    canvas.create_line(margin, graphHeight - margin, graphWidth - margin, graphHeight - margin, width=2)

    # Draw the line for stock prices
    for i in range(1, len(stockPrices)):
        x1 = margin + (i - 1) * (graphWidth - 2 * margin) / maxPoints
        y1 = graphHeight - margin - stockPrices[i - 1]
        x2 = margin + i * (graphWidth - 2 * margin) / maxPoints
        y2 = graphHeight - margin - stockPrices[i]
        canvas.create_line(x1, y1, x2, y2, fill=lineColor, width=2)

def animateGraph(root, canvas, stockPrices, graphWidth, graphHeight, margin, maxPoints, lineColor, updateInterval):
    """Keeps the graph static for now."""
    # Redraw the graph without changing prices
    drawGraph(canvas, stockPrices, graphWidth, graphHeight, margin, maxPoints, lineColor)

    # Schedule the next update
    root.after(updateInterval, animateGraph, root, canvas, stockPrices, graphWidth, graphHeight, margin, maxPoints, lineColor, updateInterval)
def increasePrice(stockPrices, maxPoints):
    """Increases the price by a fixed amount."""
    rand = random.randint(1, 1000)
    lastPrice = stockPrices[-1]
    newPrice = lastPrice + rand  # Increase by 10 units
    stockPrices.pop(0)
    stockPrices.append(newPrice)

def decreasePrice(stockPrices, maxPoints):
    """Decreases the price by a fixed amount."""
    rand = random.randint(1, 1000)
    lastPrice = stockPrices[-1]
    newPrice = lastPrice - rand  # Decrease by 10 units, but not below 0
    stockPrices.pop(0)
    stockPrices.append(newPrice)

def savePrices(stockPrices, filename="stock_prices.json"):
    """Saves stock prices to a file."""
    with open(filename, "w") as file:
        json.dump(stockPrices, file)

def loadPrices(maxPoints, filename="stock_prices.json"):
    """Loads stock prices from a file or initializes them."""
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return [0] * maxPoints

def periodicSave(stockPrices, interval, filename="stock_prices.json"):
    """Saves the stock prices periodically."""
    savePrices(stockPrices, filename)
    root.after(interval, periodicSave, stockPrices, interval, filename)

stockPrices = loadPrices(maxPoints)

def groanTubeEconomy():
    global root, stockPrices, maxPoints
    graphWidth = 400
    graphHeight = 300
    canvas = tk.Canvas(root, width=graphWidth, height=graphHeight, background="#010203", bd=0, highlightthickness=0)
    colorkey = 0x00030201
    hwnd = canvas.winfo_id()
    wnd_exstyle = windll.user32.GetWindowLongA(hwnd, -20)  # GWL_EXSTYLE
    new_exstyle = wnd_exstyle | 0x00080000  # WS_EX_LAYERED
    windll.user32.SetWindowLongA(hwnd, -20, new_exstyle)  # GWL_EXSTYLE
    windll.user32.SetLayeredWindowAttributes(hwnd, colorkey, 255, 0x00000001)
    canvas.place(x=root.winfo_screenwidth() - (graphWidth*2), y=root.winfo_screenheight() - graphHeight)


    margin = 50
    updateInterval = 100  # Milliseconds
    lineColor = "green"
    saveInterval = 5000

    animateGraph(root, canvas, stockPrices, graphWidth, graphHeight, margin, maxPoints, lineColor, updateInterval)

    periodicSave(stockPrices, saveInterval)
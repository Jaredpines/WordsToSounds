import threading
import time
import tkinter as tk
import random
from PIL import Image, ImageTk
import cv2
import vlc

root = None
images = []
videos = []
players = []

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
    if "petting" in imagePath:
        xPos = 150
        yPos = root.winfo_screenheight() - imageHeight -200
        desiredWidth = 150
        desiredHeight = 200


    if flip == False:
        label.place(x=xPos, y=yPos)
    else:
        label.place(x=root.winfo_screenwidth() - imageWidth, y=0)

    if ".gif" in imagePath and flip == False:
        # Load frames for GIF
        frames = []
        try:
            while True:
                if "petting" in imagePath:
                    frames.append(ImageTk.PhotoImage(image.copy().resize((desiredWidth, desiredHeight)), master=root))
                else:
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
        try:
            videos.remove(canvas)
        except:
            pass

    root.after(int(duration * 950), stopVideo)

    videos.append(canvas)
    if len(videos) > 5:
        killAll()


def removeImage(label):
    """Remove an image from the screen."""
    global images
    if label in images and label.winfo_exists():
        label.destroy()
        images.remove(label)

def killAll():
    global images, videos, players
    for image in images:
        image.destroy()
    for player in players:
        player.stop()
    for video in videos:
        video.destroy()


    images = []
    videos = []
    players = []



def multipleTriggers(mediaPath, mRoot, duration=None):
    global root
    root = mRoot

    if mediaPath.endswith(".mp4"):
        threading.Thread(target=flashVideo, args=(mediaPath, duration), daemon=True).start()
    else:
        threading.Thread(target=flashImage, args=(mediaPath, duration), daemon=True).start()
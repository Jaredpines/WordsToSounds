from ctypes import windll
import tkinter as tk
import random
from PIL import Image, ImageTk

images = []
startX = 0
startY = 950
mode = "idle"
direct = "right"
def dog(root):
    global images, mode, direct, startX, startY
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
    #canvas.place(x=screenWidth - windowWidth, y=screenHeight - windowHeight)

    if direct == "left":
        image = Image.open("../Images/dIdleLeft.gif")
    elif direct == "right":
        image = Image.open("../Images/dIdleRight.gif")
    elif direct == "up":
        image = Image.open("../Images/dIdleUp.gif")
    elif direct == "down":
        image = Image.open("../Images/dIdleDown.gif")

    if direct == "left" and mode == "move":
        image = Image.open("../Images/dWalkLeft.gif")
    elif direct == "right" and mode == "move":
        image = Image.open("../Images/dWalkRight.gif")
    elif direct == "up" and mode == "move":
        image = Image.open("../Images/dWalkUp.gif")
    elif direct == "down" and mode == "move":
        image = Image.open("../Images/dWalkDown.gif")

    if mode == "backflip":
        image = Image.open("../Images/backflip.gif")

    if mode == "petting":
        pImage = Image.open("../Images/petting.gif")

    # Set the desired size for the image
    desiredWidth = 150
    desiredHeight = 200

    frames = []
    pFrames = []
    try:
        while True:
            # Resize and store original frames
            resizedFrame = image.copy().resize((desiredWidth, desiredHeight), Image.Resampling.NEAREST)
            frames.append(ImageTk.PhotoImage(resizedFrame.convert("RGBA"), master=root))


            image.seek(len(frames))
            if mode == "petting":
                pResizedFrame = pImage.copy().resize((desiredWidth//2, desiredHeight//2), Image.Resampling.NEAREST)
                pFrames.append(ImageTk.PhotoImage(pResizedFrame.convert("RGBA"), master=root))

                pImage.seek(len(frames))
    except EOFError:
        pass

    currentFrames = frames  # Start with original frames
    frameId = canvas.create_image(0, 0, image=frames[0], anchor='nw')
    if mode == "petting":
        currentPFrames = pFrames
        pettingId = canvas.create_image(40, 60, image=pFrames[0], anchor='nw')

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
    def updatePFrame(index):
        if canvas.winfo_exists():
            try:
                canvas.itemconfig(pettingId, image=currentPFrames[index])
                if index + 1 < len(currentPFrames):
                    root.after(100, updatePFrame, index + 1)
                else:
                    root.after(100, updatePFrame, 0)
            except tk.TclError:
                pass


    updateFrame(0)
    if mode == "petting":
        updatePFrame(0)
    images.append(canvas)

    dx = 5
    if direct == "left" or direct == "up":
        direction = -1
    elif direct == "right" or direct == "down":
        direction = 1
    canvas.place(x=startX, y=startY)

    def move():
        global startX, mode, startY
        nonlocal direction, currentFrames
        if canvas.winfo_exists():
            # Update position
            if direct == "left" or direct == "right":
                startX += dx * direction
            else:
                startY += dx * direction
            canvas.place(x=startX, y=startY)
            # Schedule next move
            root.after(50, move)


    if mode == "move":
        move()
        root.after(1000, lambda: changeMode("idle", root))
    elif mode == "backflip":
        root.after(len(frames)*100, lambda: changeMode("idle", root))

def changeDirection(dir, root):
    global direct, images
    for image in images:
        image.destroy()
    images = []
    direct = dir
    dog(root)

def changeMode(mo, root):
    global mode, images
    for image in images:
        image.destroy()
    images = []
    mode = mo
    dog(root)

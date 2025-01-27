from ctypes import windll
import tkinter as tk
import random
from PIL import Image, ImageTk
images = []
def pikmin(root):
    global images
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
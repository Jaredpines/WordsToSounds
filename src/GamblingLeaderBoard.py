from ctypes import windll
import tkinter as tk

canvass = []
mRoot = None

def leaderboard(root):
    global mRoot
    mRoot = root
    windowWidth = 250
    windowHeight = 285
    xPos = 0
    yPos = 0
    canvas = tk.Canvas(mRoot, width=windowWidth, height=windowHeight, background="#010203", bd=0, highlightthickness=0)
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
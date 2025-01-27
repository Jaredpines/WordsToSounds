import json
import os
import random
from ctypes import windll
import tkinter as tk

maxPoints = 50
mRoot = None
def drawGraph(canvas, stockPrices, graphWidth, graphHeight, margin, maxPoints, lineColor):
    """Draws the stock market graph with zero-based baseline for negatives."""
    canvas.delete("all")

    # Calculate scaling
    minPrice = min(stockPrices)
    maxPrice = max(stockPrices)
    baseline = max(0, -minPrice)  # Adjust baseline for negative values
    priceRange = max(maxPrice + baseline, 1)  # Include baseline in range
    yScale = (graphHeight - 2 * margin) / priceRange

    # Draw axes
    xAxisY = graphHeight - margin - baseline * yScale  # Position the x-axis
    canvas.create_line(margin, xAxisY, graphWidth - margin, xAxisY, width=2)  # X-axis
    canvas.create_line(margin, margin, margin, graphHeight - margin, width=2)  # Y-axis

    # Draw the line for stock prices
    for i in range(1, len(stockPrices)):
        x1 = margin + (i - 1) * (graphWidth - 2 * margin) / maxPoints
        y1 = graphHeight - margin - (stockPrices[i - 1] + baseline) * yScale
        x2 = margin + i * (graphWidth - 2 * margin) / maxPoints
        y2 = graphHeight - margin - (stockPrices[i] + baseline) * yScale
        canvas.create_line(x1, y1, x2, y2, fill=lineColor, width=2)

    # Display max, min, and zero level
    canvas.create_text(margin, margin - 10, text=f"Max: {maxPrice}", anchor="w", font=("Arial", 10))
    canvas.create_text(margin, graphHeight - margin + 10, text=f"Min: {minPrice}", anchor="w", font=("Arial", 10))
    canvas.create_text(margin, xAxisY - 10, text="0", anchor="w", font=("Arial", 10))


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
    global mRoot
    """Saves the stock prices periodically."""
    savePrices(stockPrices, filename)
    mRoot.after(interval, periodicSave, stockPrices, interval, filename)

stockPrices = loadPrices(maxPoints)

def groanTubeEconomy(root):
    global mRoot, stockPrices, maxPoints
    mRoot = root
    graphWidth = 400
    graphHeight = 300
    canvas = tk.Canvas(mRoot, width=graphWidth, height=graphHeight, background="#010203", bd=0, highlightthickness=0)
    colorkey = 0x00030201
    hwnd = canvas.winfo_id()
    wnd_exstyle = windll.user32.GetWindowLongA(hwnd, -20)  # GWL_EXSTYLE
    new_exstyle = wnd_exstyle | 0x00080000  # WS_EX_LAYERED
    windll.user32.SetWindowLongA(hwnd, -20, new_exstyle)  # GWL_EXSTYLE
    windll.user32.SetLayeredWindowAttributes(hwnd, colorkey, 255, 0x00000001)
    canvas.place(x=mRoot.winfo_screenwidth() - (graphWidth*2), y=mRoot.winfo_screenheight() - graphHeight)


    margin = 50
    updateInterval = 100  # Milliseconds
    lineColor = "green"
    saveInterval = 5000

    animateGraph(root, canvas, stockPrices, graphWidth, graphHeight, margin, maxPoints, lineColor, updateInterval)

    periodicSave(stockPrices, saveInterval)
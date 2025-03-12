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

from src import ChatTalks
from src.Dog import *
from src.GamblingLeaderBoard import *
from src.GroanTubeEconomy import *
from src.RhythmGame import FNFVisualizer
from src.VideoAndImage import *
from src.WalkingPikmin import *

POLLINGINTERVAL = 5
# translator = Translator()
excludedNames = {"Tio", "Gio"}
today = datetime.today()
christmasTimeStart = datetime(today.year, 12, 18)
christmasTimeEnd = datetime(today.year + 1, 1, 1)
jan = datetime(today.year, 1, 1)
win = False
groan = 0
jeff = 0
car = None


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
    fnaf = [
        "five night's at freddy's", "five nights at freddys", "freddy", "animatronic", "foxy", "bonnie", "chica",
        "baby", "ennard", "springtrap", "afton", "purple guy", "fazbear", "mangle", "puppet", "jj", "rwqfsfasxc",
        "shadow bb", "xor", "springlock", "fredbear", "phantom bb", "nightmare", "plushtrap", "balloon boy",
        "nightmarionne", "freddles", "dreadbear", "ballora", "bidybab", "minireena", "bon-bon", "lolbit", "electrobab",
        "bonnet", "music man", "lefty", "rockstar foxy's parrot", "carnie", "happy frog", "mr. hippo", "pigpatch",
        "nedd bear", "orville elephant", "mystic hippo", "monty", "montgomery gator", "roxxy", "roxanne wolf", "endo",
        "the mimic", "tangle", "helpy"
    ]
    today = datetime.today()
    p = None
    global players, content, ss, win, groan, videos, jeff, maxPoints, stockPrices, car
    # message = translateToEnglish(message)
    message = message.lower()
    name = author
    print(message)
    if "jeff" in message and jeff > 0:
        killAll()
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
        multipleTriggers("../Videos/butter.mp4", root)

    if "gamese39omg" in message or "omg" in message:
        p = vlc.MediaPlayer("../Sounds/omg.mp3")
        p.play()

    if "pikmin" in message:
        rand = random.randint(0, 4)
        if rand == 0:
            p = vlc.MediaPlayer("../Sounds/pikmin.mp3")
            pikmin(root)
        elif rand == 1:
            p = vlc.MediaPlayer("../Sounds/pikmindeath.mp3")
            multipleTriggers("../Images/pikminy.gif", root, duration=2)
        elif rand == 2:
            p = vlc.MediaPlayer("../Sounds/pikminfall.mp3")
            multipleTriggers("../Images/pikminy.gif", root, duration=2)
        elif rand == 3:
            p = vlc.MediaPlayer("../Sounds/pikminpluck.mp3")
            pikmin(root)
        elif rand == 4:
            p = vlc.MediaPlayer("../Sounds/pikminthrow.mp3")
            multipleTriggers("../Images/pikminy.gif", root, duration=2)
        p.play()

    if "gamese39yippee" in message or "yippee" in message or "yippie" in message:
        count = message.count("yippee") + message.count("gamese39yippee")+ message.count("yippie")
        rand = random.randint(0, 1)
        if rand == 0:
            for _ in range(1,count):
                p = vlc.MediaPlayer("../Sounds/yippee.mp3")
                p.play()
        else:
            multipleTriggers("../Videos/yippee.mp4", root)

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
            multipleTriggers("../Videos/gamblinglose.mp4", root, duration=6)
            win = False
        else:
            multipleTriggers("../Videos/gamblingwin.mp4", root)
            win = True

        inputOutputFilePath = "../Leaderboard/saves.txt"
        try:
            with open(inputOutputFilePath, 'r+', encoding='utf-8') as inoutfile:
                lines = inoutfile.readlines()  # Read all lines into a list

                author_found = False
                for i, line in enumerate(lines):
                    if author.displayname in line and win==True:
                        author_found = True
                        # Extract the current win count from the line
                        current_wins = int(line.split(":")[1].split()[0])  # Get the current win count as an integer
                        # Increment the wins by 1
                        lines[i] = f"{author.displayname}: {current_wins + 1} wins\n"  # Update the line with new win count
                        break  # Exit the loop once the author is found
                    elif author.displayname in line and win==False:
                        author_found = True
                        current_wins = int(line.split(":")[1].split()[0])
                        lines[i] = f"{author.displayname}: {current_wins} wins\n"
                if not author_found and win == True:
                    # If the author is not found, add a new line with 1 win
                    lines.append(f"{author.displayname}: 1 win\n")
                elif not author_found and win == False:
                    lines.append(f"{author.displayname}: 0 wins\n")

                # Go back to the beginning of the file and overwrite the content
                inoutfile.seek(0)
                inoutfile.writelines(lines)  # Write the modified content back to the file
                inoutfile.truncate()  # Ensure the file is truncated to the correct size
                win = False

        except FileNotFoundError:
            print(f"File not found: {inputOutputFilePath}")
        except Exception as e:
            print(f"An error occurred: {e}")
        leaderboard(root)
    if message in fnaf:
        rand = random.randint(1, 9)
        if rand == 1:
            multipleTriggers("../Videos/fnaf1.mp4", root)
        elif rand == 2:
            multipleTriggers("../Videos/fnaf2.mp4", root)
        elif rand == 3:
            multipleTriggers("../Videos/fnaf3.mp4", root, duration=8)
        elif rand == 4:
            multipleTriggers("../Videos/fnaf4.mp4", root)
        elif rand == 5:
            multipleTriggers("../Videos/fnaf5.mp4", root)
        elif rand == 6:
            multipleTriggers("../Videos/fnaf6.mp4", root)
        elif rand == 7:
            multipleTriggers("../Videos/fnafs.mp4", root)
        elif rand == 8:
            multipleTriggers("../Videos/fnafj.mp4", root)
        elif rand == 9:
            multipleTriggers("../Videos/fivebooms.mp4", root)

    if "one piece" in message or "onepiece" in message:
        p = vlc.MediaPlayer("../Sounds/onepiece.mp3")
        p.play()
        multipleTriggers("../Images/onepiece.gif", root, duration=12)

    if "i'm sorry" in message or "i am sorry" in message or "sowwy" in message or "gamese39sowwy" in message:
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
            multipleTriggers("../Videos/christmas.mp4", root)

    if "freeze" in message:
        multipleTriggers("../Videos/freeze.mp4", root)

    if "soccer" in message:
        count = message.count("soccer")
        for _ in range(count):
            multipleTriggers("../Videos/soccer.mp4", root, duration=12)

    if "jeff" in message and jeff == 0:
        multipleTriggers("../Videos/jeff.mp4", root)
        jeff += 1

    if "content" in message:
        multipleTriggers("../Videos/mimic.mp4", root)

    if "subway surfers" in message and ss == 1:
        ss -= 1
        multipleTriggers("../Videos/subway.mp4", root)

    if "these games before" in message:
        multipleTriggers("../Videos/squid.mp4", root)

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
        multipleTriggers("../Videos/jerma.mp4", root)

    if "glorp" in message:
        multipleTriggers("../Videos/glorp.mp4", root)

    if "huh" in message:
        multipleTriggers("../Videos/huh.mp4", root)

    if "donate" in message or "donation" in message or "donating" in message or "give me your money" in message:
        count = message.count("donate") + message.count("donation") + message.count("donating") + message.count("give me your money")
        for _ in range(count):
            multipleTriggers("../Videos/give.mp4", root)

    if "i'm dead" in message:
        multipleTriggers("../Videos/imdead.mp4", root)

    if "flashbang" in message or "flash bang" in message:
        count = message.count("flashbang") + message.count("flash bang")
        for _ in range(count):
            multipleTriggers("../Videos/thinkfast.mp4", root)

    if "some of this on your that" in message:
        multipleTriggers("../Videos/rett.mp4", root)

    if "peanut butter and jelly the long way" in message:
        multipleTriggers("../Videos/peanutbutter.mp4", root)

    if "fish" in message:
        rand = random.randint(1, 8)
        if "fish horror" in message:
            rand = 9
        if rand < 8:
            multipleTriggers("../Videos/fish.mp4", root)
        else:
            multipleTriggers("../Videos/fish2.mp4", root)

    if "what the dog doing" in message:
        multipleTriggers("../Videos/what.mp4", root)

    if "salami lid" in message:
        multipleTriggers("../Videos/lid.mp4", root)


    if "bird up" in message:
        multipleTriggers("../Videos/bird.mp4", root)

    if "explode" in message:
        multipleTriggers("../Videos/boom.mp4", root)

    if "hawaii" in message:
        multipleTriggers("../Videos/hawaii.mp4", root)

    if "yellow" in message:
        count = message.count("yellow")
        for _ in range(count):
            multipleTriggers("../Videos/yellow.mp4", root)

    if "our table" in message:
        multipleTriggers("../Videos/table.mp4", root)

    if "meow" in message:
        multipleTriggers("../Videos/meow.mp4", root)

    if "getting water" in message:
        multipleTriggers("../Videos/water.mp4", root)

    if "snack" in message:
        multipleTriggers("../Videos/cheese.mp4", root, 12)

    if "mr. beast" in message or "mr beast" in message or "mrbeast" in message:
        multipleTriggers("../Videos/beast.mp4", root)

    if re.search(rf"\berb\b", message):
        rand = random.randint(1, 6)
        if rand < 6:
            multipleTriggers("../Videos/fakeerb.mp4", root)
        else:
            multipleTriggers("../Videos/erb.mp4", root)

    if "buzzer" in message:
        multipleTriggers("../Videos/buzzer.mp4", root)

    if "creature" in message:
        multipleTriggers("../Videos/creature.mp4", root)

    if "lsg is here" in message:
        multipleTriggers("../Videos/challenger.mp4", root)

    if "edwin" in message:
        multipleTriggers("../Videos/edwin.mp4", root)

    # if "i am" in message and author == "GameSelectLive":
    #     multipleTriggers("../Videos/am.mp4", root)

    if "no aura" in message:
        multipleTriggers("../Videos/aura.mp4", root)

    if "the ps5" in message:
        multipleTriggers("../Videos/ps5.mp4", root)

    if "stamper missed" in message:
        multipleTriggers("../Videos/ps52.mp4", root)

    if "what's wrong with the juice" in message or "whats wrong with the juice" in message:
        multipleTriggers("../Videos/soda.mp4", root)

    if "my name is david" in message:
        rand = random.randint(1, 2)
        if rand == 1:
            multipleTriggers("../Videos/david.mp4", root)
        elif rand == 2:
            multipleTriggers("../Videos/under.mp4", root)


    if "micola" in message:
        multipleTriggers("../Videos/micola.mp4", root)

    if "chuck e cheese" in message or "chuck-e-cheese" in message:
        multipleTriggers("../Videos/chuck.mp4", root)

    if "eggman" in message or "egg man" in message:
        multipleTriggers("../Videos/eggman.mp4", root)

    if "gerald" in message:
        multipleTriggers("../Videos/gerald.mp4", root)

    if "shadow" in message:
        multipleTriggers("../Videos/shadow.mp4", root)

    if "mushroom" in message:
        multipleTriggers("../Videos/mushroom.mp4", root)

    if "speed" in message:
        multipleTriggers("../Videos/speed.mp4", root)

    if "home run" in message:
        multipleTriggers("../Videos/homerun.mp4", root)

    if "boat dog" in message:
        multipleTriggers("../Videos/boatdog.mp4", root)

    if "silly billy" in message:
        multipleTriggers("../Videos/silly.mp4", root)

    if "crack" in message:
        multipleTriggers("../Videos/crack.mp4", root)

    if "bogos binted" in message or "bogos vintage" in message or "boat goes binted" in message or "boat goes vintage" in message:
        rand = random.randint(1, 3)
        if rand == 1:
            multipleTriggers("../Videos/bogo.mp4", root)
        elif rand == 2:
            multipleTriggers("../Videos/photos.mp4", root)
        elif rand == 3:
            multipleTriggers("../Videos/boat.mp4", root)

    if re.search(rf"\bstep mom\b", message):
        multipleTriggers("../Videos/howler.mp4", root)

    if "up" in message:
        changeDirection("up", root)
    elif "down" in message:
        changeDirection("down", root)
    elif "left" in message:
        changeDirection("left", root)
    elif "right" in message:
        changeDirection("right", root)



    if "move" in message:
        changeMode("move", root)

    if "do a backflip" in message:
        changeMode("backflip", root)

    if "pet dog" in message:
        changeMode("petting", root)

    if "good boy" in message:
        multipleTriggers("../Images/petting.gif", root, duration=4)

    if "kill" in message:
        killAll()
    if car is not None:
        if car.get_playing() == False:
            if name is not "GameSelectLive" and "gamese39" not in message:
                #ChatTalks.mode = "talk"
                ChatTalks.chatTalks(message)
            try:
                if author.is_mod and "car's little song" in message:
                    root.after(100, create_car())
            except:
                pass
    else:
        if name is not "GameSelectLive" and  "gamese39" not in message:
            # ChatTalks.mode = "talk"
            ChatTalks.chatTalks(message)
        try:
            if author.is_mod and "car's little song" in message:
                root.after(100, create_car())
        except:
            pass


root = None



def setupTkinter():
    global root
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.attributes('-fullscreen', True)
    root.attributes('-transparentcolor', 'purple')
    root.configure(bg='purple')
    root.after(100, leaderboard, root)
    root.after(100, groanTubeEconomy, root)
    root.after(100, dog, root)

    #root.after(100, ChatTalks.chat, root)


def runTkinter():
    """Run the Tkinter event loop in an async-compatible way."""
    global root
    setupTkinter()
    root.mainloop()

def create_car():
    global car
    car = FNFVisualizer(root, '../FNF/cars-little-song.json', "../FNF/CarVideo.mp4")





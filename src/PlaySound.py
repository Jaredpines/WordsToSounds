import asyncio
import re
import vlc
import threading
from PIL import Image, ImageTk
import tkinter as tk
from googletrans import Translator
import random


POLLING_INTERVAL = 5
translator = Translator()
excluded_names = {"Tio", "Gio"}
p = vlc.MediaPlayer("../Sounds/metalpipe.mp3")



def translateToEnglish(text):
    placeholder_map = {}
    words = text.split()
    for i, word in enumerate(words):
        clean_word = word.strip("!,.?")  # Remove punctuation for matching
        if clean_word.capitalize() in excluded_names:
            placeholder = f"__name_{i}__"
            placeholder_map[placeholder] = word
            words[i] = placeholder

    text_with_placeholders = " ".join(words)
    detected_lang = translator.detect(text_with_placeholders).lang

    if detected_lang != "en":
        translated_text = translator.translate(text_with_placeholders, dest="en").text
    else:
        translated_text = text_with_placeholders

    for placeholder, original_name in placeholder_map.items():
        print(placeholder)
        print(original_name)
        translated_text = translated_text.replace(placeholder, original_name)

    return translated_text


def play_sound(message):
    global p
    #message = translateToEnglish(message)
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
            p = vlc.MediaPlayer("../Sounds/gamblinglose.mp3")
        else:
            p = vlc.MediaPlayer("../Sounds/gamblingwin.mp3")
        p.play()
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
            p = vlc.MediaPlayer("../Sounds/fnaf1.mp3")
        elif rand == 2:
            p = vlc.MediaPlayer("../Sounds/fnaf2.mp3")
        elif rand == 3:
            p = vlc.MediaPlayer("../Sounds/fnaf3.mp3")
        elif rand == 4:
            p = vlc.MediaPlayer("../Sounds/fnaf4.mp3")
        elif rand == 5:
            p = vlc.MediaPlayer("../Sounds/fnaf5.mp3")
        elif rand == 6:
            p = vlc.MediaPlayer("../Sounds/fnaf6.mp3")
        elif rand == 7:
            p = vlc.MediaPlayer("../Sounds/fnafs.mp3")
        elif rand == 8:
            p = vlc.MediaPlayer("../Sounds/fnafj.mp3")
        multipleTriggers("../Images/foxy.gif", duration=2)

    if "one piece" in message or "onepiece" in message:
        p = vlc.MediaPlayer("../Sounds/onepiece.mp3")
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
        #multipleTriggers("../Images/moist.png", duration=2)

    if "bye gio" in message:
        p = vlc.MediaPlayer("../Sounds/byeosu.mp3")
        p.play()

    if "christmas" in message:
        p = vlc.MediaPlayer("../Sounds/christmas.mp3")
        multipleTriggers("../Images/christmas.gif", duration=19)

    if "freeze" in message:
        p = vlc.MediaPlayer("../Sounds/freeze.mp3")
        multipleTriggers("../Images/freeze.gif", duration=12)

root = None
images = []

def setup_tkinter():
    """Initialize the Tkinter root window."""
    global root
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.attributes('-fullscreen', True)
    root.attributes('-transparentcolor', 'black')
    root.configure(bg='black')

def flash_image(imagePath, duration=3):
    """Flash an image on the screen."""
    global root, images
    if root is None:
        raise RuntimeError("Tkinter root is not initialized. Call setup_tkinter first.")

    # Load the image
    image = Image.open(imagePath)
    image_width, image_height = image.size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Random position on screen
    x_pos = random.randint(0, screen_width - image_width)
    y_pos = random.randint(0, screen_height - image_height)

    # Create a label for the image
    label = tk.Label(root, bg='black')
    label.place(x=x_pos, y=y_pos)

    if ".gif" in imagePath:
        # Load frames for GIF
        frames = []
        try:
            while True:
                frames.append(ImageTk.PhotoImage(image.copy(), master=root))
                image.seek(len(frames))
        except EOFError:
            pass

        def update_frame(index):
            if label.winfo_exists():
                try:
                    label.config(image=frames[index])
                    label.image = frames[index]  # Keep a reference to avoid garbage collection
                    if index + 1 < len(frames):
                        root.after(100, update_frame, index + 1)
                    else:
                        root.after(100, update_frame, 0)
                except tk.TclError:
                    pass

        p.play()
        update_frame(0)
    else:
        # Single frame image
        img = ImageTk.PhotoImage(image, master=root)
        label.config(image=img)
        label.image = img  # Keep a reference

    # Add the label to the active list and schedule its removal
    images.append(label)
    root.after(int(duration * 1000), lambda: remove_image(label))

def remove_image(label):
    """Remove an image from the screen."""
    global images
    if label in images and label.winfo_exists():
        label.destroy()
        images.remove(label)

def run_tkinter():
    """Run the Tkinter event loop in an async-compatible way."""
    global root
    setup_tkinter()
    root.mainloop()
def multipleTriggers(imagePath, duration=2):
    threading.Thread(target=flash_image, args=(imagePath, duration), daemon=True).start()

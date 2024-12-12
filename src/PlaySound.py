import random

from src.GrabChat import Bot
import vlc


def play_sound(message):
    #print(message)
    if "steal" in message or "steel" in message:
        p = vlc.MediaPlayer("../Sounds/metalpipe.mp3")
        p.play()

    if "vine boom" in message or "vineboom" in message:
        p = vlc.MediaPlayer("../Sounds/vineboom.mp3")
        p.play()

    if "get out" in message or "get ou" in message or "getout" in message or "getou" in message:
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



bot = Bot(callback=play_sound)
bot.run()

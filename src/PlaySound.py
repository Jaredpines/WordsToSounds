import random
import re
from src.GrabChat import Bot
import vlc


def play_sound(message):
    # print(message)
    if "steal" in message or "steel" in message:
        p = vlc.MediaPlayer("../Sounds/metalpipe.mp3")
        p.play()

    if "vine boom" in message or "vineboom" in message:
        p = vlc.MediaPlayer("../Sounds/vineboom.mp3")
        p.play()

    if "get out" in message or re.search(rf"\bget ou\b", message) or "getout" in message or re.search(rf"\bgetou\b", message):
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
        p.play()

    if "one piece" in message or "onepiece" in message:
        p = vlc.MediaPlayer("../Sounds/onepiece.mp3")
        p.play()

    if "sorry" in message or "sowwy" in message or "gamese39sowwy" in message:
        p = vlc.MediaPlayer("../Sounds/sad.mp3")
        p.play()

    if "pog" in message or "poggers" in message or "gamese39gslpog" in message:
        p = vlc.MediaPlayer("../Sounds/pog.mp3")
        p.play()

    if re.search(rf"\bcar\b", message) or "gamese39happycar" in message or "gamese39car" in message or "gamese39shinycar" in message:
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

bot = Bot(callback=play_sound)
bot.run()

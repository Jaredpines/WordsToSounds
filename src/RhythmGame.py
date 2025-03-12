import tkinter as tk
import json
import time
from ctypes import windll
import cv2
import vlc
from PIL import Image, ImageTk


class FNFVisualizer:
    def __init__(self, root, song_path, video_path=None):
        self.root = root
        self.video_path = video_path
        self.video(self.video_path)
        self.root.title("FNF Visualizer")
        self.start = {}
        self.playing = True

        # Creating the notes canvas and placing it below the video canvas
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="#010203")
        colorkey = 0x00030201
        hwnd = self.canvas.winfo_id()
        wnd_exstyle = windll.user32.GetWindowLongA(hwnd, -20)  # GWL_EXSTYLE
        new_exstyle = wnd_exstyle | 0x00080000  # WS_EX_LAYERED
        windll.user32.SetWindowLongA(hwnd, -20, new_exstyle)  # GWL_EXSTYLE
        windll.user32.SetLayeredWindowAttributes(hwnd, colorkey, 255, 0x00000001)

        # Place the notes canvas below the video canvas (adjust yPos for your desired position)
        self.canvas.place(x=0, y=0)  # Example: place it at the bottom of the screen

        self.load_song(song_path)
        self.note_speed = 5
        self.notes = []
        self.active_notes = {}
        self.start_time = time.time()
        self.hit_window = 200  # Increased hit window
        self.fall_distance = 500
        self.arrow_size = 40  # Arrow size for larger hit boxes
        self.update_notes()
        self.bind_keys()

        # Load arrow images (replace with your actual image paths)
        self.arrow_images_start = {
            0: Image.open("../Images/left_arrow.png"),
            1: Image.open("../Images/down_arrow.png"),
            2: Image.open("../Images/up_arrow.png"),
            3: Image.open("../Images/right_arrow.png")
        }
        # Resize images and store references to them
        self.arrow_images_start = {key: img.resize((self.arrow_size * 4, self.arrow_size * 4)) for key, img in
                             self.arrow_images_start.items()}
        # Load arrow images (replace with your actual image paths)
        self.arrow_images = {
            0: Image.open("../Images/left_arrow_color.png"),
            1: Image.open("../Images/down_arrow_color.png"),
            2: Image.open("../Images/up_arrow_color.png"),
            3: Image.open("../Images/right_arrow_color.png")
        }
        # Resize images and store references to them
        self.arrow_images = {key: img.resize((self.arrow_size * 4, self.arrow_size * 4)) for key, img in
                                   self.arrow_images.items()}
        # Load arrow images (replace with your actual image paths)
        self.arrow_images_press = {
            0: Image.open("../Images/left_arrow_press.png"),
            1: Image.open("../Images/down_arrow_press.png"),
            2: Image.open("../Images/up_arrow_press.png"),
            3: Image.open("../Images/right_arrow_press.png")
        }
        # Resize images and store references to them
        self.arrow_images_press = {key: img.resize((self.arrow_size * 4, self.arrow_size * 4)) for key, img in
                             self.arrow_images_press.items()}

        self.arrow_images_hold = {
            0: Image.open("../Images/left_arrow_hold.png").transpose(Image.FLIP_TOP_BOTTOM),
            1: Image.open("../Images/down_arrow_hold.png").transpose(Image.FLIP_TOP_BOTTOM),
            2: Image.open("../Images/up_arrow_hold.png").transpose(Image.FLIP_TOP_BOTTOM),
            3: Image.open("../Images/right_arrow_hold.png").transpose(Image.FLIP_TOP_BOTTOM)
        }
        # Resize images and store references to them
        self.arrow_images_hold = {key: img.resize((self.arrow_size * 4, self.arrow_size * 4)) for key, img in
                                  self.arrow_images_hold.items()}

        self.arrow_images_hold_end = {
            0: Image.open("../Images/left_arrow_hold_end.png").transpose(Image.FLIP_TOP_BOTTOM),
            1: Image.open("../Images/down_arrow_hold_end.png").transpose(Image.FLIP_TOP_BOTTOM),
            2: Image.open("../Images/up_arrow_hold_end.png").transpose(Image.FLIP_TOP_BOTTOM),
            3: Image.open("../Images/right_arrow_hold_end.png").transpose(Image.FLIP_TOP_BOTTOM)
        }
        self.image_refs_start = {}
        self.image_refs = {}
        self.draw_hit_indicators()

    def draw_arrow(self, x, y, lane, start=None):
        """Replace the arrow with an image."""
        if start == "start":
            image = self.arrow_images_start[lane]  # Use the start image
        elif start == "hold":
            image = self.arrow_images_hold[lane]  # Use the hold image
        elif start == "hold_end":
            image = self.arrow_images_hold[lane]  # Use the hold end piece image
        else:
            image = self.arrow_images[lane]  # Use the colored image

        tk_image = ImageTk.PhotoImage(image, master=self.root)

        # Store the image reference per note to prevent garbage collection
        note_id = self.canvas.create_image(x, y, image=tk_image)
        self.image_refs[note_id] = tk_image  # Store the reference using the note ID

        return note_id

    def load_song(self, song_path):
        with open(song_path, 'r') as file:
            data = json.load(file)
            self.note_data = []
            for section in data["song"]["notes"]:
                for note in section["sectionNotes"]:
                    timestamp = note[0] / 1000
                    lane = note[1]
                    self.note_data.append((timestamp, lane))

    def on_key_press(self, lane):
        # Change the indicator image to the hit image
        image = self.arrow_images_press[lane]
        tk_image = ImageTk.PhotoImage(image, master=self.root)
        self.image_refs[self.start[lane]] = tk_image
        self.canvas.itemconfig(self.start[lane], image=tk_image)

        # Call the hit_note method to check for a hit
        self.hit_note(lane)

    def on_key_release(self, lane):
        # Reset to the original image when the key is released
        image = self.arrow_images_start[lane]
        tk_image = ImageTk.PhotoImage(image, master=self.root)
        self.image_refs[self.start[lane]] = tk_image
        self.canvas.itemconfig(self.start[lane], image=tk_image)

    def bind_keys(self):
        self.root.bind("<Left>", lambda event: self.hit_note(0))
        self.root.bind("<Up>", lambda event: self.hit_note(2))
        self.root.bind("<Down>", lambda event: self.hit_note(1))
        self.root.bind("<Right>", lambda event: self.hit_note(3))
        self.root.bind("a", lambda event: self.hit_note(0))
        self.root.bind("w", lambda event: self.hit_note(2))
        self.root.bind("s", lambda event: self.hit_note(1))
        self.root.bind("d", lambda event: self.hit_note(3))

        self.root.bind("<KeyPress-Left>", lambda event: self.on_key_press(0))
        self.root.bind("<KeyRelease-Left>", lambda event: self.on_key_release(0))
        self.root.bind("<KeyPress-Down>", lambda event: self.on_key_press(1))
        self.root.bind("<KeyRelease-Down>", lambda event: self.on_key_release(1))
        self.root.bind("<KeyPress-Up>", lambda event: self.on_key_press(2))
        self.root.bind("<KeyRelease-Up>", lambda event: self.on_key_release(2))
        self.root.bind("<KeyPress-Right>", lambda event: self.on_key_press(3))
        self.root.bind("<KeyRelease-Right>", lambda event: self.on_key_release(3))

        self.root.bind("<KeyPress-a>", lambda event: self.on_key_press(0))
        self.root.bind("<KeyRelease-a>", lambda event: self.on_key_release(0))
        self.root.bind("<KeyPress-s>", lambda event: self.on_key_press(1))
        self.root.bind("<KeyRelease-s>", lambda event: self.on_key_release(1))
        self.root.bind("<KeyPress-w>", lambda event: self.on_key_press(2))
        self.root.bind("<KeyRelease-w>", lambda event: self.on_key_release(2))
        self.root.bind("<KeyPress-d>", lambda event: self.on_key_press(3))
        self.root.bind("<KeyRelease-d>", lambda event: self.on_key_release(3))

    def hit_note(self, lane):
        current_time = (time.time() - self.start_time) * 1000
        for note_id, (note_lane, note_time) in list(self.active_notes.items()):
            if note_lane == lane and abs(current_time - note_time) <= self.hit_window:
                self.canvas.delete(note_id)
                del self.active_notes[note_id]
                print(f"Hit! Lane: {lane}")
                break

    def draw_hit_indicators(self):
        for i in range(4):
            x = 150 + i * 150
            y = 500
            note_id = self.draw_arrow(x, y, i, "start")
            self.start[i] = note_id

    def update_notes(self):
        current_time = time.time() - self.start_time
        for timestamp, lane in list(self.note_data):
            if current_time >= timestamp - (self.fall_distance / self.note_speed / 100):
                x = 150 + lane * 150
                y = 0
                note = self.draw_arrow(x, y, lane)
                self.notes.append((note, y))
                self.active_notes[note] = (lane, timestamp * 1000)
                self.note_data.remove((timestamp, lane))

        for note, y in self.notes:
            new_y = y + self.note_speed
            self.canvas.move(note, 0, self.note_speed)
            y = new_y

        self.root.after(10, self.update_notes)

    def video(self, video_path, duration=None):
        # Create a new VLC instance for playback
        instance = vlc.Instance()
        player = instance.media_player_new()
        media = instance.media_new(video_path)
        player.set_media(media)
        player.audio_set_volume(100)
        player.audio_set_mute(False)
        cap = cv2.VideoCapture(video_path)
        videoWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        videoHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cap.release()

        # Scale video dimensions to fit within maxWidth and maxHeight
        scale = max(650 / videoWidth, 600 / videoHeight)  # default max size 640x360
        scaledWidth = int(videoWidth * scale)
        scaledHeight = int(videoHeight * scale)

        xPos = 0
        yPos = 0
        canvas = tk.Canvas(self.root, width=scaledWidth, height=scaledHeight, bg='purple', highlightthickness=0)
        canvas.place(x=xPos, y=yPos)

        # Set the VLC video output to the canvas
        hwnd = canvas.winfo_id()  # Windows handle ID
        player.set_hwnd(hwnd)

        # Start playback
        player.play()

        time.sleep(0.025)

        # Get the video duration in seconds
        videoDuration = player.get_length() / 1000  # VLC gives duration in milliseconds

        # If the video duration is not provided, use the video’s actual length
        if not duration:
            duration = videoDuration

        # Schedule the video stop based on the video's actual length
        def stopVideo():
            player.stop()
            canvas.destroy()
            self.playing = False
            self.canvas.destroy()

        self.root.after(int(duration * 1000), stopVideo)
    def get_playing(self):
        return self.playing


# root = tk.Tk()
# app = FNFVisualizer(root, '../FNF/cars-little-song.json', '../FNF/CarVideo.mp4')
# root.mainloop()

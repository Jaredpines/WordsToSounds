import os
from dotenv import load_dotenv
from twitchio.ext import commands

class Bot(commands.Bot):
    load_dotenv()
    def __init__(self, callback):
        super().__init__(token=os.getenv("TOKEN"), prefix='!', initial_channels=[os.getenv("CHANNEL")])
        self.callback = callback
    async def event_ready(self):
        print(f"Logged in as {self.nick}")

    async def event_message(self, message):
        if message.echo:
            return
        self.callback(f'{message.content.lower()}')


import asyncio
import threading

import nest_asyncio
from dotenv import load_dotenv
from twitchio.ext import commands
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os

from src.PlaySound import playSound, runTkinter, setupTkinter

nest_asyncio.apply()
POLLING_INTERVAL = 5
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]


# Twitch bot setup
class TwitchBot(commands.Bot):
    load_dotenv()
    def __init__(self, callback):
        super().__init__(token=os.getenv("TOKEN"), prefix='!', initial_channels=[os.getenv("CHANNEL"),])
        self.callback = callback

    async def event_ready(self):
        print(f"Twitch bot logged in as {self.nick}")

    async def event_message(self, message):
        if message.echo:
            return
        self.callback(message.author.display_name, f"{message.content}")


class YouTubeChatHandler:

    def __init__(self, callback):
        self.callback = callback
        self.api = None
        self.live_chat_id = None
        self.next_page_token = None

    def authenticate(self):
        creds = None
        if os.path.exists("token.pickle"):
            with open("token.pickle", "rb") as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "../client_secret.json", SCOPES)
                creds = flow.run_local_server(port=0)
            with open("token.pickle", "wb") as token:
                pickle.dump(creds, token)

        self.api = build("youtube", "v3", credentials=creds)

    def get_live_chat_id(self):
        request = self.api.liveBroadcasts().list(
            part="snippet",
            broadcastStatus="active",
            broadcastType="all"
        )
        response = request.execute()
        if "items" not in response or not response["items"]:
            print("No active live broadcast found.")
            return None
        return response["items"][0]["snippet"]["liveChatId"]

    def fetch_chat_messages(self):
        if not self.live_chat_id:
            return None, None

        request = self.api.liveChatMessages().list(
            liveChatId=self.live_chat_id,
            part="snippet,authorDetails",
            pageToken=self.next_page_token
        )
        response = request.execute()

        messages = []
        for item in response.get("items", []):
            message = item["snippet"]["textMessageDetails"]["messageText"]
            messages.append(message)

        next_page_token = response.get("nextPageToken", None)
        return messages, next_page_token

    async def poll_chat(self):
        while self.live_chat_id:
            messages, self.next_page_token = await asyncio.to_thread(self.fetch_chat_messages)

            if messages:
                for message in messages:
                    self.callback(f"{message}")

            await asyncio.sleep(5)  # Adjust polling interval as needed

    async def start(self):
        self.authenticate()
        self.live_chat_id = self.get_live_chat_id()
        if not self.live_chat_id:
            print("No YouTube live chat available.")
            return
        print("Connected to YouTube live chat!")
        await self.poll_chat()



async def main():
    twitch_bot = TwitchBot(playSound)
    youtube_handler = YouTubeChatHandler(playSound)
    setupTkinter()
    threading.Thread(target=runTkinter, daemon=True).start()

    # Run both handlers concurrently
    await asyncio.gather(
        #youtube_handler.start(),
        twitch_bot.start()
    )


if __name__ == "__main__":
    asyncio.run(main())

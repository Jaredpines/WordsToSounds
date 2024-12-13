from dotenv import load_dotenv
from twitchio.ext import commands
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle


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


SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]


def authenticate():
    creds = None
    # Load credentials from file if available
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    # If no valid credentials, let the user authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "../client_secret.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save the credentials for next time
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("youtube", "v3", credentials=creds)


def get_live_chat_id(api):
    """Retrieve the live chat ID for the currently active livestream."""
    request = api.liveBroadcasts().list(
        part="snippet",
        broadcastStatus="active",
        broadcastType="all"
    )
    response = request.execute()

    if "items" not in response or not response["items"]:
        print("No active live broadcast found.")
        return None

    return response["items"][0]["snippet"]["liveChatId"]


def get_chat_messages(api, live_chat_id, callback, page_token=None):
    """Poll the live chat messages and pass them to the callback."""
    request = api.liveChatMessages().list(
        liveChatId=live_chat_id,
        part="snippet,authorDetails",
        pageToken=page_token
    )
    response = request.execute()

    for item in response["items"]:
        author = item["authorDetails"]["displayName"]
        message = item["snippet"]["textMessageDetails"]["messageText"]
        callback(f"{author}: {message}")

    return response.get("nextPageToken", None)

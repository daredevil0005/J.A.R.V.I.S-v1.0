import webbrowser
import urllib.parse
from googleapiclient.discovery import build
from livekit.agents import function_tool
from features.explanation import set_last_action
from dotenv import load_dotenv
import os

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
def search_first_video(query: str):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=1
    )

    response = request.execute()

    if not response["items"]:
        return None

    return response["items"][0]["id"]["videoId"]


@function_tool()
async def search_youtube(query: str) -> str:
    """
    Open YouTube search results page.
    """
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.youtube.com/results?search_query={encoded_query}"

    webbrowser.open(url)
    set_last_action(f"Searched YouTube for {query}")
    return f"Searching YouTube for {query}."


@function_tool()
async def play_youtube_video(query: str) -> str:
    """
    Search and play first matching YouTube video.
    """
    video_id = search_first_video(query)

    if not video_id:
        return "I couldn't find that video on YouTube."

    url = f"https://www.youtube.com/watch?v={video_id}"
    webbrowser.open(url)

    set_last_action(f"Played YouTube video: {query}")
    return f"Playing {query} on YouTube."

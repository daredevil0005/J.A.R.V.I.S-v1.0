import os
import subprocess
import pyautogui
from livekit.agents import function_tool
from features.explanation import set_last_action
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from features.youtube import search_youtube
import pygame

# Spotify credentials - user needs to set these
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

if SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET:
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))
else:
    sp = None

pygame.mixer.init()

# Global playlist for local music
playlist = []
current_index = 0

def find_music_files(directory):
    music_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.mp3', '.wav', '.flac', '.aac', '.ogg')):
                music_files.append(os.path.join(root, file))
    return music_files

@function_tool()
async def load_local_music(directory: str = "C:\\") -> str:
    global playlist
    playlist = find_music_files(directory)
    set_last_action(f"Loaded {len(playlist)} music files from {directory}")
    return f"Loaded {len(playlist)} music files."

@function_tool()
async def play_music(file_path: str = None) -> str:
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        set_last_action(f"Playing {file_path}")
        return f"Playing {file_path}"
    elif playlist:
        pygame.mixer.music.load(playlist[current_index])
        pygame.mixer.music.play()
        set_last_action(f"Playing {playlist[current_index]}")
        return f"Playing {playlist[current_index]}"
    else:
        pyautogui.press("playpause")
        set_last_action("Toggled play/pause")
        return "Toggled play/pause"

@function_tool()
async def pause_music() -> str:
    pygame.mixer.music.pause()
    pyautogui.press("playpause")  # Fallback
    set_last_action("Paused music")
    return "Music paused."

@function_tool()
async def next_track() -> str:
    global current_index
    if playlist:
        current_index = (current_index + 1) % len(playlist)
        pygame.mixer.music.load(playlist[current_index])
        pygame.mixer.music.play()
        set_last_action(f"Playing next: {playlist[current_index]}")
        return f"Playing next: {playlist[current_index]}"
    else:
        pyautogui.press("nexttrack")
        set_last_action("Next track")
        return "Next track."

@function_tool()
async def previous_track() -> str:
    global current_index
    if playlist:
        current_index = (current_index - 1) % len(playlist)
        pygame.mixer.music.load(playlist[current_index])
        pygame.mixer.music.play()
        set_last_action(f"Playing previous: {playlist[current_index]}")
        return f"Playing previous: {playlist[current_index]}"
    else:
        pyautogui.press("prevtrack")
        set_last_action("Previous track")
        return "Previous track."

@function_tool()
async def search_music(query: str, platform: str = "local") -> str:
    if platform.lower() == "spotify":
        if not sp:
            return "Spotify credentials not set."
        results = sp.search(q=query, type='track', limit=5)
        tracks = results['tracks']['items']
        if tracks:
            track = tracks[0]
            url = track['external_urls']['spotify']
            subprocess.run(["start", url], shell=True)
            set_last_action(f"Searched and opened {track['name']} on Spotify")
            return f"Opened {track['name']} by {track['artists'][0]['name']} on Spotify"
        else:
            return "No results found on Spotify."
    elif platform.lower() == "youtube":
        return await search_youtube(query)
    elif platform.lower() == "local":
        # Search in playlist
        matches = [f for f in playlist if query.lower() in os.path.basename(f).lower()]
        if matches:
            global current_index
            current_index = playlist.index(matches[0])
            pygame.mixer.music.load(matches[0])
            pygame.mixer.music.play()
            set_last_action(f"Playing local match: {matches[0]}")
            return f"Playing {matches[0]}"
        else:
            return "No local matches found."
    else:
        return "Invalid platform. Choose spotify, youtube, or local."

import pyautogui
from livekit.agents import function_tool
from features.explanation import set_last_action


@function_tool()
async def pause_media() -> str:
    pyautogui.press("playpause")
    set_last_action("Paused media playback")
    return "Media paused."


@function_tool()
async def play_media() -> str:
    pyautogui.press("playpause")
    set_last_action("Resumed media playback")
    return "Media playing."


@function_tool()
async def next_media() -> str:
    pyautogui.press("nexttrack")
    set_last_action("Skipped to next media")
    return "Playing next video."


@function_tool()
async def previous_media() -> str:
    pyautogui.press("prevtrack")
    set_last_action("Went to previous media")
    return "Playing previous video."

import pyautogui
from datetime import datetime
from livekit.agents import function_tool
from features.explanation import set_last_action

@function_tool
async def take_screenshot() -> str:
    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    pyautogui.screenshot(filename)
    set_last_action("Took a screenshot")

    return "Screenshot taken successfully."

import pyautogui
from livekit.agents import function_tool
from features.explanation import set_last_action

@function_tool
async def set_volume(level: int) -> str:
    """
    Sets system volume to an approximate percentage (Windows).
    """
    level = max(0, min(level, 100))

    # Step 1: Force volume to zero
    for _ in range(50):
        pyautogui.press("volumedown")

    # Step 2: Raise volume to desired level
    steps = int(level / 2)  # Windows volume step ≈ 2%
    for _ in range(steps):
        pyautogui.press("volumeup")
    set_last_action(f"Set system volume to {level} percent")

    return f"Volume set to {level} percent."


from livekit.agents import function_tool
from features.explanation import set_last_action

@function_tool
async def shutdown_jarvis() -> str:
    """
    Shuts down the Jarvis agent gracefully.
    """
    set_last_action("Shut down Jarvis")
    return "Shutting down Jarvis. Goodbye."
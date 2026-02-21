from livekit.agents import function_tool

LAST_ACTION = ""

def set_last_action(action: str):
    global LAST_ACTION
    LAST_ACTION = action

@function_tool
async def explain_last_action() -> str:
    if not LAST_ACTION:
        return "No recent action to explain."

    return f"I executed the following action: {LAST_ACTION}. I identified the intent and used the appropriate system tool."

from livekit.agents import function_tool
from features.explanation import set_last_action
from memory.memory_store import (
    init_memory, save_memory, get_memory
)

# Initialize DB once
init_memory()


@function_tool()
async def remember_fact(key: str, value: str) -> str:
    """
    Store a long-term fact about the user.
    """
    save_memory(key, value, "fact")
    set_last_action(f"Saved memory: {key}")
    return f"I will remember that {key} is {value}."


@function_tool()
async def recall_fact(key: str) -> str:
    """
    Recall a stored fact.
    """
    value = get_memory(key)
    if not value:
        return f"I don't have any memory about {key}."

    set_last_action(f"Recalled memory: {key}")
    return f"{key} is {value}."

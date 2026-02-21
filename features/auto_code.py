import tempfile
import subprocess
from livekit.agents import function_tool
from features.explanation import set_last_action

@function_tool()
async def open_code_in_notepad(
    code: str,
    language: str
) -> str:
    """
    Open generated code in Notepad.
    """

    lang = language.lower()
    suffix = ".txt"

    if lang in ["python", "py"]:
        suffix = ".py"
    elif lang == "c":
        suffix = ".c"
    elif lang == "cpp":
        suffix = ".cpp"
    elif lang == "java":
        suffix = ".java"

    file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    file.write(code.encode())
    file.close()

    subprocess.Popen(["notepad.exe", file.name])
    
    set_last_action(f"Write code in Notepad")
    return "Code opened in Notepad"


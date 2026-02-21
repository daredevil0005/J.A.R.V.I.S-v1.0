import os
import subprocess
import pygetwindow as gw
import win32gui
import win32con
from livekit.agents import function_tool
from features.explanation import set_last_action

USER = os.getlogin()

# -------------------- APP MAPPINGS --------------------

APP_COMMANDS = {
    # ===== System apps (shell commands) =====
    "notepad": "notepad",
    "calculator": "calc",
    "command prompt": "cmd",
    "control panel": "control",
    "settings": "ms-settings:",
    "paint": "mspaint",

    # ===== Browsers & media =====
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "edge": "msedge",
    "vlc": r"C:\Program Files\VideoLAN\VLC\vlc.exe",

    # ===== Microsoft Office =====
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    "powerpoint": r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",

    # ===== Messaging =====
    "telegram": rf"C:\Users\{USER}\AppData\Roaming\Telegram Desktop\Telegram.exe",
    "whatsapp": [
    "shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App",
    rf"C:\Users\{USER}\AppData\Local\WhatsApp\WhatsApp.exe",
    ],

    # ===== Development tools =====
    "vs code": rf"C:\Users\{USER}\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "powershell": "powershell",

    # ===== Utilities (very demo-friendly) =====
    "task manager": "taskmgr",
    "file explorer": "explorer",
    "calculator classic": "calc",

    # ===== Optional (keep only if installed) =====
    "copilot": rf"C:\Users\{USER}\AppData\Local\Programs\Copilot\Copilot.exe",
}


# -------------------- APP CONTROL --------------------

@function_tool()
async def open_app(app_name: str) -> str:
    app = app_name.lower().strip()

    if app not in APP_COMMANDS:
        return f"I don't know how to open {app_name}"

    command = APP_COMMANDS[app]

    # URI-based apps
    if command.startswith("ms-settings"):
        subprocess.Popen(command, shell=True)
        set_last_action(f"Opened {app_name}")
        return f"Opening {app_name}"

    # Absolute path apps
    if "\\" in command or "/" in command:
        if not os.path.exists(command):
            return f"{app_name} is not installed on this system"
        subprocess.Popen(command)
        set_last_action(f"Opened {app_name}")
        return f"Opening {app_name}"

    # System commands (notepad, calc, etc.)
    subprocess.Popen(command, shell=True)
    set_last_action(f"Opened {app_name}")
    return f"Opening {app_name}"


@function_tool()
async def close_app(app_name: str) -> str:
    app = app_name.lower()

    for title in gw.getAllTitles():
        if app in title.lower():
            win = gw.getWindowsWithTitle(title)[0]
            win.close()
            return f"Closed {title}"
    set_last_action(f"Attempted to close {app_name}, but no window was found.")
    return f"No open window found for {app_name}"


# -------------------- WINDOW CONTROL --------------------

@function_tool()
async def minimize_window() -> str:
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    set_last_action("Minimized the current window.")
    return "Window minimized"


@function_tool()
async def maximize_window() -> str:
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    set_last_action("Maximized the current window.")
    return "Window maximized"


@function_tool()
async def restore_window() -> str:
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    set_last_action("Restored the current window.")
    return "Window restored"


@function_tool()
async def focus_window(app_name: str) -> str:
    app = app_name.lower()

    for title in gw.getAllTitles():
        if app in title.lower():
            win = gw.getWindowsWithTitle(title)[0]
            win.activate()
            return f"Focused {title}"
    set_last_action(f"Attempted to focus {app_name}, but no window was found.")
    return f"No window found for {app_name}"


# -------------------- FOLDER CONTROL --------------------

@function_tool()
async def open_folder(path: str) -> str:
    """
    Open a folder from any drive.
    Example:
    C:/Users
    D:/Projects
    E:/Movies
    """
    if not os.path.exists(path):
        return "Folder path does not exist"

    if not os.path.isdir(path):
        return "Path is not a folder"

    subprocess.Popen(f'explorer "{path}"')
    set_last_action(f"Opened folder {path}.")
    return f"Opened folder {path}"


@function_tool()
async def close_folder() -> str:
    """
    Closes the currently active File Explorer window.
    """
    hwnd = win32gui.GetForegroundWindow()
    class_name = win32gui.GetClassName(hwnd)

    if class_name == "CabinetWClass":
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
        return "Folder window closed"
    set_last_action("Attempted to close a folder window, but no folder window was active.")
    return "No folder window is currently active"

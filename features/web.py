import webbrowser
from livekit.agents import function_tool
from features.explanation import set_last_action

# Common website shortcuts
WEBSITE_MAP = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "wikipedia": "https://www.wikipedia.org",
    "facebook": "https://www.facebook.com",
    "twitter": "https://twitter.com",
    "linkedin": "https://www.linkedin.com",
    "gmail": "https://mail.google.com",
    "instagram": "https://www.instagram.com",
    "chatGPT": "https://chat.openai.com",
}

@function_tool
async def open_website(site: str) -> str:
    site = site.lower().strip()

    # If user says a known website name
    if site in WEBSITE_MAP:
        url = WEBSITE_MAP[site]
    else:
        # Handle cases like "example.com" or "open xyz dot com"
        site = site.replace(" dot ", ".").replace(" ", "")
        if not site.startswith("http"):
            url = f"https://{site}"
        else:
            url = site

    webbrowser.open(url)
    set_last_action(f"Opened website {url}")

    return f"Opening {url}."

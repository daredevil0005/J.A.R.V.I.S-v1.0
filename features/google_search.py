import os
import requests
import logging
from dotenv import load_dotenv
from livekit.agents import function_tool
from datetime import datetime
from features.explanation import set_last_action

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@function_tool
async def google_search(query: str) -> str:
    logger.info(f"Search query received: {query}")

    api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
    search_engine_id = os.getenv("SEARCH_ENGINE_ID")

    if not api_key or not search_engine_id:
        logger.error("Missing GOOGLE_SEARCH_API_KEY or SEARCH_ENGINE_ID.")
        return "Google Search is not configured properly."

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": search_engine_id,
        "q": query,
        "num": 2  # 🔥 Reduced for faster voice response
    }

    logger.info("Sending request to Google Custom Search API...")
    response = requests.get(url, params=params, timeout=5)

    if response.status_code != 200:
        logger.error(
            f"Google API error: {response.status_code} - {response.text}"
        )
        return "There was an error while searching on Google."

    data = response.json()
    results = data.get("items", [])

    if not results:
        logger.info("No search results found.")
        return "No results were found."

    # Voice-friendly formatting
    formatted_results = []
    for i, item in enumerate(results, start=1):
        title = item.get("title", "No title")
        snippet = item.get("snippet", "")
        formatted_results.append(f"{i}. {title}. {snippet}")

        logger.info(f"{i}. {title} - {snippet}")
    set_last_action(f"Searched Google for: {query}")

    return " ".join(formatted_results)


@function_tool
async def get_current_datetime() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


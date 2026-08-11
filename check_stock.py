import os
import requests
from bs4 import BeautifulSoup

URL = "https://backestcg.com.au/collections/palworld-tcg"

response = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

page_text = soup.get_text(" ", strip=True).lower()

keywords = [
    "sleeve",
    "sleeves",
    "sleeve & card set",
    "sleeve and card set",
    "volume 1",
    "vol. 1",
    "vol 1",
    "volume one",
    "ss01",
]

found_keywords = [
    keyword for keyword in keywords
    if keyword in page_text
]

if found_keywords:
    print("🚨 POSSIBLE PALWORLD SLEEVE PRODUCT FOUND!")
    print("Matched:", ", ".join(found_keywords))

    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    message = (
        "🚨 PALWORLD STOCK ALERT! 🚨\n\n"
        "A possible Palworld Sleeve & Card Set has appeared "
        "on BackesTCG!\n\n"
        f"Matched: {', '.join(found_keywords)}\n\n"
        f"🛒 {URL}"
    )

    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    telegram_response = requests.post(
        telegram_url,
        data={
            "chat_id": chat_id,
            "text": message
        },
        timeout=30
    )

    telegram_response.raise_for_status()

    print("✅ Telegram alert sent!")
else:
    print("No matching product found yet.")

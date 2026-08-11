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
    print(URL)
else:
    print("No matching product found yet.")

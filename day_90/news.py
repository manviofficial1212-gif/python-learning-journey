import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = "eaf690451509490894f49122cab11345"

url = "https://newsapi.org/v2/top-headlines"

headers = {
    "X-Api-Key": api_key
}

params = {
    "country": "us"
}

response = requests.get(
    url,
    headers=headers,
    params=params,
    verify=False
)

print(response.status_code)
data = response.json()

print("\n📰 TOP NEWS HEADLINES 📰\n")

for i, article in enumerate(data["articles"], start=1):
    print(f"{i}. {article['title']}")
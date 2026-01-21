import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://books.toscrape.com"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0"
})

response = session.get(url, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.text.strip()
headings = soup.find_all("h1")

with open("scraped_data.txt", "w", encoding="utf-8") as file:
    file.write("Website Title:\n")
    file.write(title + "\n\n")

    file.write("Headings:\n")
    for h in headings:
        file.write(h.text.strip() + "\n")

print("Scraping completed successfully!")

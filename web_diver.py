from bs4 import BeautifulSoup
import requests

# website_2_scrape = requests.get("https://novelfire.net/book/im-the-evil-lord-of-an-intergalactic-empire/chapter-1")

with open("chapter.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")
content = soup.find("div", id="content")

if content is not None:
    print(content.get_text("\n", strip=True))
else:
    print("Could not find the content section")


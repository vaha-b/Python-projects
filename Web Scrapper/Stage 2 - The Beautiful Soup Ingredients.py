# About the project:
# https://hyperskill.org/projects/145?track=2

# Stage description
# https://hyperskill.org/projects/145/stages/782/implement

import json
import requests
from bs4 import BeautifulSoup

r = requests.get(input("Input the URL:\n").lower(), headers={
                 'Accept-Language': 'en-US,en; q=0.5'})
soup = BeautifulSoup(r.content, "html.parser")

if r:
    description = soup.find("div", {"class", "summary_text"}).text.strip()
    data = json.loads(
        "".join(soup.find("script", {"type": "application/ld+json"}).contents))
    movie = {"title": data["name"], "description": description}
    print(movie)
else:
    print("\nInvalid movie page!")

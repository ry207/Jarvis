from bs4 import BeautifulSoup
import requests
import os

def getpapers():
    url  = f"https://nips.cc/virtual/2024/papers.html?filter=titles"
    print(f"searching at: {url}")
    print("-------------------------------------------------------------------")
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    content = soup.find("div", class_="cards row")
    blocks = soup.find_all("li")[64:]

    count = 0

    for block in blocks:
        if count == 20:
            break
        title = block.find('a')
        href = block.find('a').get("href")
        print(f"{title.text}")
        print(f"https://nips.cc/{href}")
        print("----------------------------------")
        count += 1

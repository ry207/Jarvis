from bs4 import BeautifulSoup
import requests
import os

def news():
    url  = f"https://therecord.media/tag/hacking-forum"
    print(f"searching at: {url}")
    print("-------------------------------------------------------------------")
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    content = soup.find("ul", class_="briefs__list")
    blocks = content.find_all('li')
    for block in blocks:
        name = block.find('a')
        href = block.find('a').get("href")
        print(f"{name.text}")
        print(f"Link: https://therecord.media{href}")
        print("----------------------------------")



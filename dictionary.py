from bs4 import BeautifulSoup
import requests
import os

def getdef():
    word = input("Word to search: ")
    url  = f"https://www.merriam-webster.com/dictionary/{word}?src=search-dict-hed"
    print(f"searching at: {url}")

    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    content = soup.find("div", class_="entry-word-section-container")

    wordname = content.find('h1', class_="hword")
    definition = content.find('div', class_="vg-sseq-entry-item")
    definitionfinal = definition.text.replace("\n", " ")

    print("-------------------------------------------------------------------")
    print(f"Word:\t\t{wordname.text}")
    print(f"Definition:\t({definitionfinal})")
    print("-------------------------------------------------------------------")



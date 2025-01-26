from bs4 import BeautifulSoup
import requests
import os

def yaho(search):
    search = search.replace(" ", "+")
    url  = f"https://video.search.yahoo.com/search/video;_ylt=AwrFRzLuZZZnolkEgJRXNyoA;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p={search}&fr2=piv-web&.tsrc=uh3_entertainment_web&fr=uh3_entertainment_web"
    print(f"searching at: {url}")
    print("-------------------------------------------------------------------")
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    content = soup.find("ol")
    blocks = content.find_all('li')
    for block in blocks[:20]:
        title = block.find('h3')
        print(f"Title: {title.text}")
        try:
            m = block.select_one("[data-rurl]\n")
            print("Link: ", m["data-rurl"])
        except:
            print("No link")
        #print(f"Link: {href}")
        print("----------------------------------")



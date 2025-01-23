from bs4 import BeautifulSoup
import requests
import os

def getpage(voice):
    url  = f"https://en.wikipedia.org/wiki/{voice}"
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    page = soup.find('div', class_='mw-body-content')
    print(page)
    try:
        f = open(f"WikiPages/{voice}_wikipage.html", "w")
        f.write(f"Wikipedia page for: {voice}\n\n\n{page}")
        f.close()
        startlh()
    except:
        print("An error may have occured.")

def startlh():
    os.system("python -m http.server 8000 -d WikiPages/")


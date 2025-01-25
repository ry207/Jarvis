from bs4 import BeautifulSoup
import requests
import pyttsx3
import os

engine = pyttsx3.init()

def getstocks():
    url  = f"https://finance.yahoo.com/"
    print(f"searching at: {url}")
    print("-------------------------------------------------------------------")
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    content = soup.find("ul", class_=" dock yf-pmz4k")
    blocks = content.find_all('li')
    for block in reversed(blocks):
        name = block.find('span', class_="longName yf-pt5nkw")
        price = block.find('fin-streamer', class_="last-price yf-pt5nkw")
        percentChange = block.find('fin-streamer', class_="percentChange yf-pt5nkw")
        print(f"{name.text}")
        print(f"${price.text}")
        print(f"{percentChange.text}")
        print("----------------------------------")
    engine.say(f"{name.text} has a price of {price.text} dollars and regular market change of {percentChange.text}")
    engine.runAndWait()


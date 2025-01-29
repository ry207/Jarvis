from bs4 import BeautifulSoup
import requests
import pyttsx3
import os

engine = pyttsx3.init()

def getstocks():
    try:
        url  = f"https://finance.yahoo.com/"
        print(f"searching at: {url}")
        page = requests.get(url).text
        soup = BeautifulSoup(page, "lxml")
        content = soup.find("li", class_="dock-item dockRevealTarget dockRevealTarget-5 yf-1doyjox")
    except:
        print("Check your internet.")



    blocks = content.find_all('li', class_='dock-item primary font-default yf-46ugf5 clickability hover hasSymbolOptions')
    print("----------------------------------")
    for block in blocks:
        name = block.find('span', class_="longName yf-pt5nkw")
        price = block.find('fin-streamer', class_="last-price yf-pt5nkw")
        percentChange = block.find('span', class_="percent-change txt-positive yf-pt5nkw")
        if name != None:
            name = name.text
            print(f"Company: {name}")
        if price != None:
            price = price.text
            print(f"Price: ${price}")
        else:
            print("No price")
        if percentChange != None:
            percentChange = percentChange.text
            print(f"Change: {percentChange}")
        else:
            print("No change")
        print("----------------------------------")
    engine.say(f"{name} has a price of {price} dollars.")
    engine.runAndWait()

getstocks()

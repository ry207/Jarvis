from bs4 import BeautifulSoup
import requests
import pyttsx3
import urllib.request

engine = pyttsx3.init()

def analizevoice(voice):
    # --------------PAGE 1---------------
    url = f"https://en.wikipedia.org/w/index.php?title={voice}&action=info"
    page = requests.get(url).text

    soup = BeautifulSoup(page, "lxml")
    #job_elements = soup.find_all('li')
    table = soup.find('table', class_="wikitable mw-page-info")
    print(f"searching at {url}")
    #for job_element in job_elements:
    categories = table.find_all('tr')
    #for x in categories:
        #print(x.find('p').text)

    url2  = f"https://en.wikipedia.org/wiki/{voice}"
    page2 = requests.get(url2).text
    soup2 = BeautifulSoup(page2, "lxml")
    page2 = soup2.find('div', class_='mw-body-content')
    printable = page2.text
    try:
        desc = categories[14].text
        print(desc[19:])
        engine.say(desc[19:])
        engine.runAndWait()
    except:
        print("An Error Occured.")
        engine.say("An error occured, sir.")
        engine.runAndWait()


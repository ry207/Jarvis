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
    try:
        desc = categories[14].text
        print(desc[19:])
        engine.say(voice)
        engine.runAndWait()
        engine.say(desc[19:])
    except:
        print("An Error Occured.")
        engine.say("An error occured, sir.")



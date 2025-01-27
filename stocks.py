from bs4 import BeautifulSoup
import requests
import pyttsx3
import os

engine = pyttsx3.init()

def getstocks():
    url  = f"https://investing.com/"
    print(f"searching at: {url}")
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    content = soup.find("table", class_="datatable-v2_table__93S4Y dynamic-table-v2_dynamic-table__iz42m datatable-v2_table--mobile-basic__uC0U0 datatable-v2_table--freeze-column__uGXoD datatable-v2_table--freeze-column-first__zMZNN undefined")

    

    blocks = content.find_all('tr')
    for block in reversed(blocks[1:(len(blocks))]):
        tds = block.find_all('td')
        for td in (tds):
            try:
                print(td.text)
            except:
                print("Error")
        name = block.find('td', class_="datatable-v2_cell__IwP1U !h-auto w-full py-2 mdMax:border-r dynamic-table-v2_col-name__Xhsxv !py-2")
        price = block.find('td', class_="datatable-v2_cell__IwP1U dynamic-table-v2_col-other__zNU4A text-right rtl:text-right")
        percentChange = block.find('td', class_="datatable-v2_cell__IwP1U datatable-v2_cell--up__lVyET datatable-v2_cell--bold__cXQUV dynamic-table_col-other__Eu_RC text-right font-bold rtl:text-right")
        print("----------------------------------")
    engine.say(f"{name.text} has a price of {price.text} dollars.")
    engine.runAndWait()

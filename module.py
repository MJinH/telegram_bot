import os
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

def command_list(path):
    files_list = ""
    if os.path.exists(path):
        files = os.listdir(path)
        files.sort()
        for f in files:
            file_path = os.path.join(path,f)
            # check if it is folder
            if os.path.isdir(file_path):
                f = f + " => Folder"
            files_list += f
            files_list += "\n"
    return files_list



def get_weather(location):
    data = defaultdict()
    url = "https://search.yahoo.com/search?p={}+weather".format(location)
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content,"html.parser")
    data["current_location"] = soup.select_one("div.cptn > div.cptn-ctnt > p.txt").text
    data["temperature"] = soup.select_one("div.main-temp > div > span.currTemp").text
    data["temperature"] += soup.select_one("div.main-temp > div > span.deg").text
    data["temperature"] += soup.select_one("div.main-temp > div > span.unit").text
    data["current_cond"] = soup.select_one("div.main-cond > span.condition").text
    print(data)
    return data


def get_coin(coin):
    data = defaultdict()
    url = "https://coinmarketcap.com/currencies/{}/".format(coin)
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content,"html.parser")
    data["price"] = soup.select_one("div.priceValue > span").text
    data["caret_up"] = soup.select_one("div.sc-16r8icm-0 > span.sc-15yy2pl-0 > span.icon-Caret-up")
    data["caret_down"] = soup.select_one("div.sc-16r8icm-0 > span.sc-15yy2pl-0 > span.icon-Caret-down")
    if data["caret_up"]:
        del data["caret_down"]
        del data["caret_up"]
        data["percentage"] = "+" + soup.select_one("span.sc-15yy2pl-0").text
    elif data["caret_down"]:
        del data["caret_down"]
        del data["caret_up"]
        data["percentage"] = "-" + soup.select_one("span.sc-15yy2pl-0").text
    data["rank"] = soup.select_one("div.sc-16r8icm-0 > div.namePillPrimary").text
    return data
     
    
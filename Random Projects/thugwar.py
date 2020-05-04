import requests, json
from time import sleep

def mug_and_buy() :
    URL = "http://stupidstuff.org/thugwar/market.php"

    buy = "buybeer=1600000&buycondoms=&buycrack=&buyweed=1600000&buyguns=3600000&buythugs=1600000&buylowriders=&action=Buy+me+dis+here+stuff&act=buy"

    header_buy = {
        "Host": "stupidstuff.org",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "42",
        "Origin": "http://stupidstuff.org",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "http://stupidstuff.org/thugwar/scout.php",
        "Cookie": "__cfduid=d014bb07426551bdf52297d63890a2c381575935022; PHPSESSID=oc29b9echguelksm0spkq6sqv6",
        "Upgrade-Insecure-Requests": "1"}

    URL = "http://stupidstuff.org/thugwar/crimes.php"

    datas = "turns=1&mugbt=Mug+People%21&act=mug"

    header_mug = {
        "Host": "stupidstuff.org",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "35",
        "Origin": "http://stupidstuff.org",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "http://stupidstuff.org/thugwar/crimes.php",
        "Cookie": "__cfduid=d2ca5f4a93b3b28d5c5b396b2d6a4ae181573973167; PHPSESSID=j1e3gh5dnhump48e11h3vosd76",
        "Upgrade-Insecure-Requests": "1"
    }
    r = requests.post(URL, data = datas, headers = header_mug)
    print(r.status_code, r.reason)
    print(r.text)

    sleep(10)

    r = requests.post(URL, data = buy, headers = header_buy)

    print(r.status_code, r.reason)
    print(r.text)

for i in range(10) :
    mug_and_buy()
    sleep(10)
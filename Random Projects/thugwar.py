import requests, json

URL = "http://stupidstuff.org/thugwar/scout.php"

datas = "turns=60&scoutbt=Scout+for+Hoes&act=scout"
buy = "buybeer=&buycondoms=5000&buycrack=5000&buyweed=&buyguns=&buythugs=&buylowriders=&action=Buy+me+dis+here+stuff&act=buy"
header = {"Host": "stupidstuff.org",
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

r = requests.post(URL, data = buy, headers = header)

r = requests.post(URL, data = datas, headers = header)

print(r.status_code, r.reason)
print(r.text)

# AMC script
# made by asmpro
# date: 11/3/2023
# TG:@asmprotk

import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.vviruslove.com/%D8%AA%D9%81%D8%B9%D9%8A%D9%84-%D9%83%D9%88%D8%AF-airmax-tv-iptv-%D9%85%D8%AF%D8%A9-%D8%A7%D9%84%D8%AD%D9%8A%D8%A7%D8%A9-%D9%85%D8%B4%D8%A7%D9%87%D8%AF%D8%A9-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9")
soup = BeautifulSoup(page.content, "lxml")
mydiv = soup.find("div", {'class': 'post-content-bd'})
mystr = mydiv.find("a", {'style': 'color: #0000ff;'},
                   string="أضغط هنا للحصول على الكود الجديد")
myurl = mystr['href']

page = requests.get(myurl)
soup = BeautifulSoup(page.content, "lxml")
mydiv = soup.find("div", {'class': 'su-button-center'})
mystr = mydiv.find("a", {
    'class': 'su-button su-button-style-default su-button-wide', 'id': 'download'})
myurl = mystr['href']

page = requests.get(myurl, timeout=(5, 10))
soup = BeautifulSoup(page.content, "lxml")
mydiv = soup.find("div", {'class': 'post-content-bd'})
myimg = mydiv.find(
    "img", {"decoding": "async", "sizes": "(max-width: 712px) 100vw, 712px"})
myimg = myimg["src"].split("/")[-1].split(".")[0]

print("\033[31m the code is:\033[31;1;40m", myimg)
print("\n\033[32m AMC by asmpro \033[m")

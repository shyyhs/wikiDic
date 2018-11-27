import requests
from bs4 import BeautifulSoup as sp
import re

url = "https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5"

html = requests.get(url).text
soup = sp(html,"lxml")
print (soup.descandants)

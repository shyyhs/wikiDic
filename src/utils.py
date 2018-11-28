# -*- coding: utf-8 -*-
from globalSetting import *


def cpJa(url): return "http://ja.wikipedia.org"+url
def cpEn(url): return "http://en.wikipedia.org"+url

unicodeType = type(u"例")

# regular expression patterns
urlEngPattern = re.compile(ur"英.*[:：][ ]*([a-zA-z0-9 ]+)[)）]",re.UNICODE)
engPattern = re.compile(ur"英.*[:：][ ]*([a-zA-z0-9 ]+)$", re.UNICODE)

#Output: wiki type, one of these: people organization location company others
def wikiType(soup):
    return "others"

# Input: soup,
# Output: The english translation of the title of the soup if exists else "NONE"
def wikiFindEngWordFromText(soup):
    enWord = "NONE"
    result = urlEngPattern.search(soup.get_text())
    if (result is not None):
        enWord = result.group(1).strip()
        return enWord
    return enWord

def wikiFindEngWordFromUrl(soup):
    enWord = "NONE"
    for link in soup.find_all('a'):
        if (link.get_text() == "English"):
            title = link.get("title")
            if (title is None): continue
            result = engPattern.search(title)
            if (result is not None):
                enWord = result.group(1).strip()
                return enWord
    return enWord

def wikiEnWord(soup):
    enWord = wikiFindEngWordFromText(soup)
    if (enWord == "NONE"):
        enWord = wikiFindEngWordFromUrl(soup)
    return enWord

# Input: soup, Output: Wiki Title
def webTitle(soup): 
    caption = soup.find("h1")
    if (caption is not None):
        return caption.get_text()

# Input:soup, Output: dict{"title":"url"}
def wikiUrlDic(soup):
    urlDic = {}
    for link in soup.find_all('a',href=re.compile("^/wiki/((?!:).)*$")):
        urlDic[link.get('title')] = cpJa(link.get('href'))
    return urlDic

def cookSoup(url):
    html = requests.get(url).text
    soup = sp(html,"lxml")
    return soup

def crawlEntry(sourceUrl,depth,MAX_DEPTH):
    if (depth == MAX_DEPTH): return 
    try: soup = cookSoup(sourceUrl)
    except: return

    urlDic = wikiUrlDic(soup)
    jaWord = webTitle(soup)
    enWord = wikiEnWord(soup)
    wType = wikiType(soup)
    if (enWord == "NONE"): return
    outString = jaWord+','+enWord+','+wType
    outString = outString.encode('utf-8')
    print (outString)
    fileOut.write(outString)
    for subUrl in urlDic.values():
        crawlEntry(subUrl, depth+1, MAX_DEPTH)

if (__name__=="__main__"):
    print ("utils begins")
    url = "https://ja.wikipedia.org/wiki/%E4%BA%AC%E9%83%BD%E6%B0%B4%E6%97%8F%E9%A4%A8"
    url = "https://ja.wikipedia.org/wiki/%E6%A0%AA%E5%BC%8F%E4%BC%9A%E7%A4%BE_(%E6%97%A5%E6%9C%AC)"
    crawlEntry(url,0,1)

if (__name__!="__main__"):
    print ("utils loaded")




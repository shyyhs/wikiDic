# -*- coding: utf-8 -*-
from globalSetting import *

def cpJa(url): return "http://ja.wikipedia.org"+url
def cpEn(url): return "http://en.wikipedia.org"+url

# Return a dict{"title":"url"}
# Return the title and english translation
def urlLst(url):
    html = requests.get(url).text
    soup = sp(html,"lxml")
    #1. the urlDic
    urlDic = {}
    for href in soup.find_all('a',href=re.compile("^/wiki/((?!:).)*$")):
        urlDic[href.get('title')] = cpJa(href.get('href'))
    #2. the title 
    jaWord = soup.find("h1").get_text()
    #3. english translation if any
    unicodeType = type(u"例")
    pattern = re.compile(ur"英.*[:：]([a-zA-z0-9 ]+)[)）]",re.UNICODE)
    abstract = soup.find("div", {"id":"mw-content-text"}).find_all("p")
    for sentence in abstract:
        sentText = sentence.get_text()
        if (type(sentText)!=unicodeType):
            sentText= unicode(sentText,'utf-8')
        result = pattern.search(sentText)
        if (result is not None):
            enWord = result.group(1).strip()
            break;
    """
    #caption = abstract.find("caption", itemprop="name")
    st = "英: Japan Freight Railway Company）"
    st = unicode(st, 'utf-8')
    result = pattern.search(st)
    if (result is not None): print (result.group(1).strip())
    """
    return urlDic, jaWord, enWord

    


if (__name__=="__main__"):
    print ("utils begins")
    url = "https://ja.wikipedia.org/wiki/%E4%BA%AC%E9%83%BD%E6%B0%B4%E6%97%8F%E9%A4%A8"
    urlDic, jaWord, enWord = urlLst(url)
    print (jaWord, enWord)

if (__name__!="__main__"):
    print ("utils loaded")



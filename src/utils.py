# -*- coding: utf-8 -*-
from globalSetting import *
from hashing import *
from wikiType import wikiType


cpJa = lambda url: "http://ja.wikipedia.org"+url
cpEn = lambda url: "http://en.wikipedia.org"+url
unicodeType = type(u"例")

# regular expression patterns
textEngPattern = re.compile(ur"英.*[:：][\s]*([a-zA-z0-9 ]+)[)）]",re.UNICODE)
urlEngPattern = re.compile(ur"英.*[:：][\s]*([a-zA-z0-9 ]+)$", re.UNICODE)
bracketPattern = re.compile(ur"[(（\[].*[)）\]]", re.UNICODE)
emptyString = ur''

# delete brackets(also delete the context in the brackets) around a word
# To prevent these kind of words: 京都（日本） kyoto[1] -> 京都　kyoto
delBrackets = lambda s: re.sub(bracketPattern,emptyString,s)

#Output: wiki type, one of these: people organization location company others
def wikiType(soup):
    return "others"

# Output: The english translation of the title of the soup if exists else "NONE"
def wikiFindEngWordFromText(soup):
    enWord = "NONE"
    result = textEngPattern.search(soup.get_text())
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
            result = urlEngPattern.search(title)
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
    else: return "NONE"

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

def wikiProcess(sourceUrl):
    """
    return 0 if NG
    else return output string
    """
    try: soup = cookSoup(sourceUrl)
    except: return None,None
    #Output things
    jaWord = webTitle(soup)
    enWord = wikiEnWord(soup)
    if (checkHash(sourceUrl,jaWord)==0): return None,None#exit when visited already
    if (jaWord=="NONE"): return None,None#no title, not wiki site
    #if (enWord == "NONE"): return
    wType = wikiType(soup)

    #Prepare for output
    jaWord = delBrackets(jaWord.strip())
    enWord = delBrackets(enWord.strip())
    outString = jaWord+','+enWord+','+wType+'\n'
    outString = outString.encode('utf-8')
    return outString,soup

if (__name__=="__main__"):
    print ("utils begins")
    url = "https://ja.wikipedia.org/wiki/%E4%BA%AC%E9%83%BD%E6%B0%B4%E6%97%8F%E9%A4%A8"
    url = "https://ja.wikipedia.org/wiki/%E6%A0%AA%E5%BC%8F%E4%BC%9A%E7%A4%BE_(%E6%97%A5%E6%9C%AC)"
    crawlEntry(url,0,1)

if (__name__!="__main__"):
    print ("utils loaded")




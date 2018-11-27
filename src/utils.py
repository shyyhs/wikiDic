from globalSetting import *

def cpU(url): return "http://ja.wikipedia.org"+url

def urlLst(url):
    dic = {}
    html = requests.get(url).text
    soup = sp(html,"lxml")
    for href in soup.find_all('a',href=re.compile("^/wiki/((?!:).)*$")):
        dic[href.get('title')] = href.get('href')
    return dic

    


if (__name__=="__main__"):
    print ("utils begins")
    url = "https://ja.wikipedia.org/wiki/%E4%BA%AC%E9%83%BD%E6%B0%B4%E6%97%8F%E9%A4%A8"
    urlDic = urlLst(url)
    

if (__name__!="__main__"):
    print ("utils loaded")



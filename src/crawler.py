from globalSetting import *
from utils import *


#These should be put the in globalVar but it's a little special
HASHN = 1000007
hashT = [0]*max((HASHN+1),MAX_PAIR*3)
def hash(url):
    h=1
    for i in url: h=(h*ord(i))%HASHN
    return h

def logSetting():
    logging.basicConfig(
        filename = logFileName,
        filemode = 'a+',
        format = "%(asctime)s-%(levelname)s: %(message)s",
        datefmt = "%y/%m/%d_%H:%M:%S",
        level = logging.DEBUG
    )
    logging.info("logging available")

def cookSoup(url):
    html = requests.get(url).text
    soup = sp(html,"lxml")
    return soup

pairNum=0
def crawlEntry(sourceUrl,PAIR_LIMIT):
    h = hash(sourceUrl)
    if (hashT[h]): return
    hashT[h]=1

    global pairNum
    if (pairNum > PAIR_LIMIT): return

    try: soup = cookSoup(sourceUrl)
    except: return

    #Output things
    urlDic = wikiUrlDic(soup)
    jaWord = webTitle(soup)
    enWord = wikiEnWord(soup)
    wType = wikiType(soup)

    #Prepare for output
    if (enWord == "NONE"): return
    jaWord = delBrackets(jaWord.strip())
    enWord = delBrackets(enWord.strip())
    outString = jaWord+','+enWord+','+wType+'\n'
    outString = outString.encode('utf-8')
    #Output
    print (outString)
    fileOut.write(outString)
    pairNum+=1

    #Recursively crawl
    for subUrl in urlDic.values():
        crawlEntry(subUrl,PAIR_LIMIT)

def crawl(firstUrl=defaultUrl, PAIR_LIMIT=MAX_PAIR):
    pairNum=0
    crawlEntry(firstUrl,10)

if (__name__=="__main__"):
    print ("clawler begins")
    print ("---------------------------------")
    logSetting()    
    crawl()

    



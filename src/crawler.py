from globalSetting import *
from utils import *

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
    global pairNum
    pairNum+=1
    if (pairNum == PAIR_LIMIT): return

    try: soup = cookSoup(sourceUrl)
    except: return

    #Output things
    urlDic = wikiUrlDic(soup)
    jaWord = webTitle(soup).strip()
    enWord = wikiEnWord(soup).strip()
    wType = wikiType(soup)
    #Prepare for output
    if (enWord == "NONE"): return
    outString = jaWord+','+enWord+','+wType+'\n'
    outString = outString.encode('utf-8')
    #Output
    print (outString)
    fileOut.write(outString)

    #Recursively crawl
    for subUrl in urlDic.values():
        crawlEntry(subUrl,PAIR_LIMIT)

def crawl(firstUrl=defaultUrl, PAIR_LIMIT=MAX_PAIR):
    pairNum=0
    crawlEntry(firstUrl,PAIR_LIMIT)

if (__name__=="__main__"):
    print ("clawler begins")
    print ("---------------------------------")
    logSetting()    
    crawl()

    



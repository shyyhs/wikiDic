from globalSetting import *
from utils import *
from hashing import *

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
    """
    There're many 'return's to speedup
    """
    global pairNum
    if (pairNum > PAIR_LIMIT): return
    try: soup = cookSoup(sourceUrl)
    except: return

    #Output things
    jaWord = webTitle(soup)
    enWord = wikiEnWord(soup)
    if (checkHash(sourceUrl,jaWord)==0): return #exit when visited already
    if (jaWord=="NONE"): return #no title, not wiki site
    #if (enWord == "NONE"): return
    wType = wikiType(soup)

    #Prepare for output
    jaWord = delBrackets(jaWord.strip())
    enWord = delBrackets(enWord.strip())
    outString = jaWord+','+enWord+','+wType+'\n'
    outString = outString.encode('utf-8')
    #Output
    print (outString)
    fileOut.write(outString)
    #Recursively crawl
    pairNum+=1
    if (pairNum%10000==0): hashSave()
    urlDic = wikiUrlDic(soup)
    for subUrl in urlDic.values(): crawlEntry(subUrl,PAIR_LIMIT)

def crawl(firstUrl=defaultUrl, PAIR_LIMIT=MAX_PAIR):
    pairNum=0
    crawlEntry(firstUrl,10)

if (__name__=="__main__"):
    print ("clawler begins")
    print ("---------------------------------")
    logSetting()

    continueFlag = 0
    preStatusFilePath = statusFileName
    if (continueFlag == 1):
        print ("Load the previous search status")
        hashLoad(preStatusFilePath)
    crawl()

    



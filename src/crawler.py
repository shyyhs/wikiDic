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

def crawlEntry(sourceUrl):
    printFlag=0
    outString,soup = wikiProcess(sourceUrl)
    if (soup == None): return None,0
    if (outString is not None): 
        print (outString)
        fileOut.write(outString)
        printFlag=1
    return wikiUrlDic(soup),printFlag

def crawl(firstUrl=defaultUrl, PAIR_LIMIT=MAX_PAIR):
    pairNum = 0
    urlQue.put(firstUrl)
    while (not urlQue.empty()):
        urlDic,pairAdd = crawlEntry(urlQue.get())
        if (urlDic==None): continue
        pairNum+= pairAdd
        if (pairNum>=MAX_PAIR): break
        if (pairNum%10000==0): hashSave()
        for url in urlDic.values():
            if (not urlQue.full()):
                urlQue.put(url)


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

    



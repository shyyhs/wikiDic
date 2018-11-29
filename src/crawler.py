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

pairNum=0
def crawlEntry(sourceUrl,PAIR_LIMIT):
    """
    There're many 'return's to speedup
    """
    global pairNum
    if (pairNum > PAIR_LIMIT): return
    outString,soup = wikiProcess(sourceUrl)
    if (outString == None): return
    # Output
    print (outString)
    fileOut.write(outString)
    #Recursively crawl
    pairNum+=1
    if (pairNum%10000==0): hashSave()
    urlDic = wikiUrlDic(soup)
    for subUrl in urlDic.values(): crawlEntry(subUrl,PAIR_LIMIT)

def crawl(firstUrl=defaultUrl, PAIR_LIMIT=MAX_PAIR):
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

    



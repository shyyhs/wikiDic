from globalSetting import *
from utils import *
from hashing import *
from resumer import *

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
        with open(outFileName,'a') as fileOut:
            fileOut.write(outString)
        printFlag=1
    return wikiUrlDic(soup),printFlag

def crawl():
    if (urlQue.empty()==True): urlQue.put(defaultUrl)

    pairNum = 1
    while (not urlQue.empty()):
        nowUrl = urlQue.get()
        urlDic,pairAdd = crawlEntry(nowUrl)
        if (urlDic==None): continue
        pairNum+= pairAdd
        if (pairNum>MAX_PAIR): break
        for url in urlDic.values():
            url = re.sub(linkRedundantPattern,'',url)
            if (not urlQue.full()):
                urlQue.put(url)
        if ((pairAdd==1) and pairNum%SAVE_ITER==0): statusSave()
    statusSave()


if (__name__=="__main__"):
    print ("clawler begins")
    print ("---------------------------------")
    logSetting()
    preStatusFilePath = statusFileName
    statusLoad(preStatusFilePath)
    crawl()

    



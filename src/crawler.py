from globalSetting import *

def logSetting():
    logging.basicConfig(
        filename = logFileName,
        filemode = 'a+',
        format = "%(asctime)s-%(levelname)s: %(message)s",
        datefmt = "%y/%m/%d_%H:%M:%S",
        level = logging.DEBUG
    )
    logging.info("logging available")

if (__name__=="__main__"):
    print ("clawler begins")
    logSetting()    



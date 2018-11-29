import os
import sys
import time
import Queue
import logging

import requests
from bs4 import BeautifulSoup as sp
import re
import lxml

# Time
localtime = time.asctime(time.localtime(time.time()))
month, day = localtime.split()[1:3]

# Working dir
workDir = "../data/"
outFileName = workDir + "wiki_properNoun.ja-en.mix"
logFileName = workDir + month+day+".log"
statusFileName = workDir + "status.txt"
if (os.path.exists(workDir)==False): os.mkdir(workDir)

#The output file
fileOut = open(outFileName, "a+")

#defualt url
defaultUrl = "https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC"
defaultUrl = "https://ja.wikipedia.org/wiki/%E8%8F%B1%E5%9E%A3%E5%BB%BB%E8%88%B9"
defaultUrl = "https://ja.wikipedia.org/wiki/%E9%95%B7%E5%B0%BE%E7%9C%9F"
MAX_DEP = 2
MAX_PAIR = 100
HASHN = 1000007
MAX_QUE = 1000000
urlQue = Queue.Queue(MAX_QUE)



if (__name__=="__main__"):
    print("globalSetting Test begins.")

if (__name__!="__main__"):
    print ("globalSetting loaded.")

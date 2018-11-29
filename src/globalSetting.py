import os
import sys
import time
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
statusFileName = wordDir + "status.txt"
if (os.path.exists(workDir)==False): os.mkdir(workDir)

#The output file
fileOut = open(outFileName, "a+")

#defualt url
defaultUrl = "https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC"
MAX_DEP = 2
MAX_PAIR = 100



if (__name__=="__main__"):
    print("globalSetting Test begins.")

if (__name__!="__main__"):
    print ("globalSetting loaded.")

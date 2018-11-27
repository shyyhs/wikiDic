import os
import sys
import time
import logging
import requests
from bs4 import BeautifulSoup as sp
import re

# Time
localtime = time.asctime(time.localtime(time.time()))
month, day = localtime.split()[1:3]

# Working dir
workDir = "../data/"
outFileName = workDir + "wiki_properNoun.ja-en.mix"
logFileName = workDir + month+day+".log"
if (os.path.exists(workDir)==False): os.mkdir(workDir)

#The output file
fileOut = open(outFileName, "a+")


if (__name__=="__main__"):
    print("globalSetting Test begins.")

if (__name__!="__main__"):
    print ("globalSetting loaded.")

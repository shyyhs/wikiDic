# -*- coding: utf-8 -*-
from globalSetting import *

def feature(soup):
    featureDic = {}
    text = soup.get_text()

    
def locationType(soup):
    return 1

def organizationType(soup):
    return 1

def companyType(soup):
    return 1

def peopleType(soup):
    return 1

def wikiType(soup):
    if (locationType(soup)): return "location"
    if (organizationType(soup)): return "organization"    
    if (companyType(soup)): return "company"
    if (peopleType(soup)): return "people"
    return "others"


def repl(matchobj):
    if (matchobj.group(0)=='A'): return 'B'

if (__name__=="__main__"):
    print ("Test Begins")
    ts = re.sub(ur"[(（\[].*[)）\]]",ur'',ur"dkfdls[1]")
    print (ts)

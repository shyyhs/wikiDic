# -*- coding: utf-8 -*-
from globalSetting import *

HASHN = 1000007
hashU = [0]*max((HASHN+1),MAX_PAIR*3)
hashW = [0]*max((HASHN+1),MAX_PAIR*3)

# double hash
def hash(s):
    h=1
    for c in s: h=(h*ord(c))%HASHN
    return h

def checkHash(url,word):
    ht = hash(url)
    hw = hash(Word)
    if (hashU[ht]==1 and hashW[hw]==1): return 0
    hashU[ht]=1
    hashW[hw]=1
    return 1

def hashSave():
    stFile = open(statusFileName,'w+')

if (__name__=="__main__"):
    print ("hash tesing")
    print (hash(u'日本語'))


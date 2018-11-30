# -*- coding: utf-8 -*-
from globalSetting import *

HASHN = 1000007
hashU = [0]*(HASHN+1)
hashW = [0]*(HASHN+1)

# double hash
def hash(s):
    h=1
    for c in s: h=(h*ord(c))%HASHN
    return h

def checkHash(url,word):
    ht = hash(url)
    hw = hash(word)
    if ((hashU[ht]==1) and (hashW[hw]==1)): return 0
    hashU[ht]=1
    hashW[hw]=1
    return 1

if (__name__=="__main__"):
    print ("hash tesing")
    hashU[1] = 1
    hashU[10000] = 1
    hashW[0] = 1
    hashW[HASHN] = 1
    hashSave()
    hashLoad()


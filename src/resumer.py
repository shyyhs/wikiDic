# -*- coding: utf-8 -*-
from globalSetting import *
from hashing import *
from utils import *
def statusSave():
    print ("status saved(dont worry, this will not write to the dict)")
    with open(statusFileName,'w') as stFile:
        stFile.write(str(sum(hashU))+"\n")
        for i in range(len(hashU)):
            if (hashU[i]): stFile.write(str(i)+"\n")
        stFile.write(str(sum(hashW))+"\n")
        for i in range(len(hashW)):
            if (hashW[i]): stFile.write(str(i)+"\n")
        outUrlN = min(100,urlQue.qsize())
        stFile.write(str(outUrlN)+"\n")
        for i in range(outUrlN):
            tu = urlQue.get().encode('UTF-8')
            if (emptyLinePattern.search(tu) is None):
                stFile.write(tu+"\n")
                urlQue.put(tu)

def statusLoad(statusFileName=statusFileName):
    if (os.path.exists(statusFileName)): 
        if (os.path.getsize(statusFileName)):
            with open(statusFileName,'r') as stFile:
                urlN = int(stFile.readline())
                for i in range(urlN):
                    index = int(stFile.readline())
                    hashU[index] = 1
                wordN = int(stFile.readline())
                for i in range(wordN):
                    index = int(stFile.readline())
                    hashW[index] = 1
                urlLN = int(stFile.readline())
                for i in range(urlLN):
                    if (not urlQue.full()):
                        nowUrl = stFile.readline().strip()
                        if (not emptyLinePattern.search(nowUrl)):
                            urlQue.put(nowUrl)
    if (urlQue.empty()==True): urlQue.put(defaultUrl)


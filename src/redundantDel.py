from globalSetting import *
"""
There are some japanese words which has more than one wiki link.
So you can use this to delete the redundant if needed.
"""

totalRedundantNumber = 0
lineNum =0
dic={}

outFile = open(outFileNoRedun,'w')
with open(outFileName,'r') as inFile:
    while (1):
        line = inFile.readline().decode('utf-8').strip()
        if (line==''): break
        lineNum+=1
        jaWord, enWord, cate = line.split(',')
        if (dic.get(jaWord) is None):
            dic[jaWord] = enWord
            outString = jaWord+','+enWord+','+cate+'\n'
            outFile.write(outString.encode('utf-8'))
        else:
            totalRedundantNumber+=1

print ("There are {} redundant lines(and deleted already)".format(totalRedundantNumber))
outFile.close()


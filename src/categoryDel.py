import sys
sys.path.append('../')
from globalSetting import *
"""
The category is not precise, so you almost need to remove them.
If you want to tag the category, please use juman++:
http://nlp.ist.i.kyoto-u.ac.jp/index.php?JUMAN++
"""


outFile = open(outFileNoCate,'w')
inFile = open(outFileNoRedun,'r')
while (True):
    line = inFile.readline().decode('utf-8').strip()
    if (line==''): break
    wordLst = line.split(',')
    jaWord,enWord,cate = wordLst[0],','.join(wordLst[1:-1]),wordLst[-1]
    outString = jaWord+','+enWord+'\n'
    outString = outString.encode('utf-8')
    outFile.write(outString)

inFile.close()
outFile.close()

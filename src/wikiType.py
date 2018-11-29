# -*- coding: utf-8 -*-
from globalSetting import *
from utils import *

fL=[0]*4
fL[0] = [u"都道府県",u"人口",u"人口密度",u"地方",u"番地",u"位置",u"地理",u"自然",u"歴史",u"面積",u"〒"]
fL[1] = [u"盟",u"活動",u"目[標的]",u"議員",u".立日",u"設立",u"協会",u"組織",u"組合",u"連合"]    
fL[2] = [u"業種",u"法人番号",u"事業内容",u"資本金",u"売上高",u"従業員数",u"子会社",u"設立",u"事業所",u"店舗"]
fL[3] = [u"人物",u"略歴",u"入職",u"生まれ",u"経歴",u"歳",u"生誕",u"長",u"務め",u"受賞"]
lenF=[len(fi) for fi in fL]

def featureScore(soup):
    s = []
    text = soup.get_text()
    for i in range(4):
        s.append(sum([(re.search(c,text)!=None) for c in fL[i]]))
    return s

def wikiType(soup):
    s= featureScore(soup)
    if (not any(s)): return "others"
    index = s.index(max(s))
    if (index==2): return "company"
    if (index==1): return "organization"
    if (index==3): return "people"
    if (index==0): return "location"

def repl(matchobj):
    if (matchobj.group(0)=='A'): return 'B'

if (__name__=="__main__"):
    print ("Test Begins")
    locationUrl = "https://ja.wikipedia.org/wiki/%E9%B3%A5%E5%8F%96%E5%B8%82"
    peopleUrl = defaultUrl
    soup = cookSoup(peopleUrl)
    print (wikiType(soup))
    #ts = re.sub(ur"[(（\[].*[)）\]]",ur'',ur"dkfdls[1]")

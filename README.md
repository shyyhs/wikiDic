# wikiDic
---
## Basic Part Done

## Description:
* A crawling system automatically crawls JapaneseWiki while extract "Japanese-English-category" items in to a **dictionary**
* The Proper noun essential to the translation task but remains a hard bone, so it will be fine with a good dictionary(knowledge base)
* Here's some samples(The translation is prefect but the tags are only for reference)
---
有馬朗人,Akito Arima,people  
国際標準名称識別子,International Standard Name Identifier,organization  
澤柳政太郎,Masataro Sawayanagi,organization  
日本学士院,The Japan Academy,location  
吉見俊哉,Shunya Yoshimi,people  
情報処理学会,IPSJ,organization  
向坊隆,Takashi Mukaibo,people  
金出武雄,Takeo Kanade,people  
蓮實重彦,Shigehiko Hasumi,people  

## Features:
0. All things automatically Done.
1. Automatically crawl.
2. Crawl the whole Japanese Wikipedia
3. Find the english translation automatically.
4. Resume from break-point automatically.
5. Multithreads(Not yet)

## Usage:
$pip install beautifulsoup4
$python crawler.py

## Some useful tools:
1. Delete the redundant words: $ python redundantDel.py
2. Delete the categories tag(because they are unprecise): $ python categoryDel.py
3. If you want to tag the category(people,location or others), please use [juman++](http://nlp.ist.i.kyoto-u.ac.jp/index.php?JUMAN++)

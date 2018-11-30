# -*- coding: utf-8 -*-
from globalSetting import *
# Play regular expressions here, just tests

text= ur"略語（りゃくご。en: dsfkkljs 英xx語：abb -rev- ia -tion   ,dfkjls）とは、ある語の一部を"
textEngPattern = re.compile(ur"[(（].{0,20}?英.{0,5}?[:：].{0,2}?([a-zA-Z- ]+).{0,25}?[)）]",re.UNICODE)
g = textEngPattern.search(text)
if (g is not None): print (g.group(1).strip())

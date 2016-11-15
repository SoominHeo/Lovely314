from bs4 import BeautifulSoup
import re
from unicodedata import name
from nltk import sent_tokenize, word_tokenize, pos_tag

import copy
import time
import datetime
import codecs


a = [[1,3],[3,5],[5,8],[12,15],[16,13]]
kor = []
eng = []
for x in range(len(a)-1):
    if(a[x+1][0]-a[x][0] == a[x+1][1]-a[x][1]):
        kor.append([a[x][0],a[x+1][0]])
        eng.append([a[x][1],a[x+1][1]])

x=0
while 1:
    if x>=len(kor)-1:
        break
    else:
        if(kor[x+1][0]==kor[x][1]):
            kor[x+1][0]==kor[x][0]
            kor.pop(x)
        else:
            x=x+1


while 1:
    if x>=len(eng)-1:
        break
    else:
        if(eng[x+1][0]==eng[x][1]):
            eng[x+1][0]==eng[x][0]
            eng.pop(x)
        else:
            x=x+1

print(kor)
print(eng)



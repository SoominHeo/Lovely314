# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from unicodedata import name
from nltk import sent_tokenize
import time
import copy

#csv1=open("jaccard_attribute.csv"."w")

def jaccard(kor, eng):

    deno=0
    numer=0
    aver=0

    tmp_d=[]
    tmp_k=[]

    #중복없는 kor
    for kk in range(len(kor)):
        if kor[kk]:
            if kor[kk][0]==' ':
                kor[kk]=str(kor[kk]).replace(' ','')
                
            if kor[kk] not in tmp_k:
                tmp_k.append(kor[kk])
        else:
            continue
    
    #deno 갯수
    tmp_d=copy.deepcopy(tmp_k)
    for ee in range(len(eng)):
        
        if eng[ee]:
            '''
            if eng[ee][0]==' ':
                eng[ee]=str(eng[ee]).replace(' ','')
            '''
            if eng[ee] not in tmp_k:
                tmp_d.append(eng[ee])
        else:
            continue

    
    deno=len(tmp_d)

    
    for x in tmp_k:
        if x=='':
            continue
        
        for y in eng:
            if y=='':
                continue
            
            elif x==y:
                numer=numer+1
                break
                
    if deno==0:
        return 0.0
    else:
      
        aver=numer/deno
        return aver


#def matching(aver):

i=0

while i<= 10:
    print()
    print("[",str(i),"] article")
    f_kor=open("ko_num/num/"+str(i)+".kor.txt","r",encoding='UTF8')
    f_eng=open("en_num/"+str(i)+".txt","r",encoding='UTF8')
    

    ko=f_kor.readlines()
    en=f_eng.readlines()

    
    for ee in range(len(en)):
        tmp=str(en[ee]).split(']')
        if tmp[0]=='\n':
            continue
            
        en[ee]=tmp[1]
    
    for x in range(len(ko)):
        
        if ko[x]=='' or ko[x]=='\n':
            continue
        k=str(ko[x]).replace(' \n','')
        k=k.split(',')
        if k==['']:
            continue
        for y in range(len(en)):
            if en[y]=='' or en[y]=='\n':
                continue

            
            e=str(en[y]).replace(' \n','')
            e=e.split(',')

            for ee in range(len(e)):
                if e[ee]:
                    if e[ee][0]==' ':
                        e[ee]=str(e[ee]).replace(' ','')

            if e==['']:
                continue
            
            ##########여기서 함수 돌리면 됩니다. 여기부터는 한글, 영어에서 빈라인을 취급하지 않습니다. 아래는 어떻게 넘어가는지 확인용 프린트 
            print("e:",e)
            print("k:",k)

            aver=jaccard(k,e)
            if aver!=0.0:
                print("[ kor",x+1," -- eng",y+1,"]"," jaccard: "+str(aver))
                
     
    i=i+1

            


    

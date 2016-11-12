
from bs4 import BeautifulSoup
import re
from unicodedata import name
from nltk import sent_tokenize, word_tokenize, pos_tag

import copy
import time
import datetime
import codecs

cs = open("attribute.csv","w")

def jj(k,e):
    k_tmp = []
    e_tmp = []

    s_k = k.split(', ')
    s_e = e.split(', ')

    for x in range(len(s_k)):
        if(s_k[x]==''):
            continue
        k_tmp.append(s_k[x])

    for y in range(len(s_e)):
        if(s_e[y]==''):
            continue
        e_tmp.append(s_e[y])

    tmp = copy.deepcopy(k_tmp)
    for x in range(len(e_tmp)):
        chk=0
        for y in range(len(tmp)):
            if(tmp[y]==e_tmp[x]):
                chk=1
        if(chk==0):
            tmp.append(e_tmp[x])


    kyo = []
    for x in range(len(k_tmp)):
        for y in range(len(e_tmp)):
            if(k_tmp[x]==e_tmp[y]):
                kyo.append(k_tmp[x])
                break;

    if(len(tmp)!=0):
        return float(len(kyo))/float(len(tmp))
    else:
        return 0

def seq(i):

    arr_k =[]

    arr_eng=[]

    f = open("./6/"+str(i)+".kor.txt","rU")
    cnt=0
    while 1:
        s = f.readline()
        a = s[0:-1]
    
        if(s=="\n"):
            cnt=cnt+1
            continue;

        tmp = a.split(', ')
        if(len(tmp)==2 and tmp[0]=="1"):
            cnt=cnt+1
            continue;
        arr_k.append([a,cnt])
        cnt=cnt+1
        if not s:
            break;

    f = open("./7/"+str(i)+".txt","rU")
    cnt=0
    while 1:
        s = f.readline()
        a = s[0:-1]
        
        if(s=="\n"):
            cnt=cnt+1
            continue;
        tmp = a.split(', ')
        if(len(tmp)==2 and tmp[0]=="1"):
            cnt=cnt+1
            continue;
        arr_eng.append([a,cnt])
        cnt=cnt+1
        if not s:
            break;


    arr_k.pop(len(arr_k)-1)
    arr_eng.pop(len(arr_eng)-1)
    for x in arr_k:
        print(x)
    print("=============")
    for x in arr_eng:
        print(x)

    sd_k = []
    sd_e = []
    print("!!!!!!!!!!!!!!")
    for x in range(len(arr_k)):
        for y in range(len(arr_eng)):
            print(arr_k[x][0])
            print(arr_eng[y][0])
            print(jj(arr_k[x][0],arr_eng[y][0]))
            if(jj(arr_k[x][0],arr_eng[y][0])>=0.5 and x!=len(arr_k)-1 and y != len(arr_eng)-1):
                if(jj(arr_k[x+1][0],arr_eng[y+1][0])>=0.5):
                    dif_kor_line = arr_k[x+1][1]-arr_k[x][1]
                    dif_eng_line = arr_eng[y+1][1]-arr_eng[y][1]
                    if(dif_kor_line==dif_eng_line):
                        print("KOR")
                        print(arr_k[x])
                        print(arr_k[x+1])
                        sd_k.append([arr_k[x][1],arr_k[x+1][1]])
                        print("ENG")
                        print(arr_eng[y])
                        print(arr_eng[y+1])
                        sd_e.append([arr_eng[y][1],arr_eng[y+1][1]])

    print(sd_k)
    print(sd_e)
    ss = 0

    x=0
    while 1:
    #for x in range(len(sd_k)-1):
        if x>=len(sd_k)-1:
            break
        else:
            if(sd_k[x+1][0]==sd_k[x][1]):
                sd_k[x+1][0]=sd_k[x][0]
                sd_k.pop(x)
            else:
                x=x+1
    
    print(sd_k)
    x=0
    while 1:
        #for x in range(len(sd_k)-1):
        if x>=len(sd_e)-1:
            break;
        else:
            if(sd_e[x+1][0]==sd_e[x][1]):
                sd_e[x+1][0]=sd_e[x][0]
                sd_e.pop(x)
            else:
                x=x+1

    print(sd_e)

    '''
    for x in range(len(arr_k)):
        for y in range(len(arr_eng)):
            chk=0
            chk_2=0
            for z in range(len(sd_k)):
                if(arr_k[x][1]>=sd_k[z][0] and arr_k[x][1]<=sd_k[z][1]):
                    chk=1
                    break;
            for z in range(len(sd_e)):
                if(arr_eng[y][1]>=sd_e[z][0] and arr_eng[y][1]<=sd_e[z][1]):
                    chk_2=1
                    break;
            if(chk==1 and chk_2==1):
                cs.write("kor"+str(arr_k[x][1])+"--eng"+str(arr_eng[y][1])+",0.3\n")
            else:
                cs.write("kor"+str(arr_k[x][1])+"--eng"+str(arr_eng[y][1])+",0.0\n")
    '''
    f_en = open("./new/new_en/"+str(i)+".eng.txt","rU")
    f_ko = open("./new/new_kr/"+str(i)+".kor.txt","rU")
    f_total = open("./total/total"+str(i)+".txt","w")

    i_ko = 0
    k___=0
    while 1:
        if(k___==len(sd_k)):
            break;
        if(len(sd_k)==0):
            break;

        if(i_ko==sd_k[k___][0]):
            while 1:
                f_total.write(f_ko.readline())
                if(i_ko==sd_k[k___][1]):
                    break;
                i_ko=i_ko+1
            k___=k___+1
            if(k___==len(sd_k)-1):
                break;
        f_ko.readline()
        i_ko=i_ko+1

    i_en = 0
    e___=0
    while 1:
        print(len(sd_e))
        if(e___==len(sd_e)):
            break;
        if(len(sd_e)==0):
            break;


        if(i_en==sd_e[e___][0]):
            while 1:
                print("i "+ str(i_en))
                print("k__ " + str(e___))
                f_total.write(f_en.readline())
                if(i_en==sd_e[e___][1]):
                    break;
                i_en=i_en+1
            e___=e___+1
            if(e___==len(sd_e)-1):
                break;
        f_en.readline()
        i_en=i_en+1

    f_en.close()
    f_ko.close()
    f_total.close()
    f.close()


i=0
while i<=10:
    cs.write(str(i)+"article\n")
    print("\t"+str(i))
    seq(i)
    i=i+1

cs.close()

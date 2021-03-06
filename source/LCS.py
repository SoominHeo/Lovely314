from unicodedata import name
import copy
import re
from unicodedata import name
from nltk import sent_tokenize, word_tokenize, pos_tag
import copy
import time
import datetime
import codecs

cnt=0
LCStable=[]
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

def jaccard(kor, eng):
    deno=0
    numer=0
    aver=0

    tmp_d=[]
    tmp_k=[]
    

    if kor=='\n' or eng=='\n':
        return 0.0

    for kk in range(len(kor)):
        if kor[kk]:
            if kor[kk] not in tmp_k:
                tmp_k.append(kor[kk])
        else:
            continue
    
    
    tmp_d=copy.deepcopy(tmp_k)
    for ee in range(len(eng)):
        if eng[ee]:
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


def LCS(k_art, e_art, k_len, e_len):

    m=0
    n=0


    for m in range(k_len+1):
        LCStable.append([])
        LCStable[m].append(0)
        for n in range(e_len):
            if m==0:
                LCStable[m].append(0)
            else:
                LCStable[m].append(-1)
                

    for mm in range(k_len):
        for nn in range(e_len):
            k = k_art[mm].split(', ')
            e = e_art[nn].split(', ')
            if jaccard(k,e)>=0.8:
                print("0.8")
                LCStable[mm+1][nn+1]=LCStable[mm][nn]+1
            else:
                if LCStable[mm+1][nn]>=LCStable[mm][nn+1]:
                    LCStable[mm+1][nn+1]=LCStable[mm+1][nn]
                else:
                    LCStable[mm+1][nn+1]=LCStable[mm][nn+1]



    

    return LCStable[k_len][e_len]

def LCS_TraceBack(m, n, lcs):
    new_list =[]
    
    if m==0 or n==0:
        return lcs
    
    if (LCStable[m][n] > LCStable[m][n-1]) and (LCStable[m][n] > LCStable[m-1][n]) and (LCStable[m][n] > LCStable[m-1][n-1]):
        new_list.append(m)
        new_list.append(n)
        lcs.insert(0,new_list)
        result = LCS_TraceBack(m-1, n-1, lcs)
    
    elif (LCStable[m][n] > LCStable[m-1][n]) and (LCStable[m][n] == LCStable[m][n-1]):
        result = LCS_TraceBack(m, n-1,  lcs)
    
    else:
        result = LCS_TraceBack(m-1, n,  lcs)

    return result


def seq(i,a):
    global cnt
    kor = []
    eng = []
    p_kor=[]
    p_eng=[]
    for x in range(len(a)-1):
        if(a[x+1][0]-a[x][0] == a[x+1][1]-a[x][1] and (a[x+1][1]-a[x][1])<=5):
            kor.append([a[x][0],a[x+1][0]])
            eng.append([a[x][1],a[x+1][1]])
        else:
            p_kor.append([a[x][0],a[x+1][0]])
            p_eng.append([a[x][1],a[x+1][1]])

    x=0
    while 1:
        if x>=len(kor)-1:
            break
        else:
            if(kor[x+1][0]==kor[x][1]):
                kor[x+1][0]=kor[x][0]
                kor.pop(x)
            else:
                x=x+1

    x=0
    while 1:
        if x>=len(eng)-1:
            break
        else:
            if(eng[x+1][0]==eng[x][1]):
                eng[x+1][0]=eng[x][0]
                eng.pop(x)
            else:
                x=x+1
    
    f_ko = open("./joongang_corpus_data/no_single_space_text/ko/"+str(i)+".kor.txt","rU")
    f_en = open("./joongang_corpus_data/no_single_space_text/en/"+str(i)+".eng.txt","rU")
    f_total_kor = open("./total/ko/"+str(i)+".kor.txt","w")
    f_total_eng = open("./total/en/"+str(i)+".eng.txt","w")
    i_ko=0
    k=0
    
    while 1:
        if(k==len(kor)):
            break;
        if(len(kor)==0):
            break;
        
        if(i_ko==kor[k][0]-1):
            while 1:
                f_total_kor.write(f_ko.readline())
                cnt=cnt+1
                if(i_ko==kor[k][1]-1):
                    f_total_kor.write("\n")
                    break;
                i_ko=i_ko+1
            k=k+1
            
            if(k==len(kor)):
                break;
        f_ko.readline()
        i_ko=i_ko+1

    f_ko.close()
    f_ko = open("./joongang_corpus_data/no_single_space_text/ko/"+str(i)+".kor.txt","rU")
    i_ko=0
    k=0
    f_total_kor.write("\n")
    
    while 1:
        
        if(k==len(p_kor)):
            break;
        if(len(p_kor)==0):
            break;
        if(i_ko==p_kor[k][0]-1):
            tmp =f_ko.readline()
            f_total_kor.write(tmp)
            f_total_kor.write("\n")
            cnt=cnt+1
        elif(i_ko==p_kor[k][1]-1):
            tmp =f_ko.readline()
            f_total_kor.write(tmp)
            f_total_kor.write("\n")
            cnt=cnt+1
            k=k+1
        else:
            f_ko.readline()

        i_ko=i_ko+1
            
    i_en=0
    e=0
    while 1:
        
        if(e==len(eng)):
            break;
        if(len(eng)==0):
            break;
        
        if(i_en==eng[e][0]-1):
            while 1:
                f_total_eng.write(f_en.readline())
                if(i_en==eng[e][1]-1):
                    f_total_eng.write("\n")
                    break;
                i_en=i_en+1
            e=e+1
            if(e==len(eng)):
                break;
        f_en.readline()
        i_en=i_en+1
    f_en.close()
    f_en = open("./joongang_corpus_data/no_single_space_text/en/"+str(i)+".eng.txt","rU")
    i_en=0
    e=0
    f_total_eng.write("\n")
    while 1:
        #print(i_en)
        if(e==len(p_eng)):
            break;
        if(len(p_eng)==0):
            break;
        if(i_en==p_eng[e][0]-1):
            tmp =f_en.readline()
            f_total_eng.write(tmp)
            f_total_eng.write("\n")
        elif(i_en==p_eng[e][1]-1):
            tmp =f_en.readline()
            f_total_eng.write(tmp)
            f_total_eng.write("\n")
            e=e+1
        else:
            f_en.readline()
        i_en=i_en+1


    f_ko.close()
    f_en.close()
    f_total_kor.close()
    f_total_eng.close()

i=1

while i<=1:
    print(i)
    try:
        f_eng = open("./joongang_corpus_data/no_single_space_text/num/en/"+str(i)+".eng.txt","rU",)
        f_kor = open("./joongang_corpus_data/no_single_space_text/num/ko/"+str(i)+".kor.txt","rU",)
    except:
        i=i+1
        continue
    en=f_eng.readlines()
    ko=f_kor.readlines()

    for x in range(len(ko)):
        if ko[x][-1]=='\n':
            ko[x]=ko[x][:len(ko[x])-1]

    for y in range(len(en)):
        if en[y][-1]=='\n':
            en[y]=en[y][:len(en[y])-1]


    length=LCS(ko, en, len(ko), len(en))
    print(length)
    #print("LCS:",length)

    result=[]

    a = LCS_TraceBack(len(ko),len(en),result)
    seq(i,a)
    i=i+1



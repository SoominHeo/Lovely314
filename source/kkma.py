# This Python file uses the following encoding: utf-8
import os, sys
from konlpy.tag import Kkma
from konlpy.utils import pprint
import codecs
import time

kkma = Kkma()
POS = ["NR", "MDN"]
#POS = ["NNP"]
unit = {
    '백':100, '천':1000,'만':10000,'십만':100000,'백만':1000000,'천만':10000000,'억':100000000,'십억':1000000000,'백억':10000000000,'천억':100000000000,'조':" ",'여':" "
}
num_ = {
    '하나':1, '둘':2, '셋':3, '넷':4, '다섯':5, '여섯':6, '일곱':7, '여덟':8, '아홉':9, '열':10, '세이':" ", '석':3,
    '일':1, '이':2, '삼':3, '사':4, '오':5, '육':6, '칠':7, '팔':8, '구':9, '십':10,
    '한':1, '두':2, '세':3, '네':4, '댓':5,
    '수십':10, '수백':100, '수천':1000, '수만':10000, '수십만':100000, '수백만':1000000, '수천만':10000000, '수억':100000000, '수십억':1000000000, '수백억':10000000000, '수천억':100000000000
}

def nomalization(list):
    #print (list)
    #time.sleep(0.5)
    min = 0
    max = 0

    for i in range(len(list)):
        #print (list[i])
        for j in range(len(list[i])-1):
            if list[i][j] == ',':
                string = list[i][:j] + list[i][j+1:]
                list[i] = str(string)
            if list[i][j] == 'Z':
                list[i] = " "
                break

    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == '-':
                if list[i] == '-':
                    break
                a = list[i].split('-')
                list[i] = a[0]
                list[i+1] = a[1]
                break

    for i in range(len(list)-1):
        if len(list[i])>0 and len(list[i+1])>0 and list[i][0].isdigit() and list[i+1][0].isdigit() and list[i][0] in ['1','2','3','4','5','6','7','8','9','0']:
            if i > max:
                min = i
            max = i
            while (list[max+1][0].isdigit()):
                max += 1
            if list[i-1] != " ":
                list[i+1] = str(float(list[i]) * float(list[i+1]))
                list[i] = " "
            if i+1 == max:
                sum = 0
                for i in range(min,max+1):
                    if list[i] != " ":
                        sum += float(list[i])
                for i in range(min,max):
                    list[i] = " "
                if str(sum)[-1] != '0':
                    list[max] = str(float(sum))
                else:
                    list[max] = str(int(sum))
    #print (list)
    return list

total = 0
lines = 0

#input_url = "C:/Users/HEOSOOMIN/Desktop/2016-2/project/copus/joongang_ko/joongang_ko_"
#output_url = "C:/Users/HEOSOOMIN/Desktop/2016-2/project/copus/joongang_ko_num/"

input_url = "C:/Users/HEOSOOMIN/Desktop/ko/new_kr/"
output_url = "C:/Users/HEOSOOMIN/Desktop/ko/new_kr/num/"
#6177
num = 8000
new_input_url = ""
new_output_url = ""
for art_num in range(8217-num):
#for art_num in range(20):
    n = str(num)
    #new_input_url = input_url + n + ".txt"
    new_input_url = input_url + n + ".kor.txt"
    new_output_url = output_url + n + ".kor.txt"
    print (new_input_url)
    #print (new_output_url)
    num = num + 1
    try:
        file = open(new_input_url, "rt", encoding='utf-8')
    except IOError as e:
        print ("There is no",new_input_url)
        continue
    write_ko_File = open(new_output_url, 'w', encoding = 'utf-8')

    first_list = []
    i = 0
    for line in file:
        first_list.append(line)
        i += 1
    line_num = i

    kkma_list = [ [] for j in range(line_num)]
    i=0
    for i in range(line_num):
        if first_list[i] == "\n":
            kkma_list[i] = [(" "," ")]
        else:
            kkma_list[i] = kkma.pos(first_list[i])

    i=0

    for i in range(line_num):
        for j in range(len(kkma_list[i])):
            list = [" "," "]
            list[0] = kkma_list[i][j][0]
            list[1] = kkma_list[i][j][1]
            kkma_list[i][j] = list

    for i in range(line_num):
        for j in range(len(kkma_list[i])):

            if kkma_list[i][j][1] in POS:
                if kkma_list[i][j][0] in ['백','천','만','십만','백만','천만','억','십억','백억','천억','조','여']:
                    kkma_list[i][j][0] = str(unit[kkma_list[i][j][0]])
                    #print ("#",kkma_list[i][j][0])
                if kkma_list[i][j][0] in ['하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉', '열', '일', '이', '삼', '사', '오', '육',
                                  '칠', '팔', '구', '십', '한', '두', '세', '네', '댓', '수십', '수백', '수천', '수만', '수십만', '수백만', '수천만',
                                  '수억', '수십억', '수백억', '수천억', '세이', '석']:
                    kkma_list[i][j][0] = str(num_[(kkma_list[i][j][0])])

    num_list = [[] for i in range(line_num)]
    for i in range(line_num):
        for j in range(len(kkma_list[i])):
            num_list[i].append(kkma_list[i][j][0])

    fin_list = [[] for i in range(line_num)]
    for i in range(line_num):
        fin_list[i] = (nomalization(num_list[i]))

    for i in range(line_num):
        for j in range(len(kkma_list[i])):
            if len(fin_list[i][j])>0 and fin_list[i][j][0].isdigit() and fin_list[i][j][0] in ['1','2','3','4','5','6','7','8','9','0']:
                write_ko_File.write(str(fin_list[i][j]) + ", ")
        write_ko_File.write("\n")
    write_ko_File.close()


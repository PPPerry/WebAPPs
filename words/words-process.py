# with open("words.txt", "r") as f:
#     data = f.readlines()

# data1 = []
# for line in data:
#     if len(line) == 6:
#         data1.append(line.lower())

# file = open("out.txt", 'w').close()
# with open("out.txt","w") as f:
#     f.writelines(data1)
import pywebio
from pywebio.input import *
from pywebio.output import *
with open("out.txt", "r") as f:
        data = f.readlines()

def words():
    no = input("letters not in the word: (用空格分隔)")
    yes = input("letters in the word: (用空格分隔)")

    no = no.split(' ')
    yes = yes.split(' ')


    info = input_group("User info",[
  input('第0位字符(不确定则不填，下同)', name='0'),
  input('第1位字符', name='1'),
  input('第2位字符', name='2'),
  input('第3位字符', name='3'),
  input('第4位字符', name='4'),
])
        

    out = []
    flag = 0


    for word in data:
        for n in no:
            if n in word:
                flag = 1
                break
        if flag == 1: 
            flag = 0
            continue   
        for y in yes:
            if y not in word:
                flag = 1
                break
        if flag == 1: 
            flag = 0
            continue
        if  (info['0'] != '' and info['0'] == word[0]) and (info['1'] != '' and info['1'] == word[1]) and (info['2'] != '' and info['2'] == word[2]) and(info['3'] != '' and info['3'] == word[3]) and(info['4'] != '' and info['4'] == word[4]):
            out.append(word)
        elif (info['0'] == '') and (info['1'] == '') and (info['2'] == '') and(info['3'] == '') and(info['4'] == ''):
            out.append(word)
    

    put_scrollable(content=out, height=800)

pywebio.start_server(words)

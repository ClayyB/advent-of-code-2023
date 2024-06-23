# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:45:43 2023

@author: clari
"""

file = open("input.txt", mode='r')

data = file.read()
file.close()

j=0
k=0
summ = 0

words_fine = ["one", 
         "two",
         "three",
         "four",
         "five",
         "six",
         "seven",
         "eight",
         "nine"]

numbers_fine = ['o1e',
           't2o',
           't3e',
           'f4r',
           'f5e',
           's6x',
           's7n',
           'e8t',
           'n9e']
 
while j<len(data):
    if data[j]=='\n':
        my_string = data[k:j]
 
        for i in range(0,(len(words_fine))):
            my_string=my_string.replace(words_fine[i], numbers_fine[i])

        cali = []
        for kk in range(0,len(my_string)):
            if my_string[kk].isnumeric():
                cali.append(int(my_string[kk]))
        if len(cali)==1:
            summ = summ + int(str(cali[0]) + str(cali[0]))
        else:
            summ = summ + int(str(cali[0]) + str(cali[-1]))
        k = j+1
    j+=1
    
print(summ)



    
     


 

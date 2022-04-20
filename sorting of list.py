# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:03:45 2022

@author: Admin
"""
#using 2 for loops taking index+1 for second loop and comparing then swapping to sort the list 
list = [1,98,3,7,42,5,6,8,4,9,47,7,2]
for i in range(len(list)):
    for j in range(i+1,len(list)):
       if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)
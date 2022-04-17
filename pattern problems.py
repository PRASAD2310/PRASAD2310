# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 18:58:17 2022

@author: Admin
"""

for i in range(0,5):
    print("*")
    
    
    

print("#####################################")

    
    

for i in range(0,4):
 
   for j in range(0,4):
     print("*",end="")
   print("")
    
   
    

print("#####################################")

   
   
    
for a in range(0,5):
    for b in range(0,a):
        print("*",end="")
    print("") 


print("#####################################")


a=5
for i in range (a,0,-1):
    for j in range (0,i) :
      print ("*",end="")
    print("")
    


print("#####################################")

r=int(input("enter the number of rows: "))
n= r*2-1

for i in range (0,r):
    for j in range (0,n):
      print (end="#")  
    n= n-2
    for j in range (0,i+1):
        print ("* ",end="")
    print()



print("#####################################")

r=int(input("enter the number of rows: "))
n=r
for i in range (0,r):
    for j in range (0,n):
      print (end=" ")  
    n= n-1
    for j in range (0,i+1):
        print ("* ",end="")
    print()


r=int(input("enter the number of rows: "))
n=r
for i in range (0,r):
    for j in range (0,i+1):
      print (end=" ")  
    n= n-1
    for j in range (0,n):
        print ("* ",end="")
    print()














   
    
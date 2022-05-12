# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:41:18 2022

@author: Admin
"""

      
# Python program to find H.C.F of two numbers

def find_hcf(a,b):
    if (a<b):
      small_n=a
    else:
      small_n=b
    for i in range (1,small_n+1):
        if((a%i==0 )and (b%i==0)):
            hcf= i
    return hcf      

a = int (input("give 1 num :"))
b = int (input("give 2 nd num :"))

print("The H.C.F. is", find_hcf(a, b))      

# finding lcm of 2 numbers 
def find_lcm(a,b):
    if (a>b):
      grt=a
    else:
      grt=b
    while(True):
        if((grt%a==0 )and (grt%b==0)):
            lcm=grt
            break
        grt+=1
          
    return lcm     

a = int (input("give 1 num :"))
b = int (input("give 2 nd num :"))

print("The lcm is", find_lcm(a, b))      

##imorting own function 
import create_function
create_function.cubing(3)

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 11:08:06 2022

@author: Admin
"""
#cubing function ************************************************

def cubing(number):
  cube=number*number*number
  return cube
y=int(input("enter your number:"))
b=cubing(y)
print(b)


#sqaure func **************************************************888

def square(number1):
    squares = number1 * number1
    return squares

x=int(input("enter your number:"))
a=square(x)
print(a)
    

#factorial fuction **************************************************8
def factorial(n):
  
   if n<0:
       print("number invalid")
   else:
       x=1
       while n>1:
        x=x*n
        n=n-1
       return x
n=int(input("enter your desired number :"))  
f1=factorial(n) 
print(f1)


#factorial fuction **************************************************8

def factorial(n):
  
   if n==1:
       return 1
   else:
       return n*factorial(n-1)
   
n=int(input("enter your desired number :"))  
f1=factorial(n) 
print(f1)    



#exponential function **********************************************88

def expo(num,power):
    if num<0:
        print("number invalid")
    else:
         exp=num**power
         return exp
num=int(input("enter your desired number :"))  
power=int(input("enter your desired power :"))  
f2=expo(num,power) 
print(f2)
  
    
  
    
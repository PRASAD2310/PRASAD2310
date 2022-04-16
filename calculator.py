# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 10:13:23 2022

@author: Admin
"""
while(True):
   a=int(input("enter 1st num: "))
   b=int(input("enter 2nd num: ")) 
   sum =a + b 
   sub = a-b
   mult = a*b
   div = a/b
   op_com = input (""""Enter your choice 
                          + for add ,
                          - for sub,
                          * for mult 
                          / for div 
                              your command please :""")
   if op_com=='*' :
    print("multiplication is : ",mult)
   elif op_com== '+':
        print ("addition is : ",sum)
   elif op_com== '-':
            print("substraction is : ",sub)
   elif op_com== '/':
                print ("division is :",div)
   else :
                        print ("wrong command ")
        
   x=input ("   press  y-> continue , n-> exit : ")   
   if x== 'y':
    True
   else :
       break 
  


  
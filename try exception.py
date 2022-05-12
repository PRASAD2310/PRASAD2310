# -*- coding: utf-8 -*-
"""
Created on Sun May  1 07:47:35 2022

@author: Admin
"""

# try 

x= -1
y=2
try :
     if not type(x) is int and  x<0 :
      raise ValueError()
except NameError:
    print("define variable fisrt ")    
except TypeError :
    print('enter int ')
    x =int(input("enter num : ")) 
else :
    print("give positive values ")
finally :
    print("out ")



x = "aplpha"

if not type(x) is int:
  raise TypeError("Only integers are allowed")


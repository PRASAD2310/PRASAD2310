# -*- coding: utf-8 -*-
"""
Created on Sun May  8 19:28:36 2022

@author: Admin
"""





import mysql.connector as c
con = c.connect (user="root",host ="localhost",passwd = "root", database= "prasad")
if con.is_connected():
  print("sucess")
 
cursor=con.cursor()
while True:
 code=int(input("enter code:")) 
 name=(input("enter name:"))
 salary=int(input("enter salary:"))
 query= "insert into emp values({},'{}',{})".format(code,name,salary)
 cursor.execute(query)
 con.commit()
 print("data inserted sucessfully")
 x=int(input("1->enter more\n 2-> exit\n enter choice:"))
 if x==2:
  break
   

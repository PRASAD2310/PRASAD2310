# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 12:30:45 2022

@author: Admin
"""

Students_list=['ravi','raj','shyam','rahul']
value= ( input("enter the new name :"))
Students_list.append(value)
print(Students_list)
alpha=(input("alphabet :"))
for i in Students_list:
 if ((i[0])==alpha):
     print(i)
    
  

# f1=find(Students_list)   
# print(f1)


e={}
e['emp_name']='prasad'
sub=input("subj name :")
val=input("val :")
e.update({sub:val})
print(e)
alphabet=(input("your desired parameter:"))
for j in e:
    if ((j[0])==alphabet):
        print(j)
        
        
        


list_dicionary=[{"name":"vinayak","age":29},{"name":"lalit","age":39},{"name":"hitesh","age":49},{"name":"rohit","age":19}]

user_input="l"


def list_initial_search(list_dicionary):
          
    while(True):
        
        user_input=input("please enter initial alphabet of the name you want to print... : ")
        print("\n",user_input)
        
        count=0
        for element in list_dicionary:
            # print(name)   
           
            if element["name"][0].lower()==user_input.lower():             
                print("\n",element)
                break           
            count+=1
    
        if count>=len(list_dicionary):   
            print("invalid input/ alphabet not in names..")
            break
            
        user_input2=input("Do you want to continue ? : yes/no : ")
        
        if user_input2=="yes":
            pass
        
        else:
            break
    
list_initial_search(list_dicionary)   
 
  
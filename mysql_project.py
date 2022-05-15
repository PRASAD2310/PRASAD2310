import mysql.connector as connecor
from unicodedata import name

class DBhelper:
   def __init__(self) :
       self.con=connecor.connect (user="root",
                             host ="localhost",
                             passwd = "root",
                             database= "prasad")
       query = 'create table if not exists user(userid int primary key,username varchar(20),phone varchar(20))'
       cur=self.con.cursor()  
       cur.execute(query)
       print('created')

   def insert_user(self):
        userid= int(input("enter used id"))
        username=input("enter username")
        phone=input("enter phone number ")
        query = "insert into  user (userid,username,phone) values ({},'{}','{}')".format(userid,username,phone)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('data inserted')

   def fetch_all(Self):
        query1="select * from user "
        cur = Self.con.cursor()
        cur.execute(query1)
        for row in cur:
           print('userid is =',row[0])
           print('username is = ',row[1])
           print('phone is = ',row[2])
           print()
           print()

   def delete(Self):
      userid=int(input("enter userid you wish to delete:")) 
      query= "delete from user where userid ={}".format(userid)
      cur=Self.con.cursor()
      cur.execute(query)
      Self.con.commit()
      print("data deleted sucessfully")

   def update(self):
      userid=int(input("enter userid you wish to update:"))
      newusername=input("enter new username:")
      newnum=input("enter new phone")
      query2 = "update user set username='{}',phone='{}'where userid={}".format(newusername,newnum,userid)
      cur1=self.con.cursor()
      cur1.execute(query2)
      self.con.commit()
      print("data updated sucessfully")



def mysqlmain():
 db=DBhelper()
 while True:
   print("**********welcome *************")
   print()

   print("press 1 to insert")
   print("press 2 to delete ")
   print("press 3 to update")
   print("press 4 to fetch")
   print("press 5 to exit")
   print()

   try :
      choice=int(input())
      if (choice==1):
          db.insert_user()
          pass
      elif (choice==2):
          db.delete()
          pass 
      elif (choice==3):
          db.update()
          pass  
      elif (choice==4):
          db.fetch_all()
          pass
      elif choice==5:
         print("successfully exited")
         break
      else:
          print("invalid input try again ")
   except Exception as e:
     print(e) 
     print("invalid input try again ")  




m1=mysqlmain()

          
  
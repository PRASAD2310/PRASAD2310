# -*- coding: utf-8 -*-
"""
Created on Sun May  1 11:24:18 2022

@author: Admin
"""

class human(object):
     eyes=2
     dna="yx"
     species="mammals"
    
     def __init__(self, name_v ,age_v ,hieght_v,wieght_v):
        self.name=name_v
        self.age=age_v
        self.hieght=hieght_v
        self.wieght=wieght_v
        
     def display_details(self):
         print ("name is {}".format(self.name))
         print ("age  is {}".format(self.age))
         print ("hieght is {}".format(self.hieght))
         print ("wieght is {}".format(self.wieght))
    
      
human2=human("raj",25,6,69)
human2.display_details()


class robot(human):
    
    def __init__ (self,name_v,age_v,hieght_v,wieght_v,type_v,body_v,validity_v):
        self.type=type_v
        self.body=body_v
        self.valid=validity_v
       
        #if we use class.init......function of inherited class are defining )
        human.__init__(self, name_v, age_v, hieght_v, wieght_v)
         
    def display_details(self):
         print ("name is {}".format(self.name))
         print ("age  is {}".format(self.age))
         print ("hieght is {}".format(self.hieght))
         print ("wieght is {}".format(self.wieght))
    
         print ("type {} , bodytype {}, valid till year - {}".format(self.type,self.body,self.valid))
            
    
        
genesys1=robot("gen1", 0, 10, 100, " defense", "alloys", 2029)
genesys1.display_details()

    
class drone(robot):
         def __init__ (self,name_v,age_v,hieght_v,wieght_v, type_v, body_v, validity_v,fly_v):
           self.fly=fly_v
           
       #if we use super all function of inherited class are defining )
           super().__init__(name_v, age_v, hieght_v, wieght_v, type_v, body_v, validity_v)
          
         def display_details(self):
             print ("name is {}".format(self.name))
             print ("age  is {}".format(self.age))
             print ("hieght is {}".format(self.hieght))
             print ("wieght is {}".format(self.wieght))
             
             print ("type {} , bodytype {}, valid till year - {}".format(self.type,self.body,self.valid))
           
             
             print("can fly:{}".format(self.fly))
          
            
drone1=drone(1, 2, 4, 5, "yes",1,2,"yes")
drone1.display_details()
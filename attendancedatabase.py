# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:28:38 2020

@author: reena
"""




import mysql.connector
mydb = mysql.connector.connect(
        host="localhost",
        user='root',
        password="",
        database="attendance"
)
print(mydb)

myCursor = mydb.cursor()
   
#myCursor.execute("CREATE TABLE `attendance`.`mca` ( `rollno` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(50) NOT NULL , `theory` BOOLEAN NOT NULL , `practical` BOOLEAN NOT NULL , `subject` VARCHAR(50) NOT NULL , `month` DATE NOT NULL , PRIMARY KEY (`rollno`)) ENGINE = InnoDB;")
 
#myCursor.execute("SHOW TABLES") 

#for x in myCursor:
#    print(x) 


sqlStr="INSERT INTO `mca`(`rollno`, `name`, `theory`, `practical`, `subject`, `month`) VALUES (NULL,%s,%s,%s,%s,%s);"
val =[
      ("reena",1,0,"Python",'1-04-2020'),
      ("riya",1,1,"Python",'2-04-2020')
]


myCursor.executemany(sqlStr,val)
mydb.commit() 
#no of rows added in database 
print(myCursor.rowcount) 





           

        
    
   

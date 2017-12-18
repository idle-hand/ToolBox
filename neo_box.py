##CREATE TABLE "tool" (
##    "name" TEXT,
##    "type" TEXT,
##    "id_num" TEXT,
##    "location" TEXT,
##    "status" TEXT,
##    "age" TEXT
##);
#             these are the data elements in my tables
#                           tool and employ
##CREATE TABLE employ (
##    "name" TEXT,
##    "email" TEXT,
##    "emp_num" TEXT,
##    "security " TEXT
##, "hire_date" TEXT);
##CREATE TABLE sqlite_stat1(tbl,idx,stat);


import sqlite3 as lite
import sys
        
conn = lite.connect('bigbox.db')
print ("Opened database successfully");
cursor = conn.execute("SELECT name, type, id_num, location, status, age from tool")
for row in cursor:
    print ("name =  ", row[0])
    print ("type = ", row[1])
    print ("id_num = ", row[2],"\n\n")
    print('location =', row[3])
    print('status =', row[4])
    print('age =', row[5],"\n\n\n")
    
   
    
print ("Operation done successfully");
conn.close()


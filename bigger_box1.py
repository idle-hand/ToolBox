# - Tool Inventory Manager

'''Project = personal python3 classes -
manage tool inventory for contractor on mult. sites
across mult site and employees - all empl. users check tools in or out
and out of main inventory, that tracks damaged or missing tools
- age of tools - maint and suggested replacement dates?
'''
class Tool:

    '''Full Tool Inventory e.g. Main Tool Box for company '''
    def __init__(self,name, ttype, id_num, location, status, age):
        self.name = name
        self.ttype = ttype
        self.id_num = id_num
        self.location = location
        self.status = status
        self.age = age




# def add tool,
# remove tool,
# assign too




class Employee:
    def __init__(self,name, email, emp_num, security, hire_date):
        self.name = name
        self.email = email
        self.emp_num = emp_num
        self.security = security
        self.hire_date = hire_date


class Site:
     def __init__(self, jobname, jobaddress, jobsize, jobstart, joblength, jobvalue):
         self.jobname = jobname
         self.jobaddress = jobaddress
         self.jobsize = jobsize
         self.jobstart = jobstart
         self.joblength = joblength
         self.jobvalue = jobvalue
import sqlite3 as lite
import sys

con = lite.connect('bigbox.db')

        
conn = lite.connect('bigbox.db')
print ("Opened database successfully");
cursor = conn.execute("SELECT name, type, id_num, location, status, age from tool")
for row in cursor:
    print ("name =  ", row[0])
    name = row[0]
    print ("type = ", row[1])
    ttype = row[1]
    print ("id num = ", row[2])
    id_num = row[2]
    print('location =', row[3])
    location = row[3]
    print('status =', row[4])
    status = row[4]
    print('age =', row[5],"\n")
    age = row[5]

       
  
    
print ("Operation done successfully");
conn.close()


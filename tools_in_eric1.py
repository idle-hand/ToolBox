# - Tool Inventory Manager

'''Project = personal python3 classes -
manage tool inventory for contractor on mult. sites
across mult site and employees - all empl. users check tools in or out
and out of main inventory, that tracks damaged or missing tools
- age of tools - maint and suggested replacement dates?
'''


class Tool:

    '''Full Tool Inventory e.g. Main Tool Box for company '''
    def __init__(self,name, descrip, idnum, loc, status, toolage):
        self.name = name
        self.descrip = descrip
        self.idnum = idnum
        self.loc = loc
        self.status = status
        self.toolage = toolage




# def add tool,
# remove tool,
# assign too


class Drill(Tool):

    def __init_(self,name, descrip, idnum, loc, status, toolage, power, bits):

        Tool.__init__(self, name, descrip, idnum, loc, status, toolage)
        self.power = power
        self.bits = bits


class Cutting(Tool):

    def __init__(self,name, descrip, idnum, loc, status, toolage, subtype, tsize):

        Tool.__init__(self, name, descrip, idnum, loc, status, toolage)
        self.subtype = subtype
        self.tsize = tsize

class Driver(Tool):

    def __init__(self, name, descrip, idnum, loc, status, toolage, subtype, head):

        Tool.__init__(self, name, descrip, idnum, loc, status, toolage)
        self.subtype = subtype
        self.head = head


class Hammer(Tool):

    def __init__(self, name, descrip, idnum, loc, status, toolage, subtype, handle):
        Tool.__init__(self, name, descrip, idnum, loc, status, toolage)
        self.subtype = subtype
        self.handle = handle

class Employee:
    def __init__(self,name,address, hiredate, status, subcontr,contact):
        self.name = name
        self.address = address
        self.hiredate = hiredate
        self.status = status
        self.subcontr = subcontr
        self.contact = contact


class Site:
     def __init__(self, jobname, jobaddress, jobsize, jobstart, joblength, jobvalue):
         self.jobname = jobname
         self.jobaddress = jobaddress
         self.jobsize = jobsize
         self.jobstart = jobstart
         self.joblength = joblength
         self.jobvalue = jobvalue


job1 = Site('Rideau 1','1049 Curry Road',4,'25/6/2017','7 months','42,000')


driver1 = Driver('philips','4 inch',101,'site one','out','3 years''multi','philips','ronson')
driver2 = Driver('philips','6 inch',102,'site one','in','non power',100,'head')

hammer1 = Hammer('regal','12 inch',201,'site three','out','non power','short',150)
emp101 = Employee ('David D. David','500 Canada Ave','28/12/2001','Active','Yes','555-5555')

drill1 = Drill('De-Walt','Corded',307,'Tool Crib','in','2 years')




print(driver1.name,driver1.descrip,driver1.idnum)
print(driver2.subtype,driver2.status,driver2.loc,driver2.idnum)
print(emp101.name,emp101.status,emp101.contact)

print(job1.jobvalue,job1.jobname,job1.jobaddress)
print(drill1.loc,drill1.idnum)
      
job2 = Site('Rideau 2','John Cord Road',18,'1/6/201','3 years','642,000')


driver3 = Driver('Stanley','8 inch',103,'site two','out','2 years''multi','philips','ronson')
driver4 = Driver('philips','6 inch',102,'site one','in','non power',100,'head')

hammer2 = Hammer('regal','12 inch',201,'site three','out','non power','short',150)
emp102 = Employee ('Howie D. Howie','1500 Winipe Ste','28/12/2011','Active','Yes','555-5555')

drill2 = Drill('Stanly','6 Volt',307,'Tool Crib','in','2 years')



print(driver3.name,driver1.descrip,driver1.idnum)
print(driver4.subtype,driver2.status,driver2.loc,driver2.idnum)

print(emp102.name,emp101.status,emp101.contact)

print(job2.jobvalue,job1.jobname,job1.jobaddress)
print(drill2.loc,drill1.idnum)
      
      
print(hammer1.name)
print(hammer2.name,hammer2.idnum, hammer2.loc)

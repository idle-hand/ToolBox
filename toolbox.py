# - ToolBox - MainBox


'''Project = personal python3 classes -
manage tool inventory for contractor on mult. sites
across mult site and employees - all empl. users check tools in or out
and out of main inventory, that tracks damaged or missing tools
- age of tools - maint and suggested replacement dates?
'''


class MainBox:
    
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



##Hammers - class Hammer
##Pliers - class Plier
##Screwdrivers - class Driver
##Drilling Tools - class Drill
##Wrenches - class Wrench
##Cutting Tools - class Cutting
##Measureing Devices class Measure
##Levels class Level
##Axes and Hatchets = class cutting
##Saws class cutting
##Storage Items calss Storage 

class Driver(MainBox):
    
    def__init__(self, name, descrip, idnum, loc, status, toolage, subtype, head)
        MainBox.__init__(self, name, descrip, idnum, loc, status, toolage)
        self.subtype = subtype
        self.head = head

        
class Hammer(MainBox):
    
    def__init__(self, name, descrip, idnum, loc, status, toolage, subtype, handle)
        MainBox.__init__(self, name, descrip, idnum, loc, status, toolage)
        self.subtype = subtype
        self.handle = handle        
      
    
    
    
        
class HandTools(MainBox):
    
    def __init__(self, name, descrip, idnum, loc, status, subtype, quant):
        MainBox.__init__(self, name, descrip, idnum, loc, status)
        self.subtype = subtype
        self.quant = quant

                    
class Employee:
    def __init__(self,name,address, hiredate, status, subcontr,contact):
        self.name = name
        self.address = address
        self.hiredate = hiredate
        self.status = status
        self.subcontr = subcontr
        self.contact = contact
        
driver1 = Driver('philips','4 inch',101,'site one','out','non power',100)
driver2 = (Driver('philips','6 inch',102,'site one','in','non power',100)
hammer1 = Hammer('regal','12 inch',201,'site three','out','non power',150)
emp101 = Employee ('David D. David','500 Canada Ave','28/12/2001','Active','Yes','555-5555')



print(driver1.name,driver1.descrip,driver1.idnum)
print(driver2.subtype,driver2.status,driver2.loc,driver2.idnum)
print(emp101.name,emp101.status,emp101.contact)

                   
                   
        
##ToolPush - work site tool inventory manager pers. proj. per python
##self-study - dec. 2017 david howe kingston on. ca. oop - invent_site
##class __init__ inventory , e.g. ham1 = 50, (hammer type 1? quantity 50
##in tool box at job start_)
##
##site loc sub tool types, details, status, totals empoyer issue to, emp.
##number, name, subcontract boxcontroler, emp number, name
####
## a tool tracking app that assigns accountability to a person who “signs out” a particular tool. This kind of app doesn’t rely on beacons to track tools, but rather shifts the responsibility to the person last assigned to the tools. An app like ShareMyToolbox creates a “catalog” of tools and assigns the tool to an employee who “accepts” it in the app. His/her responsibility for the tool is easy for everyone to see and, once the tool is returned to the warehouse, the name of the borrower is removed as the responsible party.
##
##Think about it: when a member of your team knows there’s a digital
##record of who has a particular tool, they won’t leave it lying among
##piles of debris on a remote job location. Instead, he/she will be more
##compelled to return it to the inventory that you’re managing.
####

##1. Know what you currently have.
##The first step is to compile a current inventory of all tools and equipment. How are you going to track it if you don’t even know you have it? When you know what you already own, you’ll buy fewer duplicates, saving you money – and sanity.
##
##2. Know where it currently is.
##Obviously, tools and equipment move in the field – that’s part of what makes tracking them a challenge. But look at the list of what you currently own, and answer the question: right now, where is it?
##
##3. Know how long you’ve had it.
##You know all that equipment isn’t built to last forever. It’s important to know how long you’ve owned something so you can anticipate needed maintenance or replacement, and also be sure your equipment is lasting as long as it should.
##
##Taking these first three tool tracking steps and getting organized is going to take effort, but with modern technology, it is completely do-able. (And by modern technology, we do not mean the old desktop PC in the back office.) Whether you’re trying to build your own process or evaluating a tool tracking system, be sure it starts with getting organized. Ignorance is not bliss when it comes to tool tracking (or not tracking). Take advantage of the technology available to make your life simpler – and your bottom line healthier.
##
##To learn more about tool tracking technology that helps you easily
##organize your tool inventory, visit
##www.sharemytoolbox.com/tool-tracking.
##

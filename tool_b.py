class MainBox:

    '''Full Tool Inventory e.g. Main Tool Box for company '''
    
    def __init__(self, tname, tidnum, tloc, tage):
        self.tname = tname
        self.tidnum = tidnum
        self.tloc = tloc
        self.tage = tage

class Power(MainBox):
    def __init__(self, tname, tidnum, tloc, tage, corded, voltage):
        Mainbox.__init__(self, tname, tidnum, tloc, tage)
        self.corded = corded
        self.voltage = voltage

class Hand(MainBox):
    def __init__(self, tname, tidnum, tloc, tage, tsize):
        Mainbox.__init__(self, tname, tidnum, tloc, tage)
        self.tsize = tsize

        
class Employee:
    def __init__(self, name, idnum, address, contact, level):
        self.name = name
        self.idnum = idnum
        self.address = address
        self.contact = contact
        self.level = level

class Manager(Employee):
    def __init__(self, name, idnum, address, contact, level, rank):
          Employee.__init__(self, name, idnum, address, contact, level)
          self.rank = rank

class Onsite(Employee):
    def __init__(self, name, idnum, address, contact, level, status):
          Employee.__init__(self, name, idnum, contact, level)
          self.status = status

          
          
        

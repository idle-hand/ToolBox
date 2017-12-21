import sqlite3
conn = sqlite3.connect('mane.db')
c = conn.cursor()

pnames = []
pdescrp = []
pid_nums = []
plocate = []
pbuy_date = []

cursor = c.execute("SELECT tname, descrp, id_num, locate, buy_date from tools")


for row in cursor:

    name = row[0]
    descrp = row[1]
    id_num = row[2]
    locate = row[3]
    buy_date = row[4]
    
    pnames.append(name)
    pdescrp.append(descrp)
    pid_nums.append(id_num)
    plocate.append(locate)
    pbuy_date.append(buy_date)
    

#                                                                          Save (commit) the changes
conn.commit()
#                                            We can also close the connection if we are done with it.
#                                  Just be sure any changes have been committed or they will be lost.
conn.close()

##CREATE TABLE employ (
##    ename     TEXT,
##    email     TEXT,
##    emp_num   TEXT,
##    hire_date TEXT
##);
##
##CREATE TABLE tools (
##    tname    TEXT,
##    descrp   TEXT,
##    id_num   TEXT,
##    locate   TEXT,
##    buy_date TEXT
##);


# Create table
# c.execute('''CREATE TABLE tools
#(tname text, descrp text, id_num text, locate text, buy_date text)''')
# Insert a row of data

##Here's an example of a list and an example use:
##
##x = [1,3,5,6,2,1,6]
##
##'''
##You can then reference the whole list like:
##'''
##print(x)
##
### or a single element by giving its index value.
### index values start at 0 and go up by 1 each time
##
##print(x[0],x[1])

x = 0 

while x < 5 :
    print('*************************')
    print('*************************')
    print(pnames[x])
    print(pdescrp[x])
    print(pid_nums[x])
    print(plocate[x])
    print(pbuy_date[x])
    print('*************************')
    print('*************************')
    x = x + 1


print('*************************')
print('*************************')
print('  Thatssss Alll Fokessss ')
print('*************************')
print('*************************')

def qikpik(a):
    print('*****           *********')
    print('*************************')
    print(pnames[a])
    print(pdescrp[a])
    print(pid_nums[a])
    print(plocate[a])
    print(pbuy_date[a])
    print('****             ********')
    print('*************************')


qikpik(7)
qikpik(22)
qikpik(9)
    


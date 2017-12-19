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
    
for name in pnames:
    print(name, descrp, id_num, locate, buy_date)
    print('main tool box inventory -- main tool box inventoy','\n\n')


# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
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

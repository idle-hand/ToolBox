import sqlite3
conn = sqlite3.connect('mane.db')
c = conn.cursor()
# Create table
# c.execute('''CREATE TABLE tools
#(tname text, descrp text, id_num text, locate text, buy_date text)''')
# Insert a row of data

pnames = []
pdescrp = []
pid_nums = []
plocate = []
pstatus = []

cursor = c.execute("SELECT tname, descrp, id_num, locate, buy_date from tools")


for row in cursor:

    name = row[0]
    descrp = [1]
    id_num = [2]
    locate = [3]
    status = [4]
    
    pnames.append(name)
    pdescrp.append(descrp)
    pid_nums.append(id_num)
    plocate.append(locate)
    pstatus.append(status)
    
for name in pnames:
    print(name, id_num, locate)

# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


## (tname text, descrp text, id_num text, locate text, buy_date text)

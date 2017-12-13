import csv  
with open('tools_fin.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    t_name = []
    t_descrip = []
    t_idnum = []
    t_loc = []
    t_status = []
    t_date = []

    for row in readCSV:
        name = row[0]
        descrip = row[1]
        idnum = row[2]
        loc = row[3]
        status = row[4]
        age_of_tool = row[5]

        t_name.append(name)
        t_descrip.append(descrip)
        t_idnum.append(idnum)
        t_loc.append(loc)
        t_status.append(status)
        t_date.append(age_of_tool)
        


        
        
        print(name)
        print(idnum)
        print(descrip)
        print(loc)
        print(status)
        print(age_of_tool)

        print('********************************')


print(len(t_name))

x = 0


while x < 41:
    print(t_name[x], t_descrip[x], t_idnum[x], t_loc[x], t_status[x], t_date[x])
    print('*****************')
    x = x + 1

print ('done')

        
    

# create a  list of team members with option to sort or random order after team list created.

print("This will ask you to add team members, then an option to reproduce them in random order\n")

import random, csv
import os
from datetime import date

# Dictionary
dt = date.today()
dt = dt.strftime("%d-%b-%Y")
teamlist = []
name = {}
fileDirectory = "C:\\coding data\\Output\\" 
os.chdir(fileDirectory)
fileName = "team_list.csv"
stopped = False
# Data capture
with open(fileName, 'a', newline="") as file:
    csvwriter = csv.writer(file)
    while not stopped:  # see alt below from cat_names.py use while True:
        name = input("add a name, type 'F' - Finish: ")
        #    if name == '':
        # break     alternate way of stopping the loop. 
        if name.upper() == "F":
            stopped = True
        else:
            csvwriter.writerow([dt, name.title()])  # write as a line to csv file
            teamlist.append(name.title())
file.close()  # (save) close file
# Data count
team_num = len(teamlist)
print("\nYou have entered {} players' names.".format(team_num))
print("Your team on {} is ready for download from {}.\n".format(dt, fileDirectory))
request = input("Do you want the team sorted alphabetically Y/N?")

if request.upper == "Y": # Screen print list in alphabetic order
    teamlist.sort()
    print("Your team is:")
elif request == "y": # Screen print list in alphabetic order
    teamlist.sort()
    print("Your team is:")
else:
    random.shuffle(teamlist)
    print("Your team in random order is:")
    
print(*teamlist, sep= "\n")





# create the randon number generator
# random_num = random.randint(1, team_num)
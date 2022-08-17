# create a  list of team members with option to sort or random order after team list created.

print("This will ask you to add team members, then an option to reproduce them in random order")
print()
import random
from datetime import date
import csv
# Dictionary
dt = date.today()
dt = dt.strftime("%d/%m/%Y")
teamlist = []
name = {}
filename = "C:\\coding data\\Datadump\\team.csv" 
stopped = False
# Data capture
with open(filename, 'a',newline="") as file:
    csvwriter = csv.writer(file)
    while not stopped:  # see alt below from cat_names.py use while True:
        name = input("add a name, type 'F' - Finish: ")
        #    if name == '':
        # break     alternate way of stopping the loop. 
        if name == "F":
            stopped = True
        elif name == "f":
            stopped = True    
        else:
            csvwriter.writerow([dt, name.title()])  # write as a line to csv file
            teamlist.append(name.title())
file.close()  # (save) close file
# Data count
team_num = len(teamlist)
print("\nYou have entered", team_num, "players' names.")
print("Your team on",dt,"is ready for download.\n")
request = input("Do you want the team sorted alphabetically Y/N?")
request = request.upper
if request == "Y": # Screen print list in alphabetic order
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
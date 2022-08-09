# Don't run this all at once.  
# It could crate a file, read and write to it and then delete it.

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile2.txt", "a")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
f.close()


# to delete the file..
# https://www.w3schools.com/python/python_file_remove.asp
import os
if os.path.exists("demofile2.txt"):
    print("this would've deleted it")
#  os.remove("demofile2.txt")
else:
  print("The file does not exist")
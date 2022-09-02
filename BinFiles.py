import os 
import send2trash

folderName = input("What folder are you wanting to delete DS_Store files?")
os.chdir(folderName)
for filename in os.listdir():
  
    num=0
    if filename.endswith('.DS_Store'):
        num = num + 1 
        send2trash.send2trash(filename)
        print(str(num) + "files deleted")

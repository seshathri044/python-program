import os
import shutil
import glob
import csv
import json
print("os operation")
if os.path.exists("myfile.txt"):
    print("Yes")
else:
    print("No")
print("shutil operation\n")
shutil.copy("myfile.txt","newfile.txt")
print("glob operation")
f1=glob.glob("????.txt")
print(f1)
f2=glob.glob("*.txt")
print(f2)
print("csv operation\n")

with open('email-password-recovery-code.csv', 'r') as file:
    csv_read = csv.reader(file)
    for row in csv_read:
        print(row)
print("Json operation\n")
data={"name":"karth99","age":19,"city":"madurai"}
with open('myjson.json','w') as file:
    json.dump(data,file)
with open('myjson.json','r') as file:
    data1 = json.load(file)
    print(data1)
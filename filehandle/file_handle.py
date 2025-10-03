# file_obj = open("D:\\Python-class\\filehandle\\txtfile.txt", "r")
# a=file_obj.read()
# print(a)
# file_obj.close()
# f1=open("myfile.txt","w")
# f1.write("I am M seshathri final year cse student\n")
# f1=open("myfile.txt","r")
# f1.close()
# Open the file in write mode and write some content
# f1 = open("myfile.txt", "w")
# f1.write("I am M seshathri, a final year CSE student.\n")
# f1.close()  # Always close the file after writing
# Open the file in read mode and read its contents


# write,seek,tell,read operation
f1 = open("myfile.txt", "w")
a=45
b=str(a)
f1.write(b)
c=["vanakam da kodurama\n","Madura Payaluka da\n ippo onnu appo onnu\n"]
f1.writelines(c)
print("position:",f1.tell())
f1.close()
f1=open("myfile.txt","r")
f1.seek(23)
print("position:",f1.tell())
content = f1.read()  # Read the entire content of the file
#f1.read(10)//Madura Pay ,only 10 position character is will be printed
#f1.readline(4)//Madu ,in that line only 4 character will be printed
print(content)  # Print the content to see what was written
f1.close()  # Always close the file after reading

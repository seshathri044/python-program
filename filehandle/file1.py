f1=open("myfile.txt","r")
a= f1.read()
b =a.split(" ")
print(b)
print("remove duplicate value")
c=set(b)
print(c)


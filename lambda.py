#Lambda
square = lambda x:x*x
rs=square(5)
print(rs)
print("-----------")
#Sort using lambda
n=[1,2,1,5,3]
s=sorted(n,key=lambda x:x**2)
print(s)
print("-----------")
#len of String using lambda
w=['hello','welcome','home','seshathri']
f=filter(lambda word: len(word)>5,w)
print(list(f)) 
print("-----------")
#Mapping list using lambda
number =[2,3,4,5]
square_num=map(lambda x: x*x,number)
print(list(square_num))


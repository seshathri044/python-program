print("hello world")
a=5# In the initial a is 5
print(a)# 5 is printed
b="55"
c=33.2
#Normal if block
if a>5:# But here the a is 4 because it is oveerride
    print("Inside if Block")#SO this block is not excecuted
print("Outside if block")
print(b, type(b))
print(c, type(c))
a=4          #The value of 5 is override in the this area
print(a)
# TypeCasting
e="10"
d="1"
print(e+d)# The answer is 101 because it is in the String
print(int(e)+int(d))# Using tupecaste the string is converted into int
#f="A" #print(int(f)) this cannot be typecaste because the value is string so not possible
#Arithmetic Operators
z=4
x=2
print("z/x",z/x)
print("z//x",z//x)
print("z%x",z%x)
print("z**x",z**x)
print("z+x",z+x)
#Comparison
ab =5
bc = 10
print(ab==bc)
print(ab!=bc)
print(ab>bc)
#Logical 
q=True
w=False
print(q and w)
print(q or w)
print(not q)


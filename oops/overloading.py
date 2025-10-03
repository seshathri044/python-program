# #Type checking
def fun(arg1,arg2):
    if isinstance(arg1,int):
        if isinstance(arg2,int):
            c = arg1+arg2
            print(c)
    elif isinstance(arg1,str):
        if(arg2,str):
            d= arg1+arg2
            print(d)
fun(1,2)
fun("Hi","Python")
#Another method - Variable length
def fun1(*args):
    if len(args)==1:
        a=args[0]
        c=a*a
        print("the area of square:",c)
    elif len(args)==2:
        b,e=args
        d= 2*(b + e)
        print("The perimeter of rectangle:",d)
fun1(4)
fun1(5,2)
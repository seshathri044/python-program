class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add (self):
        self.c=self.a+self.b
        print("Addition", self.c)
    def sub (self):
        self.c=self.a-self.b
        print("Subtraction", self.c)
    def mul (self):
        self.c=self.a*self.b
        print("multiplication", self.c)
    def div (self):
        self.c=self.a/self.b
        print ("division", self.c)
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
cl=calculator(a,b)
while True:
    x=int(input("choose One \n1.ADD: \n2.SUB: \n3.MUL: \n4.DIV: \n5.Stop:"))
    if x==1:
        cl.add()
    elif x==2:
        cl.sub()
    elif x==3:
        cl.mul()
    elif x==4:
        cl.div()
    else:
        break
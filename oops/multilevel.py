class Pricipal:
    def fun1(self,a):
        self.a=a
        print(a)
        print("The principal")
class Teacher(Pricipal):
    def fun2(self,b):
        self.b=b
        print(b)
        print("The Teacher")
class Student(Teacher):
    def fun3(self,c):
        self.c=c
        print(c)
        print("The Student")
obj = Student()
a=5
b=12
c=13
obj.fun1(a)
obj.fun2(b)
obj.fun3(c)

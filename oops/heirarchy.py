class Parent:
    def func1(self):
        print("This is parent class")
class child1(Parent):
    def func2(self):
        print("This is child 1")
class child2(Parent):
    def func3(self):
        print("This child 2")
obj1 = child1()
obj2 = child2()
obj1.func1()
obj1.func2()
obj2.func3()
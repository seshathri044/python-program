class Parent:
    def func1(self):
        print("Parent Class")
class Child(Parent):
    def func2(self):
        print("Child Class")
object = Child()
object.func1()
object.func2()
class F:
    def fun1():
        print("F class")
class G:
    def fun2():
        print("G class")
class A(F):
    def fun3():
        print("A class")
class B(F):
    def fun4():
        print("B class")
class E(F,G):
    def fun5():
        print("E class")


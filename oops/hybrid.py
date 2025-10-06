class F:
    def fun1(self):
        print("F class")

class G:
    def fun2(self):
        print("G class")

class A(F):
    def fun3(self):
        print("A class")

class B(F):
    def fun4(self):
        print("B class")

class E(F, G):
    def fun5(self):
        print("E class")
        
    # Calling the inherited methods from F and G
    def call_inherited_methods(self):
        self.fun1()  # Calling method from class F
        self.fun2()  # Calling method from class G

# Testing the classes
e = E()
e.fun5()  # Prints "E class"
e.call_inherited_methods()  # Prints "F class" and "G class"

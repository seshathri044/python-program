#Program 1
# class Dog:
#     sound = "bark"
#     def speak(self):
#         print(self.sound)
# dog1 = Dog()
# print(dog1.sound)
# dog1.speak()
#Program
class student:
    def __init__(self,a,b,c):
        self.rollno=a
        self.name=b
        self.age=c
    def display(self):
        print("rollno:",self.rollno)
        print("Name:",self.name)
        print("Age:",self.age)
s1 = student(1,"AAA",22)
s2= student(2,"BBB",20)
s3= student(3,"CCC",23)
s1.display()
s2.display()
s3.display()

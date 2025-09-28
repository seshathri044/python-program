names=["seshathri","vasanth","Karthi99","Yogesh"]
#for
for test in names:
    print(test.upper())
#While
correct_pin="1234"
entered_pin=""
while entered_pin != correct_pin:
    entered_pin = input("enter your correct pin:")
print("Access Granted")
#for and break
for i in range(10):
    if i == 5:
        break
    print(i)
# for and continue
n=[2,-5,7,-9,18]
for num in n:
    if num <0:
        continue
    print(num)

a=5
b="12c"
try:
    z=a+b
except TypeError:
    print("Type error")
try:
    z=int(b)
except ValueError:
    print("Value error")
try:
    ac=[1,2,3]
    print(ac[5])
except IndexError:
    print("Index error")


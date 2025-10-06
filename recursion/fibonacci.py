n=int(input("Enter the number:"))
s=0
def fibonacci(n):
    a=0
    b=1
    print(a,end =" ")
    print(b,end =" ")
    for i in range(n):
        s=a+b
        print(s,end=" ")
        a=b
        b=s
fibonacci(n)
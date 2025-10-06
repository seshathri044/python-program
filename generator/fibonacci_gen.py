def fibonacci(n):
    a=0
    b=1
    print(a,end=" ")
    print(b, end=" ")
    for i in range(n):
        c=a+b
        yield c
        a=b
        b=c
for i in fibonacci(5):
    print(i,end=" ")
i=0
sum=0
while True:
    a=int(input("Enter a value"))
    if a==0:
        break
    else:
        sum = sum + a
        i=i+1
print("Sum",sum)
print("Avg",sum/i)

#Another Method
'''
arr=[]
while True:
    a=int(input("Enter the vslue:"))
    if a!=0:
        arr.append(a)
    else:
        break
total = sum(arr)
print("Sum",total)
print("Avg",total/len(arr))

'''

arr =[1,2,3,1]
a1=arr.append(1)
print(arr)
#print(arr.index[1])
a=arr.count(1)
print(a)
a2=arr.remove(2)
print(arr)
a3=arr.sort()
print(arr)
a4=arr.extend([6,7,8])
print(arr)
a5=arr.insert(3,0)
print(arr)
a6=arr.reverse()
print(arr)
print("len",len(arr))
print("before del",arr)
del arr[3]
print("after del",arr)
a7=arr[2:6]
print(a7)


#O/P
# [1, 2, 3, 1, 1]
# 3
# [1, 3, 1, 1]
# [1, 1, 1, 3]
# [1, 1, 1, 3, 6, 7, 8]
# [1, 1, 1, 0, 3, 6, 7, 8]
# [8, 7, 6, 3, 0, 1, 1, 1]
# len 8
# before del [8, 7, 6, 3, 0, 1, 1, 1]
# after del [8, 7, 6, 0, 1, 1, 1]
# [6, 0, 1, 1]

# 
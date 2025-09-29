set1 = {1,2,3,4}
set2 = {2,3,4,5,6}
union= set1 | set2
print(union)
intersection = set1 & set2
print(intersection)
diff = set1 - set2
print(diff)
Symmetric = set1 ^ set2
print(Symmetric)
subset = set1 <= set2
print(subset)
super = set1 >= set2
print(super)
set3= {10,23,1,2,3}
set4={1,2,3,4}
print(set3>=set4)#super
print(set3<=set4)#subset
#Method
set4.add(5)
print(set3)
set3.update({4,5})
print(set4)
set3.remove(5)
print(set3)
set3.pop()
print(set3)
#Program
print("Program1")
a=[1,2,3,4,4]
b=set(a)
c=list(b)
print(c)
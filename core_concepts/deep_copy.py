import copy
a=[1,2,[3,4]]
b=copy.deepcopy(a)
b[2][0]="new"
b[0]="54"
print("b:",b)
print("a:",a)
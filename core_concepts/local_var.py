a=10

def func():
    #Local variable
    local_var=10
    a=5
    print("the new value:",a)#even though the "a" variable is 10 but inside function the local a is high priority it is caleed "shadowing"
    print("Inside the Function:",local_var)
func()
print("global value:",a)

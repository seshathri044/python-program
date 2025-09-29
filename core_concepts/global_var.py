global_var=10

def modified_global():
    global global_var
    print("before modify:",global_var)
    global_var = 20
    print("Inside the fun:0",global_var)
modified_global()
print("Outside the function:",global_var)
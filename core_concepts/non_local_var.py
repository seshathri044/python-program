def outer_func():
    outer_var =10
    def inner_func():
        nonlocal outer_var
        outer_var = 20
        print("Inner function:",outer_var)
    inner_func()
    print("Outer funcation:",outer_var)
outer_func()
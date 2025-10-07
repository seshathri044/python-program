def loging(fun):
    def inner(username,password):
        if password == 12345:
            print("Authorized User:")
        else:
            print("Unauthorized User:")
        return fun(username,password)
    return inner
@loging
def log_ex(a,b):
    print(a,b)
log_ex("seshathri",12345)
log_ex("vasanth",12367)
log_ex("yogesh",12345)

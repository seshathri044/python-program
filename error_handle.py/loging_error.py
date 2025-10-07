#User Defined Exception
class LogingError(Exception):
    def __init__(self,msg="Invalid User"):
        self.msg = msg
        super().__init__(msg)
try:
    password=int(input("Enter the password"))
    if password ==12345:
        print("Login success")
    else:
        raise LogingError()
except LogingError as e:
    print(f"This the custom login error:{e}")
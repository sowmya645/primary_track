def login(func):
    def wrapper(username,password):
        if username=="admin" and password=="123":
            print("valid user")
            return func(username,password)
        else:
            print("invalid credentials")
            return func(username,password)
    return wrapper
@login
def user(username,password):
    print(" ")
user("admin","1232")
def reg(func):
    def wrapper(fname,lname):
        print(fname)
        print (lname)
        return func(fname,lname)
    return wrapper
@reg
def regis(fname,lname):
    print(" ")
regis("alic","bob")

    
        
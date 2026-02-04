a=input("enter your email:")
s=False
for c in a:
    if(c=='@'):
        print("valid email")
        s=True
        break
if(s==False):
    print("invalid email")
r=False
b=input("enter your password:")
if(len(b)<=8):
    r=True

    print("invalid password")
if(r==False):
    print("valid password")
d=input("enter your name").isalpha()
if(d==True):
    print("name is valid")
else:
    print("name is invalid")
e=input("enter your age:")
if(e.isdigit()):
    print("age is valid")
else:
    print("age is not valid")



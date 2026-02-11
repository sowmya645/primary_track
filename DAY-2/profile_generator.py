<<<<<<< HEAD

def print_data(**kwargs):
    dict={}
    for key,value in kwargs.items():
        dict[key.upper()]=value.strip()
    return dict
name=input("enter name")
age=input("Age")
place=input("location")
email=input("email id")
dict=print_data(name=name,age=age,place=place,email=email)
print(dict)
=======

def print_data(**kwargs):
    dict={}
    for key,value in kwargs.items():
        dict[key.upper()]=value.strip()
    return dict
name=input("enter name")
age=input("Age")
place=input("location")
email=input("email id")
dict=print_data(name=name,age=age,place=place,email=email)
print(dict)
>>>>>>> a81a820bdbc5f1b7d9217ab6fd9a71841d230998

def profile(**kwargs):
    pin={}
    for key,value in kwargs.items():
        pin[key.upper()]=value.strip()
    return pin
dict={}

sum=0
import shutil
pea={}
def finalprice(dict):
    sum=0
    for i in dict.values():
        sum+=i
    return sum
def getdetails():
    name=input("name ")
    location=input("location ")
    phonenumber=input("phone number ")
    restaurant_name=input("name of hotel:")
    pea=profile(name=name,location=location,phonenumber=phonenumber,restaurant_name=restaurant_name)
    return pea
def bill():
    while True:
          item=input("enter item name:")
          amount=eval(input("enter the price of item "))
          dict[item]=amount
          reply=input("are u done")
          if(reply=="YES"):
             sum=finalprice(dict)
             break
    return sum
def display(pea):
    for i in pea:
        pea[i]=pea[i].title()
    print(pea)
    phone=pea["PHONENUMBER"][:2]+"******"+pea["PHONENUMBER"][-2:]
    print(f"{pea["NAME"]} is in {pea["LOCATION"]} went to {pea["RESTAURANT_NAME"]} has a phone number{phone} and made a total bill {sum}.")
def download():
    path=r"C:\Users\91906\OneDrive\Desktop\primary track capg\DAY-2\bill.txt"
    with open(path,"a") as f:
        for key,value in dict.items():
            f.write(f"Items: {key}    amount:{value}")
    print(f"files is downloaded {path}")
    return path
def copy(path):
    dest=r"C:\Users\91906\OneDrive\Desktop\primary track capg"
    shutil.copy(path,dest)

    
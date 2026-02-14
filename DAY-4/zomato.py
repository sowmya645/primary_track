try:
    ite={"apple":30,"kurkure":10,"pizza":300,"momos":200}
    for key,value in ite.items():
        print(f"items:{key}  prize:{value}")
    while True:
        item=input("enter name of the item")
        quantity=eval(input("enter qunatity per item"))
        if quantity<=0:
            raise Exception("quantity cannot be zero")
        total_cost=ite[item]*quantity
        inp=input("do you want to add more items?")
        if inp!="YES":
            break
    print(f"total price: {total_cost}")
except ValueError as e:
    print("please enter a right value",e)
except Exception as e:
    print("exception occured")
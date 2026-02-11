

for i in range (1,5):
    password=eval(input("enter crct passowrd"))
    user=input("enter username")
    if(i==4): 
        print("all attempts failed")
        break
    if(password==123 and user=="admin"):
        print("crct")
        break
    else:
        print(f"you have {4-i} attempts")
        
        


fullname="gunda sowmya"
initials=fullname.split(" ")
for i in initials:
    print(i[0],end="")

initials="".join(word[0].upper() for word in fullname.split())
print(initials) 
marks=eval(input("enter marks"))
attendance=eval(input("enter attendance"))
if(marks>=50 and attendance>=75):
    print("eligible")
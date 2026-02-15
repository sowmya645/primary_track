file=open("notes.txt","w")
file.write("welcome\n")
file.write("this is a sample file\n")
file.close()
file=open("notes.txt","r")
content=file.read()
print(content)
file.close()
file=open("notes.txt","a")
file.write("primary\n")
file.close()
with open("notes.txt","r") as file:
    content=file.read()
    print(content)
with open("notes.txt","r") as file:
    print(file.readline().strip())
    print(file.readline().strip())
    print(file.readline().strip())
with open("notes.txt","r") as file:
    while True:
        line=file.readline()
        if not line:
            break
        print(line.strip())
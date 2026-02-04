errors=[]
with open("log3.log","r") as f:
    lines=f.readlines()
    for line in lines:
        words=line.split(" ")
        for word in words:
            if word=="ERROR":
                errors.append(line)
with open("error.txt","w") as f:
    for wo in errors:
        f.write(wo)
        
    
            
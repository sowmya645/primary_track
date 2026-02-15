lis=["1","2","3","4","5"]
with open("bye.csv","w") as f:
    for i in lis:
        f.write(i+"\n")
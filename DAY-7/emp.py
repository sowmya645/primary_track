with open("employee.csv","r")as f:
    lines=f.readlines()
    for line in lines:
        print(line)
while True :
  choice = int(input("Enter 1.write file 2. read file"))
  match choice :
    case 1 :
      with open(r"C:\Users\91906\OneDrive\Desktop\task.txt", "a") as f:
        f.write("hello world")
    case 2 :
      with open(r"C:\Users\91906\OneDrive\Desktop\task.txt", "r") as f:
        print(f.read())
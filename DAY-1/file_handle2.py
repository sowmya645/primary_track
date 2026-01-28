import shutil
import datetime
import os
source = r"C:\Users\91906\OneDrive\Desktop\primary track capg\DAY-1\todo.txt"

backup = rf"C:\Users\91906\OneDrive\Desktop\primary track capg\DAY-1\d{datetime.date.today()}e.txt"

shutil.copy(source,backup)
print(f"backup of {source} created at {backup}")

ne=r"C:\Users\91906\OneDrive\Desktop\primary track capg\backup_1"
os.mkdir(ne)
fe=rf"{ne}\fr{datetime.date.today()}.txt"
shutil.copy(source,fe)

print(f"backup of {source} created at {fe}")
import shutil
import datetime
source="C:\Users\91906\OneDrive\Desktop\primary track capg\DAY-1\todo.txt"
backup=f"C:\Users\91906\OneDrive\Desktop\primary track capg\DAY-1\de.txt"
shutil.copy(source,backup)
print(f"backup of {source} created at {backup}")
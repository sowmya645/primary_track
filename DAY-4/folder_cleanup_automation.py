import os
import shutil
path=r"C:\Users\91906\OneDrive\Desktop\temp"
for file in os.listdir(path):
    fil=os.path.join(path,file)
    if os.path.isdir(fil):
        os.rmdir(fil)
    else:
        os.remove(fil)
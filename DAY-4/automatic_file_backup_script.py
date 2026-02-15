import datetime
import shutil
from pathlib import WindowsPath
path=input("enter path: ")
np=WindowsPath(path.replace('"',''))
t=datetime.datetime.now().strftime("%d_%m_%Y, %H_%M_%S")
newpath=rf"C:\Users\91906\OneDrive\Desktop\bill_{t}.txt"
shutil.copy(np,newpath)
import os
from pathlib import WindowsPath
path=input("enter path: ")
np=WindowsPath(path.replace('"',''))
dd=input("give the new name to rename:")
rn=WindowsPath(dd.replace('"',''))
os.rename(np,rn)
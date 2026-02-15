import shutil
total,used,free=shutil.disk_usage("/")
gb=1024**3
print(f"the total memory space available is {total/gb:.2f}GB")
print(f"the used memory space available is {used/gb:.2f}GB")
print(f"the free memory space available is {free/gb:.2f}GB")

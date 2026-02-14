import psutil 
mem=psutil.virtual_memory()
gb=1024**3
print(f"the total memory space available is {mem.total/gb:.2f}GB")
print(f"the used memory space available is {mem.used/gb:.2f}GB")
print(f"the free memory space available is {mem.free/gb:.2f}GB")
while True:
    print(psutil.cpu_percent(interval=1))

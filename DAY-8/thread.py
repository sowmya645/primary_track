# import time
# def task():
#     print("task started")
#     time.sleep(2)
#     print("task completed")
# task()
# print("finished")
import threading
import time
from urllib.request import urlretrieve
# def greet(name):
#     print(f"hello {name}")
# t=threading.Thread(target=greet,args=("Alice",))
# t.start()
# def gree(name):
#     print(f"hello {name}")
# gree("Alice")
def work(num):
    print(f"worker {num} is working")
    time.sleep(2)
    print(f"worker {num} is finished")
for i in range (5):
    t=threading.Thread(target=work,args=(i,))
    t.start()
# destination="s.pdf"
# def download():
#     url="https://dspmuranchi.ac.in/pdf/Blog/JAVA%20thread.pdf"
#     fil,headers=urlretrieve(url,destination)
#     time.sleep(2)
#     print(f"done downloading {fil} ")
    
# t=threading.Thread(target=download)
# t.start()
# t.join()


import shutil
import os
import datetime
def writef():
    path= r"C:\Users\91906\OneDrive\Desktop\bill"
    if not  os.path.isdir(path):
        with open("bill.txt","a"):
            pass
    t=datetime.date.today()
   
    with open(path,"a") as f:
        f.write(f"time is {t} sow")
import schedule 
import time
schedule.every(1).minutes.do(writef)
while True:
    schedule.run_pending()
    time.sleep(1)

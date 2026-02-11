import time

def cal(n):
    print("Starting calculation.")
    start_time = time.time()   
    total = 0
    for i in range(n):
        total += i
    end_time = time.time()     
    print("Calculation finished.")
    print(f"Sum of numbers up to {n}: {total}")
    print(f"Start time: {start_time}")
    print(f"End time: {end_time}")
    print(f"Execution time: {end_time - start_time} seconds")

cal(1000000000)
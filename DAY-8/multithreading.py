# from multiprocessing import Process
# def worker():
#     print("worker is running")
# if __name__=="__main__":
#     p=Process(target=worker)
#     p.start()
#     p.join()
#     print("finished main")
# import time
# from multiprocessing import Pool
# def square(n):
#     return n*n
# if __name__=="__main__":
#     numbers=[10**7,10**2]
#     start=time.time()
#     with Pool() as p:
#         results=p.map(square,numbers)
#     end=time.time()

#     print("reults:",results)
#     print("",end-start)
def worker(q):
    q.put('hello')

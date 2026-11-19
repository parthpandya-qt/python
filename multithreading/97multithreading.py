
import threading
import time

def function1(num):
    time.sleep(num)
    print("Function completed")

t1= threading.Thread(target=function1, args=[4])
t2= threading.Thread(target=function1, args=[3])   
t3= threading.Thread(target=function1, args=[1])    

time1 = time.perf_counter()
t1.start()
t2.start()      
t3.start()
time2 = time.perf_counter()

print(time2 - time1)




time3 = time.perf_counter()
t1.join()
t2.join()       
t3.join()
time4 = time.perf_counter()
print(time4 - time3)







import time
def timeLimit(t):
    time.sleep(t)
    print(f"Function completed after {t} seconds")


# def normalExecution():
#     time1 = time.perf_counter()
#     timeLimit(1)
#     timeLimit(2)
#     timeLimit(3)
#     timeLimit(4)
#     time2 = time.perf_counter()
#     print(time2 - time1)
# normalExecution()

time1 = time.perf_counter()
from concurrent.futures import ThreadPoolExecutor   
with ThreadPoolExecutor(max_workers=10) as executor:
    future0 = executor.submit(timeLimit, 1)
    
    future1 = executor.submit(timeLimit, 2)
    
    future2 = executor.submit(timeLimit, 3)
    
    future3 = executor.submit(timeLimit, 4)
    print(future0.result())
    print(future1.result())
    print(future2.result())
    print(future3.result())
time2 = time.perf_counter()
print(time2 - time1)
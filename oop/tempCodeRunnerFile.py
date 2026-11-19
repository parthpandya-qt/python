

import multiprocessing
import time
import os

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

def multiprocessingExecution():
    time1 = time.perf_counter()
    pros = []
    prosID = []
    for t in [1, 2, 3, 4]:
        process = multiprocessing.Process(
            target=timeLimit,
            args=[t]
        )
        process.start()
        pros.append(process)
        prosID.append(os.getpid())

    for process in pros:
        process.join()

    time2 = time.perf_counter()
    print(time2 - time1)
    for id in prosID:
        print(f"Process ID: {id}")

if __name__ == "__main__":
    # normalExecution()
    multiprocessingExecution()
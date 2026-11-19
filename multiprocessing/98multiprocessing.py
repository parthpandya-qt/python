import multiprocessing

import requests

def download(url, name):
    response = requests.get(url)
    print(f"Downloading {name}...")
    with open(f"multiprocessing/{name}", "wb") as f:
        f.write(response.content)
    print(f"{name} downloaded successfully.")
url = "https://picsum.photos/2000/3000"

if __name__ == "__main__": 
    pros = []
    for picture in range(1, 6):
        # download(url, f"pic{picture}.jpg")
        process = multiprocessing.Process(
            target=download,
            args=[url, f"pic{picture}.jpg"]
        )
        process.start()
        pros.append(process)

    for process in pros:
        process.join()




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
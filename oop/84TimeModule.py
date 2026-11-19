import time
print(time.time())  # e.g., 1724869542.12345


print("Start")
time.sleep(2)  # Sleep for 2 seconds
print("End")


lt = time.localtime()
print(lt)  # time.struct_time(tm_year=2025, tm_mon=6, ...)

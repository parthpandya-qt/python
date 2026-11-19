# What is a daemon thread?
# A daemon thread is a background thread that doesn’t keep the Python program running.

# When the main program finishes, Python waits for regular (non-daemon) threads to finish. But it does not wait for daemon threads: the program can exit while they’re still running. They may stop abruptly, so they might not finish their current work or clean up resources



import threading
import time

def background_work():
    while True:
        print("Background work...")
        time.sleep(1)

thread = threading.Thread(target=background_work, daemon=True)
thread.start()

print("Main program is done")
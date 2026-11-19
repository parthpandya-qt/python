# Producer Consumer Problem: One thread produces data that another thread consumes. The producer and consumer threads must be synchronized so that the consumer does not try to consume data that has not yet been produced.

# Use the synchronization tool that fits the problem. These are the main ones in threading:
# Lock
# Allows one thread at a time to enter a protected section. Use it to protect shared mutable data.




import threading
import asyncio

# ============================================================
# LOCK TYPES IN PYTHON
# ============================================================

# ------------------------------------------------------------
# 1. Lock
# Basic mutual-exclusion lock.
# - Only one thread can hold it at a time.
# - Not reentrant: acquiring it twice in the same thread deadlocks.
# - Any thread can release it, not just the one that acquired it.
# ------------------------------------------------------------
lock = threading.Lock()

with lock:
    # critical section: only one thread runs this at a time
    pass

# ------------------------------------------------------------
# 2. RLock (Reentrant Lock)
# - The same thread can acquire it multiple times without deadlock.
# - Must be released the same number of times it was acquired.
# - Useful for recursion or nested calls that both need the lock.
# ------------------------------------------------------------
rlock = threading.RLock()

with rlock:
    with rlock:   # safe: same thread re-acquiring
        pass

# ------------------------------------------------------------
# 3. Semaphore
# - Allows up to N threads into a section at the same time.
# - Good for limiting access to a resource (e.g. DB connections).
# ------------------------------------------------------------
semaphore = threading.Semaphore(3)   # max 3 threads at once

with semaphore:
    pass

# ------------------------------------------------------------
# 4. BoundedSemaphore
# - Like Semaphore, but raises ValueError if released more times
#   than it was acquired. Helps catch bugs.
# ------------------------------------------------------------
bounded_sem = threading.BoundedSemaphore(3)

# ------------------------------------------------------------
# 5. Condition
# - Lets threads wait until a condition becomes true.
# - wait() blocks, notify() wakes one thread, notify_all() wakes all.
# - Wraps a lock internally (Lock or RLock).
# - Common in producer/consumer patterns.
# ------------------------------------------------------------
condition = threading.Condition()

with condition:
    # condition.wait()        # wait until notified
    # condition.notify()      # wake one waiting thread
    # condition.notify_all()  # wake all waiting threads
    pass

# ------------------------------------------------------------
# 6. Event
# - A simple flag shared between threads.
# - wait() blocks until another thread calls set().
# - clear() resets the flag, is_set() checks it.
# ------------------------------------------------------------
event = threading.Event()

# event.set()     # signal: flag becomes True, waiting threads continue
# event.wait()    # block until flag is True
# event.clear()   # reset flag to False

# ------------------------------------------------------------
# 7. Barrier
# - Makes a fixed number of threads wait for each other.
# - All threads continue only once everyone has reached the barrier.
# ------------------------------------------------------------
barrier = threading.Barrier(3)   # waits for 3 threads

# barrier.wait()   # block until 3 threads have called this

# ------------------------------------------------------------
# 8. multiprocessing locks
# - multiprocessing.Lock, RLock, Semaphore, Condition, Event, Barrier
# - Same idea as above, but work across separate PROCESSES,
#   not just threads.
# ------------------------------------------------------------

# ------------------------------------------------------------
# 9. asyncio locks
# - asyncio.Lock, Semaphore, Condition, Event
# - For coroutines; use with "async with".
# - NOT thread-safe.
# ------------------------------------------------------------
async_lock = asyncio.Lock()

async def example():
    async with async_lock:
        pass

# ------------------------------------------------------------
# 10. GIL (Global Interpreter Lock)
# - Internal CPython lock: only one thread executes Python bytecode
#   at a time.
# - Does NOT replace the need for your own locks when sharing data.
# ------------------------------------------------------------










import threading, queue, time

q = queue.Queue()

def producer():
    for i in range(100):
        print("Produced", i)
        q.put(i)                 # add item
        time.sleep(0.5)
    q.put(None)                  # sentinel: "no more items"

def consumer():
    while True:
        item = q.get()           # waits (blocks) until an item is available
        if item is None:
            break
        print("Consumed", item)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start(); t2.start()
t1.join(); t2.join()
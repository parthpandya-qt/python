"""
RACE CONDITION AND THREADING LOCK - THEORY NOTES

=====================================================================
PART 1: RACE CONDITION
=====================================================================

WHAT IS A RACE CONDITION?
A race condition happens when the result of a program depends on the timing
or order in which multiple threads/processes access SHARED data, and at least
one of them modifies it. The threads "race" each other, and whoever gets
there first changes the outcome.

SIMPLE ANALOGY
A shared notebook has the number 5 written in it. You and a friend both want
to add 1:
    1. You read the notebook: 5
    2. Your friend reads the notebook: 5 (before you write anything)
    3. You write 6
    4. Your friend also writes 6
Expected 7, got 6. One update was lost.

WHY IT HAPPENS IN CODE
`counter += 1` looks like one step, but it is actually three:
    1. READ   the current value of counter
    2. ADD    1 to it
    3. WRITE  the result back
Two threads can interleave these steps:
    Thread 1: READ  (counter = 5)
    Thread 2: READ  (counter = 5)    <- reads before Thread 1 writes
    Thread 1: WRITE (counter = 6)
    Thread 2: WRITE (counter = 6)    <- overwrites Thread 1's work
Expected 7, got 6.

TWO COMMON FORMS
1. Read-modify-write : read a value, change it, write it back (lost updates).
                       Example: shared counter.
2. Check-then-act    : check a condition, then act on it, but the condition
                       changes in between.
                       Example: two people both see "1 ticket left" and both
                       buy it; two withdrawals both pass the balance check.

WHY IT IS DANGEROUS
- Non-deterministic: same code gives different results on different runs.
- Hard to reproduce: adding a print or using a debugger changes timing and
  can hide the bug.
- Silent: no error or exception, just wrong data.
- Often works in testing but fails in production under heavy load.

NOTE ON THE GIL
Python's GIL does NOT protect against this. Threads can be switched between
bytecode instructions, and `+=` spans several of them. The bug is real even
if a particular run looks correct.

WAYS TO FIX IT
1. Locks             : allow only one thread in the critical section at a time.
2. Queues            : workers send results to a thread-safe queue and ONE
                       owner updates the shared state.
3. Avoid sharing     : give each thread its own copy of the data, combine the
                       results at the end.
4. Immutable data    : if nothing is modified, nothing can race.
5. Atomic DB ops     : transactions, row locks, atomic UPDATE statements,
                       unique constraints.

=====================================================================
PART 2: LOCK IN THREADING
=====================================================================

WHAT IS A LOCK?
A Lock is a synchronization tool that allows only ONE thread at a time to
execute a particular section of code. Any other thread that wants to enter
that section must wait until the lock is released.
Analogy: a bathroom key. One person holds the key, everyone else waits.

HOW A LOCK FIXES THE RACE CONDITION
The lock makes the three steps (read, add, write) finish completely before
another thread is allowed to start them.

KEY TERMS
- Critical section : code that touches shared data and must not be run by
                     two threads at once.
- acquire()        : take the lock (waits if another thread holds it).
- release()        : give the lock back.
- Blocking         : a thread waits until the lock becomes free.

HOW TO USE
1. Manual way:
       lock.acquire()
       ...critical section...
       lock.release()
   Risky: if an exception occurs, release() never runs and all other
   threads wait forever.

2. Recommended way (with statement):
       with lock:
           ...critical section...
   The lock is released automatically, even if an error occurs.

USEFUL OPTIONS
- lock.acquire(blocking=False) : do not wait; returns True if acquired,
                                 False otherwise.
- lock.acquire(timeout=3)      : wait at most 3 seconds.
- lock.locked()                : True if the lock is currently held.

TYPES OF LOCKS
- Lock       : basic lock. If the same thread tries to acquire it twice,
               it gets stuck (deadlock).
- RLock      : re-entrant lock. The same thread can acquire it multiple
               times, but must release it the same number of times.
- Semaphore  : allows up to N threads inside at once.
- Condition  : threads wait until they are notified that something happened.
- Event      : a simple flag; threads wait until another thread sets it.

DEADLOCK
Happens when two threads each hold one lock and wait for the other's lock,
so both wait forever.
    Thread 1 holds A, wants B
    Thread 2 holds B, wants A
Fix: always acquire multiple locks in the same order everywhere.

BEST PRACTICES
- Prefer `with lock:` over manual acquire/release.
- Keep the critical section as small as possible.
- Do not do slow work (network calls, sleep) while holding a lock.
- Use the SAME lock for all access to the same shared data.
- Acquire multiple locks in a consistent order to avoid deadlock.

SUMMARY
A race condition is a bug caused by unsynchronized access to shared data.
A Lock provides mutual exclusion: only one thread runs the critical section
at a time, which prevents the race condition.
"""




import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        # lock.acquire()
        # counter += 1
        # lock.release()
        with lock:
            counter += 1


t1= threading.Thread(target=increment)
t2= threading.Thread(target=increment)
t3= threading.Thread(target=increment)   

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print(f"Final counter value: {counter}")
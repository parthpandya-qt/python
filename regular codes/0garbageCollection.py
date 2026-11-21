'''


Garbage Collection (GC) in Python is the process of automatically identifying and freeing memory that is no longer being used by a program.

In simple words, when objects are no longer needed, Python's garbage collector helps remove them from memory so that memory can be reused.
1. How does garbage collection work?
Python primarily uses two mechanisms:
1. Reference Counting
2. Cyclic Garbage Collection
1. Reference Counting
Every Python object maintains a reference count.

The reference count represents how many references point to that object.

Example:
a = [10, 20, 30]  # Reference count = 1b = a             # Reference count = 2c = a             # Reference count = 3del b             # Reference count = 2del c             # Reference count = 1del a             # Reference count = 0



When the reference count becomes zero, CPython immediately deallocates the object.
2. Cyclic Garbage Collection
Sometimes objects reference each other, creating a cycle.

Example:
class Demo:    passa = Demo()b = Demo()a.ref = bb.ref = adel adel b



Here:
- Object a references object b.
- Object b references object a.
- Both reference each other.
Even after deleting a and b, their reference counts are not zero.

Python's cyclic garbage collector detects such unreachable reference cycles and collects them.
2. Python garbage collection module
Python provides a built-in gc module to interact with the garbage collector.
import gc# Check whether garbage collection is enabledprint(gc.isenabled())# Manually trigger garbage collectiongc.collect()# Disable garbage collectiongc.disable()# Enable garbage collectiongc.enable()



3. Interview questions
Q1. Is garbage collection automatic in Python?

Yes. Python automatically manages memory using reference counting and cyclic garbage collection in CPython.

Q2. What is the difference between reference counting and garbage collection?
Reference Counting	Cyclic GC
Tracks object references	Detects unreachable reference cycles
Frees objects when count reaches zero	Handles circular references
Immediate in CPython	Runs periodically or manually

Q3. Can Python have memory leaks despite garbage collection?

Yes. For example, if your program maintains unnecessary references to objects, Python cannot collect them because they are still reachable.

Q4. Does del directly free memory?

No. del removes a reference (or name). If the object's reference count reaches zero in CPython, the object is deallocated.


'''
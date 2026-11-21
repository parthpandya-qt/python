
'''
In Python, shallow copy and deep copy are two ways to create copies of objects.

The main difference is how they handle nested objects (objects inside objects).
1. Shallow Copy
A shallow copy creates a new outer object, but the nested objects are still shared between the original and copied objects.

We can create a shallow copy using:
- copy.copy()
- Slicing for lists: list[:]
- list.copy()
Example:
import copyoriginal = [[1, 2], [3, 4]]shallow = copy.copy(original)shallow[0][0] = 100print(original)print(shallow)



Output:
[[100, 2], [3, 4]]
[[100, 2], [3, 4]]


Why did the original list change?

Because both lists share references to the same nested lists.
Shallow copy memory representation
Original
[[1, 2], [3, 4]]

Shallow copy
[[1, 2], [3, 4]]



Shared nested objects

Both lists point to the same inner lists.


2. Deep Copy
A deep copy creates a new outer object and recursively copies the nested objects as well.

We create it using copy.deepcopy().

Example:
import copyoriginal = [[1, 2], [3, 4]]deep = copy.deepcopy(original)deep[0][0] = 100print(original)print(deep)



Output:
[[1, 2], [3, 4]]
[[100, 2], [3, 4]]


Why did the original list not change?

Because deep copy creates independent copies of the nested objects.
Deep copy memory representation
Original
[[1, 2], [3, 4]]

Deep copy
[[1, 2], [3, 4]]


Original nested lists
Independent

Copied nested lists
Independent



3. Shallow Copy vs Deep Copy
Feature	Shallow Copy	Deep Copy
New outer object	Yes	Yes
Nested objects copied	No	Yes
Nested objects shared	Yes	No
Memory usage	Generally lower	Generally higher
Speed	Generally faster	Generally slower
Python method	copy.copy()	copy.deepcopy()

'''
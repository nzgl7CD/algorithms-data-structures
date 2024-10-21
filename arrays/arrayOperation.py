import array as arr
import numpy as np

'''
Access -> O(1) because:
1. Arrays have continuous memory allocation. When an array is created, the elements are stored in contiguous memory blocks. 
This means that the memory address of each element is directly calculated based on its index. This also means it has a fixed size and might need
generate a new array if additional elements are inserted.

2. Index calculation: address-of-element=base-address-of-array+(index*size-of-each-element)

3. Direct access: Once the address is calculated, the system can directly retrieve the value stored at that memory location, 
which is why accessing an element by index is O(1).

'''

# Array
# 'i' is a unicode of data type, where i=int, h=short int, f=float, d=double, and u=characters
# the letter in upper case is unsigned -> i=signed int, I=unsigned int
# unsigned can only represent positive numbers and signed can represent both 
array1= arr.array('i',[1,2,3,4,5]) # Only allow homogeneous data types: Access avg = Avg O(1)
peek_el=array1[1] # -> O(1)
array1.append(1) # -> O(n): makes a new list
array1.remove(1) # removes the first element=1 that appears -> O(1)
array1.pop(0) #removes and return the firs element -> O(1)

array2=np.array([1,2,3,45])
first_element=array2[1] # = 2 -> O(1)
# array2.append(1) raise error (fixed size)



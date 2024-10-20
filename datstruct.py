'''
- For access: always try to use array (numpy or array)
- For push/pop: Tru to use Stack, dictionary or set
'''


import array as arr
from collections import deque

# List/Stack -> it's a stack if you only use pop and append but not[]
list1=[2,3,4,"test"] # Allows all sort of types: Access avg = O(N)
list1.append(1) # Push element to the end of stack: list1=[2,3,4,"test",1]
last_element=list1.pop() # = 1 ->O(1)
last_element=list1.pop(0) # = 2 ->O(n) queue
peek_element=list1[-1] # =1 ->O(1) stack
peek_element=list1[1]  # =1 ->O(1) list

# Array
array1= arr.array('i',[1,2,3,4,5]) # Only allow homogeneous data types: Access avg = Avg O(1)
peek_el=array1[1] # -> O(1)
array1.append(1) # -> O(1)
array1.remove(1) # removes the first element=1 that appears -> O(1)
array1.pop(0) #removes and return the firs element -> O(1)

# Queue: FIFO Principle 
queue=deque()
queue.append(1)
queue.append(2) # -> O(1)
first_element=queue.popleft() # Remove element from front of queue -> O(1)
first_element=queue[0] # Peek first element -> O(1)


# Dictionaries
dict={'Name': 'Seb', 1: [1,2,3,4]}
access_by_key=dict[1] # -> O(1) 
access_w_get=dict.get(1) # ->  O(1)
dict.pop(1) # Delete key and values -> O(1)
myDict = {x: x**2 for x in [1,2,3,4,5]}

# Tuples
tuple1 = ('Geeks', 'For') # CAn have strings
my_tuple = (1, 2, 3, "hello", 4.5) # Can have heterogeneous types

single_element_tuple = (5,)  # Correct way to define a single-element tuple: without , it's just an integer 
tuple2=tuple([1,2,3,4,5])

first_el=tuple2[0] # -> O(1)
sliced_tuple=tuple2[1:3] # =[2,3,4] -> O(k), where k is the number of elements in the slice (3)
combined_tuples=single_element_tuple+tuple2 # = (5,1,2,3,4,5)
a, b, c, d, e = tuple2 #must have same number of variables as elements

#Sets
Set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks']) #can use {1, 2, 'Geeks', 4, 'For', 6, 'Geeks'}
Set.add(30) # Adds in the back like append in stacks: O(1)
Set.remove(30) # Removes if element exists, and raise error if it doesn't exists: O(1)
Set.discard(30) # Remove if element exists, and DOES NOT raise error if it doesn't exists: O(1) 
new_set={1,25}

combined_sets=Set.union(new_set) # sorts it: -> O(len(Set)+len(new_set))

intersection_set = Set.intersection(new_set) # Makes new sets with only common elements from both sets: ={1}: -> O(len(Set)+len(new_set))

difference_set =Set.difference(new_set) # Gives elements from the first set (Set) that doesn't exists in the second set (new_set): -> O(len(Set))
symmetric_difference_set =Set.symmetric_difference(new_set) # Gives elements from both sets that the other doesn't have

#Frozen set: immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied.
f_set=frozenset([1,2,3])
n_set={1,2,4}
diff=f_set.difference(n_set) # we can do the same as we do with sets but not change the variable (add, remove, discard)

#String
string="Algdat practice"
first_letter=string[0] # ->O(1)
slice_string=string[1:3] # -> O(k) also [start:stop:step]

new_string=string+" is fun" # -> O(n)
length=len(string) # -> O(1)

find_letter=string.find('Algdat') # -> O(m*n), where n=len(string) and m=len('Algdat')
is_in= 'A' in string # Bool output: -> O(n)

s='b'
order=ord(s) - ord('a') + 1 # return 2 as b is the second letter in the alphabet

orderlist=[ord(char.lower()) - ord('a') + 1 for char in s if char.isalpha()]

# print(ord('5')-ord('0'))



#Bits
a = 10 #int 0b1010
b = 3  #int 0b0011
and_result = a & b # =0b0010 as an int (2): doesn't work with bin(10) as this gives a string

bin_and_result=bin(and_result)

or_result= a|b # one of or both 

xor_result=a^b # =0b1001 only one of them but not both

not_result=~b # reverse all bins

multiply_val=a<<1 # multiply by 2^1 
multiply_val_val=a<<2 # multiply by 2^2

divide_val=a>>1 # dive by 2^1
divide_val=a>>2 # divide by 2^2 (4)

a |= (1 << 2) # sets the second bit to 1 = 0b1110 
a &= ~(1 << 2) # reverse the second bit to 0 = 0b1010

is_set = (a & (1 << 1)) != 0
a&=~(1) #makes any number pair

a ^= b # reduce a with what only b has in bits 


























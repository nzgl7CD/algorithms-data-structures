'''
Lists:
- No specific order requirement
- append() adds to the end
- pop() can remove the last element or any specific index
- Lists allow insert() at any position (O(n) operation)
- Can access any element by index
- Constant time for append/pop at end but O(n) for operations elsewhere
- Lists are mutable, but stacks maintain strict LIFO order
'''
list = []

# Pushing elements onto the list (push operation)
list.append(1)
list.append(2)
list.append(3)
list.insert(0,4) #-> [4, 1, 2, 3]

# Popping elements from the list (pop operation)
list.pop(0) #-> pops fist element, list=[1, 2, 3]

# Checking the second element of the list
list[1] #-> 2
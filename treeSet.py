'''
Python does not have a direct equivalent of Java's TreeSet in its standard library. 
However, you can achieve similar functionality by using the sortedcontainers module, 
which provides a SortedSet class, or by using set with manual sorting.
'''

my_set = set()

# Add elements
my_set.add(10)
my_set.add(5)
my_set.add(20)
my_set.add(15)

# Display the set in sorted order
print("Sorted set:", sorted(my_set))

# Check if a specific element exists
print("Contains 15?", 15 in my_set)

# Remove an element
my_set.remove(10)
print("Sorted set after removing 10:", sorted(my_set))

# Retrieve the smallest and largest elements
print("Smallest Element:", min(my_set))
print("Largest Element:", max(my_set))
'''
A node is larger og equal to its child nodes
'''
import heapq

# Create an empty max-heap
max_heap = []

# Adding elements (negated values)
heapq.heappush(max_heap, 30)  
heapq.heappush(max_heap, 20)  
heapq.heappush(max_heap, 25)  
heapq.heappush(max_heap, 10)
heapq.heappush(max_heap, 15)
heapq.heappush(max_heap, 5)
  

# Creating the following Max Heap
#      30
#     /  \
#    20   25
#   / \   /
#  10 15 5

print("Max heap after pushes:", [-x for x in max_heap])  # Negate back for display

# Accessing the largest element
largest = -max_heap[0]
print("Largest element:", largest)

# Removing the largest element
removed = -heapq.heappop(max_heap)
print("Removed largest element:", removed)

print("Max heap after removal:", [-x for x in max_heap])  # Negate back for display

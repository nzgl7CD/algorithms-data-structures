import heapq

# Heap Sort: Can sort an iterable in O(n*logn) time complexity. 

# empty heap
min_heap = []

# push nodes
heapq.heappush(min_heap, 30)  
heapq.heappush(min_heap, 20)  
heapq.heappush(min_heap, 25)  
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 15)
heapq.heappush(min_heap, 5)

# Creating the following Min Heap
#      5
#     / \
#    10  25
#   / \  /
#  30 15 20

print("Heap after pushes:", min_heap)

# Accessing the smallest element
smallest = min_heap[0]
print("Smallest element:", smallest)

# Removing the smallest element
removed = heapq.heappop(min_heap)
print("Removed smallest element:", removed)

# Accessing the smallest element after removing the previous smallest
print("Heap after removal:", min_heap)
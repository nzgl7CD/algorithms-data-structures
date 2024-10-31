'''
In python we can reconstruct a treeset (from java) with SortedSet 
'''
from sortedcontainers import SortedSet

def sortedSet(arr):
    sorted_set=SortedSet()
    sorted_set.update(arr)
    return sorted_set

print(sortedSet([2,1,5,4,3,6,9,7]))
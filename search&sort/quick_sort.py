
def quickSort(arr):
    
    if not arr: return []
    pivot=arr[0]
    left=[i for i in arr[1:] if i<pivot]
    right=list(filter(lambda x: x>pivot, arr[1:]))
    return quickSort(left)+[pivot]+quickSort(right)

print(quickSort([2,4,1,3,6,5,4]))


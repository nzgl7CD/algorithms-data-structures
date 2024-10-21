
def quickSort(arr):
    if not arr: return [] # to avoid indexerror exception
    pivot=arr[0]
    left=list(filter(lambda x: x<pivot, arr[1:]))
    right=[i for i in arr[1::] if i>=pivot]
    return quickSort(left) + [pivot] + quickSort(right)
    
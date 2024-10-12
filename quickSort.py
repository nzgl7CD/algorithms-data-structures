def quick(arr:list[int])->list[int]:
    if len(arr)<=1: return arr
    pivot=arr[0]
    left=list(filter(lambda x: x<pivot, arr[1:]))
    right=[x for x in arr[1:] if x>=pivot]
    return quick(left)+[pivot]+quick(right)

print(quick([0,0,1,2,1,0,1,1]))
def quick(arr:list[int])->list[int]:
    if len(arr)<=1: return arr
    pivot=arr[0]
    left=list(filter(lambda x: x<pivot, arr[1:]))
    right=[x for x in arr[1:] if x>=pivot]
    return quick(left)+[pivot]+quick(right)

def bubbleSort(arr:list[int])->list[int]:
    if len(arr)<=1: return arr
    for n in range(len(arr)-1,0,-1):
        for i in range(n):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
print(bubbleSort([2,1,4,3,6,5]))    


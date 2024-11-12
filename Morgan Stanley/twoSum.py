def twoSum(arr,target):
    if not arr: return None
    dict={}
    for idx, num in enumerate(arr):
        temp=target-num
        if temp in dict:
            return dict[temp], idx
        dict[num]=idx
    return None

print(twoSum([1,2,3,4],3))

def sumTwo(arr,target):
    if not arr: return ()
    
    checker={}
    for idx, val in enumerate(arr):
        temp=target-val
        if temp in checker: return checker[temp], idx
        checker[val]=idx
    return ()

print(sumTwo([1,2,3,4],7))
    
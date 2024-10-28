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
        
    
def greedyNumber(arr:list[int])->int: #max profit
    if len(arr)<=1:return 0
    min_num=float('inf')
    max_num=0
    for i in arr:
        if i<min_num:min_num=i
        max_num=max(i-min_num,max_num)
    return(max_num)

def kadunaAlg(arr: list[int]) -> int: # max subproduct
    if len(arr) == 0:
        return 0
    max_so_far=float('-inf')
    max_ending_here=0
    for i in arr:
        max_ending_here+=i
        if max_ending_here>max_so_far: max_so_far=max_ending_here
        
        if max_ending_here<=0: max_ending_here=0
    return max_so_far

def greedySub(arr:list[int])->list[int]: #max sub array
    if len(arr)<=1: return arr
    max_so_far=float('-inf')
    max_ends_here=0
    max_array=[]
    for i in arr:
        max_ends_here+=i
        if max_ends_here>max_so_far: 
            max_so_far=max_ends_here
            max_array.append(i)
        if max_ends_here<0: 
            max_ends_here=0
            max_array=[]
    return max_array


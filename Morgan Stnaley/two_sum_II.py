def two_sum_II(nums:list[int], target)->list[any]:
    '''
    The array input is sorted
    '''
    if not nums:return []
    
    left,right=0,len(nums)-1
    
    while left!=right:
        temp=nums[left]+nums[right]
        if temp==target: return left, right
        elif temp>target: right-=1; continue
        left+=1
    return []

print(two_sum_II([1,3,5,8],4))
    
    
    
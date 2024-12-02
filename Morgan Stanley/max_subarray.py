def maxSubArray(nums: list[int]) -> int:
    if not nums: return 0
    current_max=nums[0]
    final_max=nums[0]
    for i in nums[1:]:
        current_max=max(i,current_max+i)
        final_max=max(final_max,current_max)
    return final_max


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    
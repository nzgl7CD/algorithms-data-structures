def missing_number(nums:list[int])->int:
    if not nums: return 0
    n=len(nums)
    expected_sum=n*(n+1)//2
    return expected_sum-sum(nums)
print(missing_number([0,2,1]))
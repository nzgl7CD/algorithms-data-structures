def missing_number(nums:list[int])->int:
    if not nums: return 0
    n=len(nums)
    expected_sum=n*(n+1)/2
    return int(expected_sum-sum(nums))
print(missing_number([4,2,1]))
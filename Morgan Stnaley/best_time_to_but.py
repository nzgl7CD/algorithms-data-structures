def BestTime(arr:list[int])->int:
    if not arr: return 0
    low_num=float('inf')
    max_profit=0
    for i in arr:
        low_num=min(i,low_num)
        max_profit=max(max_profit,i-low_num)
    return max_profit

print(BestTime([2,1,5,3,3]))
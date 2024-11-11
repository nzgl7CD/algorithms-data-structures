def BestTime(arr:list[int])->int:
    if not arr: return 0
    low_num=float('inf')
    max_profit=0
    for i in arr:
        low_num=min(i,low_num)
        max_profit=max(max_profit,i-low_num)
    return max_profit

print(BestTime([2,1,5,3,3]))



def maxProfit(arr:list[int])->int:
    if not arr: return 0
    lowest=float('inf')
    max_profit=0
    for i in arr:
        lowest=min(i,lowest)
        max_profit=max(max_profit,i-lowest)
    return max_profit

print(maxProfit([2,1,5,3,3]))
    
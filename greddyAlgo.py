def greedyNumber(arr:list[int])->int: #max profit
    if len(arr)<=1:return 0
    min_num=float('inf')
    max_num=0
    for i in arr:
        if i<min_num:min_num=i
        max_num=max(i-min_num,max_num)
    return(max_num)

def kadunaAlg(arr: list[int]) -> int: # max sum of subproduct
    if len(arr) == 0:
        return 0
    max_so_far=float('-inf')
    max_ending_here=0
    for i in arr:
        max_ending_here+=i
        if max_ending_here>max_so_far: max_so_far=max_ending_here
        if max_ending_here<=0: max_ending_here=0
    return max_so_far

def dynamicGreed(arr: list[int])->int:
    maxportfolio1, maxportfolio2=0,0
    for i in arr:
        temp=max(maxportfolio1+i,maxportfolio2)
        maxportfolio1=maxportfolio2
        maxportfolio2=temp
    return maxportfolio2

# print(dynamicGreed([1,2,3,4,5]))

def maxSubArray(arr):
    if not arr:
        return []
    max_sum = arr[0]
    current_sum = 0
    start = end = s = 0
    for i in range(len(arr)):
        current_sum+=arr[i]
        if current_sum>max_sum:
            max_sum=current_sum
            start=s
            end=i
        if current_sum<0:
            current_sum=0
            s=i+1
    return arr[start:end+1],max_sum

# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# subarray, max_sum = maxSubArray(arr)
# print("Maximum sum subarray:", subarray)  # Output: [4, -1, 2, 1]
# print("Maximum sum:", max_sum)   

def bestDay(arr:list[int]):
    best_day_to_buy,best_day_to_sell=0,0
    min_price=float('inf')
    max_profit=0
    for i in range(len(arr)):
        if arr[i]<min_price:
            min_price=arr[i]
            best_day_to_buy=i
        if arr[i]-min_price>max_profit:
            max_profit=arr[i]-min_price
            best_day_to_sell=i
    
    return f'Best day to buy: {best_day_to_buy+1} -- Best day to sell: {best_day_to_sell+1}'

# arr = [-2, 1, -38, 4, -1, 2, 1, -5, 4]
# print(bestDay(arr))

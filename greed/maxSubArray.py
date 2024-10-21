'''
Find the continuos array with the greatest sum
'''

def maxSubArray(arr):
    if not arr: return 0
    max_sum,current_sum=arr[0],0
    start,end,s=0,0,0
    for i in range(len(arr)):
        current_sum+=arr[i]
        if current_sum>max_sum:
            max_sum=current_sum
            start=s
            end=i
        if current_sum<0:
            current_sum=0
            s=i+1
    
    return arr[start:end+1], max_sum 

arr = [-2, 1, -3, 4, -1, 2, 1, -5,5, 12,-100]
maxSubArray,maxSum=maxSubArray(arr)
print(f'The subarray: {maxSubArray} gives the greatest number equal to: {maxSum}') 
    
    
'''
We can't hold stock on the left or right side of another stock in the list
- Use dynamic memory structure to avoid memory usage
- Time complexity: O(n)
'''

def dynamicGreed(arr):
    portfolio_a,portfolio_b=0,0
    for i in arr:
        temp=max(portfolio_a+i,portfolio_b)
        portfolio_a=portfolio_b
        portfolio_b=temp
    return portfolio_b
'''
- Divide and Conquer Algorithm involves breaking a larger problem into smaller subproblems
- Divide: Break the problem to smaller pieces 
- Conquer: Solve each sub problem individually
'''

def find_max(a, lo, hi):
    if lo > hi:
        return float('-inf')
    if lo == hi:
        return a[lo]
    mid = (lo + hi) // 2
    # Get the maximum element from the left half using recursion 
    left_max = find_max(a, lo, mid)
    # Get the maximum element from the right half using recursion
    right_max = find_max(a, mid + 1, hi)
    return max(left_max, right_max)


    
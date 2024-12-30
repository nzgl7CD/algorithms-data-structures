'''
Memoization:

Top-down approach
Caches the results of function calls
Recursive implementation
Well-suited for problems with a relatively small set of inputs
Used when the subproblems have overlapping subproblems
'''

# count number of ways to reach
# nth stair using recursion

def countWays(n):

    # Base cases: If there are 0 or 1 stairs,
    # there is only one way to reach the top.
    if n == 0 or n == 1:
        return 1

    return countWays(n - 1) + countWays(n - 2)

n = 7
print(countWays(n))

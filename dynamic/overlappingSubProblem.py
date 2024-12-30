'''
Memoization:

Top-down approach
Caches the results of function calls
Recursive implementation
Well-suited for problems with a relatively small set of inputs
Used when the subproblems have overlapping subproblems
'''

# A simple recursive program for Fibonacci numbers
# Returns the Nth element in a fibonacci sequale
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(7))

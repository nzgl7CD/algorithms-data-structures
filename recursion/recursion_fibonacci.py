'''
- Time Complexity: O(2^n)
'''
def rec_fib(n):
    if n<=1: return n
    return rec_fib(n-1)+rec_fib(n-2)
n = 3
result = rec_fib(n)
print(result)
    
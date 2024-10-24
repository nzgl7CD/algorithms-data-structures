'''
Focusing:

-Bitwise Operations instead of Arithmetic operation
-Memorisation
-Built-in Functions and Libraries
-List Comprehensions and Generator Expressions
-Correct data structure 
-Optimize Loop Performance
-Profiling and Benchmarking
-Algorithmic Optimizations
'''

from itertools import islice

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

fib_list=list(islice(fib(),10))
print(fib_list)

def memorised_fib(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
        
    if n in memo:  # Check if the result is already computed
        return memo[n]
    
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    
    # Compute and store the result in the memo dictionary
    memo[n] = memorised_fib(n - 1, memo) + memorised_fib(n - 2, memo)
    return memo[n]

# Example of usage
print(memorised_fib(10))
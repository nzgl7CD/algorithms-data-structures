'''
Tabulation:

Bottom-up approach
Stores the results of subproblems in a table
Iterative implementation

Well-suited for problems with a large set of inputs
Used when the subproblems do not overlap
Here’s an example of using memoization and tabulation to solve the same problem – calculating the nth number in the Fibonacci sequence:
'''
def fibonacci(n, cache={}):
	if n in cache:
		return cache[n]
	if n == 0:
		result = 0
	elif n == 1:
		result = 1
	else:
		result = fibonacci(n-1) + fibonacci(n-2)
	cache[n] = result
	return result

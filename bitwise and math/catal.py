def catalan(n):
    if n <= 1: #base case
        return 1
 
    # Catalan(n) is the sum
    # of catalan(i)*catalan(n-i-1)
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n-i-1)
    return res

print(catalan(4))
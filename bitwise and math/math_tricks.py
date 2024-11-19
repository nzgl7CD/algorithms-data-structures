import numpy as np

def myPow(x:int,n:int):
    if n==0: return 1
    elif n<0: return 1/myPow(x,n)
    elif n&1==0: half_power=myPow(x,n//2); return half_power * half_power
    else: return x * myPow(x,n-1)
number=6
factor=3
    
print(myPow(number,factor))

def isPrime(x:int):
    sqrt_x=int(x**0.5+1)
    for i in range(2,sqrt_x):
         if x%i==0:return False
    return True

print(isPrime(113))

def count_primes_in_range(start, end):
    """
    Counts the number of prime numbers between start and end (inclusive).
    Uses the Sieve of Eratosthenes for efficiency.
    """
    if end < 2:
        return 0  # No primes below 2

    # Create a boolean array "is_prime[0..end]" initialized to True
    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    # Sieve of Eratosthenes
    for i in range(2, int(end**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, end + 1, i):
                is_prime[j] = False

    # Count primes in the specified range
    return sum(1 for i in range(start, end + 1) if is_prime[i])


def factorial(x):
    if x==1:return 1
    return x*factorial(x-1)

print(factorial(9))

'''
Note: 
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
10! = 3628800
15! = 1307674368000
20! = 2432902008176640000
'''
print(np.log(1000))

'''
Number of prime numbers in a range: 
x//ln(x)
ln(10)=2.3
ln(100)=4.6
ln(1000)=6.9

Nth number in a fibonacci sequence:
Golden ratio: ø=(1+sqrt(5))/2
Conjugate: v=(1-sqrt(5))/2    
F(n)=(ø**n-v**n)/sqrt(5)
'''

def nth_fib_number(n):
    '''
    Math variant-> will provide a float error with larger numbers
    '''
    golden_ration,conjugate=(1+np.sqrt(5))/2,(1-np.sqrt(5))/2
    return int((golden_ration**n-conjugate**n)//np.sqrt(5))

def nth_fib_w_programmin(n):
    '''
    Better for larger numbers
    '''
    a,b=0,1
    for i in range(n-1):
        b,a=b+a,b
    return b

print(nth_fib_number(10))
print(nth_fib_w_programmin(3))


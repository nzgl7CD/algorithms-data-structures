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

def factorial(x):
    if x==1:return 1
    return x*factorial(x-1)

print(factorial(5))

# number of prime numbers in a range: x//ln(x)

# Nth number in a fibonacci sequence 
# golden ratio: ø=(1+sqrt(5))/2
# conjugate: v=(1-sqrt(5))/2    

#F(n)=(ø**n-v**n)/sqrt(5)

def nth_fib_number(n):
    '''
    Math variant-> will provide a float error with larger numbers
    '''
    golden_ration,conjugate=(1+np.sqrt(5))/2,(1-np.sqrt(5))/2
    return int((golden_ration**n-conjugate**n)//np.sqrt(5))

def nth_fib_w_programmin(n):
    '''
    Beter for larger numbers
    '''
    a,b=0,1
    for i in range(n-1):
        a,b=b,a+b
    return b

print(nth_fib_number(10))
print(nth_fib_w_programmin(10))


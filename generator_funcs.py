import itertools

# Generator functions-> only store one variable at a time
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
# fib_gen=fib()
# for _ in range(5): 
#     print(next(fib_gen))
    
# third_element=next(itertools.islice(fib_gen, 9, 10)) # 10 is the iteration range and 9 is the stop index


def checkPrimes(arr:list[int]):
    for i in arr:
        if i<2: 
            continue
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
            else:
                yield i

# l=[1,2,3,4,42,7,11,14]                
# gen=checkPrimes(l)

# for prime in gen:
#     print(prime)


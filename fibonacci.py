# Generator functions-> only store one variable at a time
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
fib_gen=fib()
for _ in range(25):
    print(next(fib_gen))



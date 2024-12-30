# Iterate with exception
def average_of(lst):
    iterator = iter(lst)
    sum_of_nums,n=0,0
    while True:
        try:
            sum_of_nums += next(iterator)
            n+=1
        except StopIteration:
            break
    return sum_of_nums/n

print(average_of([1,2,3]))
# Incrementer function

def incrementer():
    i = 0
    while True:
        i += 1
        yield i

gen = incrementer()
#iter(object,sentinel) -> the iteration will stopp when the returned value is the same as the sentinel
my_iter = iter(gen.__next__,5)

for num in my_iter:
    print(num)  

# Create iterable class
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

counter = Counter(1, 4)
for num in counter:
    print(num)  # Output: 1, 2, 3
    

# Iterate throw each line in an excel file

# with open('example.txt', 'r') as file:
#     for line in iter(file.readline, ''):  # Sentinel value: empty string
#         print(line.strip())

# Iterate fibonacci sec
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
# fib_gen=fib()
# for _ in range(5): 
#     print(next(fib_gen))  


def avgIter(arr):
    iterator=iter(arr)
    sum_of,n=0,0
    while True:
        try:
            sum_of+=next(iterator)
            n+=1
        except Exception as e:
            print(type(e))
            break
    return sum_of/n


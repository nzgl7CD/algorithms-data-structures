import itertools

def chain():
    my_iter = iter([1, 2, 3])
    another_iter = iter([4, 5, 6])
    # combines the two iter
    combined_iter = itertools.chain(my_iter, another_iter)
    for item in combined_iter:
        print(item)
        
def slicing():
    my_iter = iter([1, 2, 3, 4, 5])
    sliced_iter = itertools.islice(my_iter, 2)  # Get first 2 items
    for item in sliced_iter:
        print(item)

def zipping():
    my_iter = iter([1, 2, 3])
    cycled_iter = itertools.cycle(my_iter)
    # Print the first 6 elements of the cycled iterator -> repeats the patter forever
    for i, item in zip(range(6), cycled_iter):
        print(item)

def repeater():
    repeated_iter = itertools.repeat(1,3) # repeats 1 three times

    for item in repeated_iter:
        print(item)


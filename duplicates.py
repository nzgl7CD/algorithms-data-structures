def find_duplicates(arr:list[int]):
    check_duplicates=set()
    for i in arr:
        if i in check_duplicates:
            yield i 
        else: 
            check_duplicates.add(i)
            
arr=[1,2,2,3,4,5,5,6,7,7]
for i in find_duplicates(arr):
    print(i)
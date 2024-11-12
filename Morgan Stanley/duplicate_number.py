def duplicate(arr) -> bool:
    validation=set()
    for i in arr:
        if i in validation: return True
        validation.add(i)
    return False

print(duplicate([1,2,3,4]))
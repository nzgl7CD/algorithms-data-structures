# Horrible performance -> O(N)
def lin_search(arr:list[int], target:int)->int:
    for i in arr:
        if i ==target: return arr.index(i)

        
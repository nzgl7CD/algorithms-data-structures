def twoSum(num:list[int], target:int):
    dict={}
    for i, num in enumerate(num):
        complemente=target-num
        if complemente in dict:
            return [dict[complemente],num]
        dict[num]=num
    return []





a=[1,2,3,4,5]
b=7
print(twoSum([1,3,4,6,5], 7))

    
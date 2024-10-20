


def bubbleSort(arr:list[int])->list[int]:
    if len(arr)<=1: return arr
    for n in range(len(arr)-1,0,-1):
        for i in range(n):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
# print(bubbleSort([2,1,4,3,6,5]))    

def letters_to_numbers(s: str):
    return [ord(char.lower()) - ord('a') + 1 for char in s if char.isalpha()]

# print(letters_to_numbers('somet100hing'))

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Count each element's occurrence
    for num in arr:
        count[num] += 1

    # Rebuild the sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])  # Append 'i' count[i] times

    return sorted_arr

# arr = [4, 2, 2, 8, 3, 3, 1]
# sorted_arr = counting_sort(arr)
# print("Counting Sort Output:", sorted_arr) 

def quick(arr:list[int])->list[int]:
    if not arr: return [] 
    pivot = arr[0]
    left=list(filter(lambda x: x<pivot, arr[1:]))
    right=[x for x in arr[1:] if x>=pivot]
    return quick(left) + [pivot] + quick(right)


print(quick([5,4,2,3,1,7,6,2]))

def fromStrToInt(s:str):
    listOfNums=[ord(i) for i in s]
    return ''.join(chr(i) for i in listOfNums)

    
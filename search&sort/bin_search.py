# Iterative Binary Search Algorithm:
def iter_bin_search(arr:list[int],low,high, target:int):
    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == target:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1

# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = iter_bin_search(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
        

# Recursive Binary Search Algorithm:
def rec_binarySearch(arr, low, high, target):

    # Check base case
    if high >= low:

        mid = low + (high - low) // 2

        # If element is present at the middle itself
        if arr[mid] == target:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > target:
            return rec_binarySearch(arr, low, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return rec_binarySearch(arr, mid + 1, high, x)

    # Element is not present in the array
    else:
        return -1


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    
    # Function call
    result = rec_binarySearch(arr, 0, len(arr)-1, x)
    
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
    
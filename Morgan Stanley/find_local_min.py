def find_local_minimum(arr):
    def binary_search(arr, low, high):
        mid = (low + high) // 2
        
        if (mid == 0 or arr[mid] < arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] < arr[mid + 1]):
            return mid
        
        # If the element on the left is smaller, search the left half
        elif mid > 0 and arr[mid - 1] < arr[mid]:
            return binary_search(arr, low, mid - 1)
        
        # If the element on the right is smaller, search the right half
        else:
            return binary_search(arr, mid + 1, high)

    return binary_search(arr, 0, len(arr) - 1)

# Example usage:
arr = [9, 6, 3, 5, 2, 7, 8]
index = find_local_minimum(arr)
print(f"Local minimum is at index {index}, value: {arr[index]}")

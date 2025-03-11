#Recursive Approach:

def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1  # Target not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, high, target)
    else:
        return binary_search_recursive(arr, low, mid - 1, target)

# Example usage
arr = [2, 4, 6, 8, 10, 12, 14]
target = 10
result = binary_search_recursive(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")


# Approach	 Best Case	Average Case	Worst Case	 Space Complexity
# Recursive	 O(1)	    O(log n)	    O(log n)	 O(log n)(Call Stack)
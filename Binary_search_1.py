
#Iterative Approach

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Target not found

# Example usage
arr = [2, 4, 6, 8, 10, 12, 14]
target = 10
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")


# Approach	       Best Case	Average Case	Worst Case	    Space Complexity
# Iterative   	   O(1)	        O(log n)	    O(log n)	    O(1)(Constant)
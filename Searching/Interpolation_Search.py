def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
            
    return -1  # Target not found

# Example
arr = [10, 20, 30, 40, 50, 60]
target = 40
print("Index:", interpolation_search(arr, target))  # Output: 3


# Best Case (O(1)), Worst Case (O(n))
# Improvement over binary search.
# Works well when data is uniformly distributed.
# Instead of checking the middle, it estimates position using a formula.

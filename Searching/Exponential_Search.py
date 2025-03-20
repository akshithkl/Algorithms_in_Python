def binary_search(arr, left, right, target):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, left, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, right, target)
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    return binary_search(arr, i // 2, min(i, len(arr) - 1), target)

# Example
arr = [10, 20, 30, 40, 50, 60, 70, 80]
target = 60
print("Index:", exponential_search(arr, target))  # Output: 5


# Best Case (O(1)), Worst Case (O(log n))
# Searches in exponentially increasing steps (1, 2, 4, 8, ...) until the range is found.
# Once the range is found, binary search is used.
# Used for: Unbounded or infinite-sized lists.
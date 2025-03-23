import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    while prev < n and arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # Target not found
    
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1  # Target not found

# Example
arr = [10, 20, 30, 40, 50, 60, 70]
target = 50
print("Index:", jump_search(arr, target))  # Output: 4


# Best Case (O(1)), Worst Case (O(√n))
# Requires a sorted array.
# Jumps ahead by a fixed block size (√n) and then does linear search in the found block.
# Used for: Large sorted lists.
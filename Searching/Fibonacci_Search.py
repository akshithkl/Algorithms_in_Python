def fibonacci_search(arr, target):
    n = len(arr)
    fib2, fib1 = 0, 1
    fib = fib2 + fib1
    
    while fib < n:
        fib2, fib1 = fib1, fib
        fib = fib2 + fib1
    
    offset = -1
    while fib > 1:
        i = min(offset + fib2, n - 1)
        
        if arr[i] < target:
            fib, fib1, fib2 = fib1, fib2, fib - fib1
            offset = i
        elif arr[i] > target:
            fib, fib1, fib2 = fib2, fib1 - fib2, fib - fib1
        else:
            return i
    return -1  # Target not found

# Example
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 40
print("Index:", fibonacci_search(arr, target))  # Output: 3


# Best Case (O(1)), Worst Case (O(log n))
# Uses Fibonacci numbers to split the array instead of dividing by half (like binary search).
# Used for: Sorted lists, better than binary search in some cases.
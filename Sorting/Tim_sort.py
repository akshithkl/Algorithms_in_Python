
MIN_RUN = 32

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    
    i = 0  
    j = 0 
    k = left  

    
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

  
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def tim_sort(arr):
    n = len(arr)

    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(arr, start, end)


    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2



arr = [5, 21, 1, 16, 20, 22]
print("Original array:", arr)
tim_sort(arr)
print("Sorted array:", arr)

# Case             Time Complexity      Explanation
# Best Case        O(n)                 Occurs when the array is already sorted.
# Average Case     O(n log n)           Consistently efficient for random datasets.
# Worst Case       O(n log n)           Occurs for reverse-sorted or nearly reversed arrays.

# Space Complexity: O(n) (Due to temporary arrays during merging)


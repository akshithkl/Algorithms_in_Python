def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Initial gap size

    # Start with the largest gap, then reduce the gap
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Perform a gapped insertion sort
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2  # Reduce the gap for the next iteration

    return arr


# Example usage

arr = [12, 34, 54, 2, 3, 7, 42, 3]
print("Original array:", arr)
sorted_array = shell_sort(arr)
print("Sorted array:", sorted_array)

# Case             Time Complexity       Explanation
# Best Case        O(n)                   Occurs when the array is already nearly sorted.
# Average Case     O(n log n) to O(n²)    Varies based on the gap sequence used.
# Worst Case       O(n²)                  Happens with poor gap sequences or reverse-sorted arrays.

# Space Complexity: O(1) (In-place sorting, requires minimal additional memory)


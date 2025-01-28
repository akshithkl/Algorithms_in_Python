def counting_sort(arr):
    # Find the maximum and minimum values in the array
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Initialize count array and output array
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Count the occurrences of each element
    for num in arr:
        count[num - min_val] += 1

    # Update count array to hold the position of elements
    for i in range(1, range_of_elements):
        count[i] += count[i - 1]

    # Build the output array
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    # Copy the sorted elements back into the original array
    for i in range(len(arr)):
        arr[i] = output[i]

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
print("Original array:", arr)

counting_sort(arr)
print("Sorted array:", arr)

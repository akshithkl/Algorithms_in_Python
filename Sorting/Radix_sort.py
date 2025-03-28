def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", arr)

radix_sort(arr)
print("Sorted array:", arr)


# Case	       Time Complexity	  Explanation
# Best Case	    O(nk)	           n is the number of elements, k is the number of digits.
# Average Case	O(nk)	           Uniform digit distribution results in consistent performance.
# Worst Case	O(nk)	           Still linear, but depends on the number of digits.

# Radix Sort:        O(n + k) (Due to temporary arrays for counting digits)

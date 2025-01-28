def Insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr

arr = [7, 6, 8, 5, 4, 9, 1, 18, 2]

print(f"Original array: {arr}")
print(f"Sorted array: {Insertion_sort(arr)}")

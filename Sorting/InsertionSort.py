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


#Case	          Time Complexity	Explanation
#Best Case	       O(n)	             Already sorted array, only one comparison per element.
#Average Case	   O(n²)	         Comparisons and shifts increase quadratically with input size.
#Worst Case	       O(n²)	         Reverse sorted array requires maximum shifts.


# Insertion Sort:    O(1) (In-place sorting, requires only a few auxiliary variables)

def heapify(arr, n, i):
    """
    Function to heapify a subtree rooted at index i.
    n is the size of the heap.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (max element) with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

    return arr


# Example usage

arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
sorted_array = heap_sort(arr)
print("Sorted array:", sorted_array)

#Case	         Time Complexity	Explanation
#Best Case	      O(n log n)	     Heap construction and removal of elements.
#Average Case	  O(n log n)	     Consistent due to heap property.
#Worst Case	      O(n log n)	     All elements must be moved in and out of the heap.

# Heap Sort:         O(1) (In-place sorting, uses constant extra space)

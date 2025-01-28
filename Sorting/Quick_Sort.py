def Quick_Sort(arr, left, right):
    if left < right:
        partition_pas = partition(arr, left, right)
        Quick_Sort(arr, left, partition_pas - 1)
        Quick_Sort(arr, partition_pas + 1, right)
        
def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i
arr = [7, 6, 10, 5, 9, 2, 1, 15, 7]
Quick_Sort(arr, 0, len(arr) - 1)
print(arr)

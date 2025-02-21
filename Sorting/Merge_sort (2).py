def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[: len(arr) // 2]
        right_arr = arr[len(arr) // 2:]
        
        #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        #merge
        i = 0
        j = 0 
        k = 0
        
        while i < len(left_arr) and j < len(right_arr):
            
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

arr_test = [15, 5, 24, 8, 1, 3, 16, 10, 20]
merge_sort(arr_test)
print(arr_test)

#Case	         Time Complexity	Explanation
#Best Case	      O(n log n)	     Dividing the array and merging sorted halves.
#Average Case	  O(n log n)	     Consistent due to the divide-and-conquer approach.
#Worst Case	      O(n log n)	     Even in reverse order, complexity remains O(n log n).

# Merge Sort:        O(n) (Requires temporary arrays for merging)

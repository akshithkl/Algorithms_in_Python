def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    min_value = min(arr)
    max_value = max(arr)
    range_value = max_value - min_value

    num_buckets = len(arr)
    
    buckets = [[] for i in range(num_buckets)]                               # buckets = []                                                                                                              
    for num in arr:                                                          # for i in range(num_buckets):
        index = int((num - min_value) / range_value * (num_buckets - 1))        # buckets.append([])
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array


arr = [10, 22, 98, 123, 1, 401]
print("Original array:", arr)
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)

#Case	           Time Complexity	  Explanation
#Best Case	        O(n)	           Uniformly distributed data with few elements per bucket.
#Average Case	    O(n + k)	       n for distributing and collecting, k for sorting each bucket.
#Worst Case	        O(n²)	           All elements fall into the same bucket (inefficient sorting).

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    min_value = min(arr)
    max_value = max(arr)
    range_value = max_value - min_value

    num_buckets = len(arr)
    
    buckets = [[] for _ in range(num_buckets)]                               # buckets = []                                                                                                              
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

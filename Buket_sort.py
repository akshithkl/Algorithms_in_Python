def bucket_sort(arr):
    # Step 1: Create buckets
    num_buckets = len(arr)  # Number of buckets
    buckets = [[] for _ in range(num_buckets)]

    # Step 2: Distribute elements into buckets
    for num in arr:
        index = int(num * num_buckets)  # Calculate bucket index
        buckets[index].append(num)

    # Step 3: Sort each bucket
    for bucket in buckets:
        bucket.sort()

    # Step 4: Concatenate all buckets
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array


# Example usage

arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print("Original array:", arr)
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)

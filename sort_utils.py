import time

import random

# Use your existing quick_sort and merge_sort functions here

# Step 1: Make test data
data = [random.randint(1, 10000) for _ in range(1000)]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = quick_sort([x for x in arr[1:] if x <= pivot])
    right = quick_sort([x for x in arr[1:] if x > pivot])
    return left + [pivot] + right
# print(quick_sort([2,4,7,1,2,99,7,33]))
start = time.time()
# quick_sort([34,4,65,5,231,5565])
print("Quick Sort Time:", round(time.time() - start, 5), "seconds")
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result




start = time.time()
# merge_sort([34,4,65,5,231,5565,2343,234234,2232323,3232,2323,4343,5354])
# print("Merge Sort Time:", round(time.time() - start, 5), "seconds")
# print(merge_sort([2,4,7,1,2,99,7,33]))


# Step 2: Run and time quick_sort
start = time.time()
sorted_quick = quick_sort(data.copy())
quick_time = time.time() - start
print("Quick Sort Time:", quick_time)

# Step 3: Run and time merge_sort
start = time.time()
sorted_merge = merge_sort(data.copy())
merge_time = time.time() - start
print("Merge Sort Time:", merge_time)

# Step 4: Confirm they match
print("Sorted lists match:", sorted_quick == sorted_merge)

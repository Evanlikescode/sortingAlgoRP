import random, time
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    merged_arr = merge(left_half, right_half)
    return merged_arr

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

arr = [random.randint(1, 1000) for _ in range(1000)]

start_time = time.time()
sorted_arr = merge_sort(arr)
stop_time = time.time()
duration = stop_time - start_time


print("Unsorted Array: ")
print(arr)
print("Sorted Array: ")
print(sorted_arr)
print("Time executed: ", duration)

import random, time
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [random.randint(1, 1000) for _ in range(1000)]
start_time = time.time()
sorted_arr = quick_sort(arr)
stop_time = time.time()
duration = stop_time - start_time


print("Unsorted Array: ")
print(arr)
print("Sorted Array: ")
print(sorted_arr)
print("Time executed: ", duration)

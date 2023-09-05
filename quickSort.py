import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    global step_counter
    step_counter += 1
    return quick_sort(left) + middle + quick_sort(right)

step_counter = 0
arr = [random.randint(1, 100) for _ in range(100)]
start_time = time.time()
sorted_arr = quick_sort(arr)
end_time = time.time()

print("Unsorted Array:")
print(arr)
print("Sorted Array:")
print(sorted_arr)

print(f"Jumlah langkah: {step_counter}")
print(f"Waktu yang diperlukan: {end_time - start_time} detik")

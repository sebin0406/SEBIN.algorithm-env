import random
import time


# 1. Insertion Sort
def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# 2. Quick Sort
def quick_sort(arr):
    arr = arr.copy()

    def partition(low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pivot_index = partition(low, high)
            quick_sort_recursive(low, pivot_index - 1)
            quick_sort_recursive(pivot_index + 1, high)

    quick_sort_recursive(0, len(arr) - 1)

    return arr


# 3. Heap Sort
def heap_sort(arr):
    arr = arr.copy()

    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)

    return arr


# Performance test
def measure_time(sort_function, data):
    start = time.perf_counter()
    result = sort_function(data)
    end = time.perf_counter()

    assert result == sorted(data)

    return end - start


# Test different input sizes
sizes = [1000, 5000, 10000]

for size in sizes:
    data = [random.randint(0, 100000) for _ in range(size)]

    print(f"\nData size: {size}")

    insertion_time = measure_time(insertion_sort, data)
    quick_time = measure_time(quick_sort, data)
    heap_time = measure_time(heap_sort, data)

    print(f"Insertion Sort: {insertion_time:.6f} seconds")
    print(f"Quick Sort:     {quick_time:.6f} seconds")
    print(f"Heap Sort:      {heap_time:.6f} seconds")

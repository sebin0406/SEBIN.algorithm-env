import random
import time


# ============================================================
# 1. Insertion Sort
# ============================================================
def insertion_sort(arr):
    """
    Sort an array using Insertion Sort.
    Time Complexity:
        Best:    O(n)
        Average: O(n^2)
        Worst:   O(n^2)
    Space Complexity:
        O(n) because a copy of the input array is created.
    """

    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements that are greater than key
        # one position to the right.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key into its correct position.
        arr[j + 1] = key

    return arr


# ============================================================
# 2. Quick Sort
# ============================================================
def quick_sort(arr):
    """
    Sort an array using Quick Sort.

    Time Complexity:
        Best:    O(n log n)
        Average: O(n log n)
        Worst:   O(n^2)

    Space Complexity:
        O(log n) on average because of recursion.
    """

    arr = arr.copy()

    def partition(low, high):
        # Use the last element as the pivot.
        pivot = arr[high]

        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1

                # Swap elements.
                arr[i], arr[j] = arr[j], arr[i]

        # Put pivot into its correct position.
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pivot_index = partition(low, high)

            # Sort left part.
            quick_sort_recursive(low, pivot_index - 1)

            # Sort right part.
            quick_sort_recursive(pivot_index + 1, high)

    quick_sort_recursive(0, len(arr) - 1)

    return arr


# ============================================================
# 3. Heap Sort
# ============================================================
def heap_sort(arr):
    """
    Sort an array using Heap Sort.

    Time Complexity:
        Best:    O(n log n)
        Average: O(n log n)
        Worst:   O(n log n)

    Space Complexity:
        O(log n) because of recursive heapify calls.
    """

    arr = arr.copy()

    def heapify(n, i):
        """
        Maintain the max-heap property.
        """

        largest = i

        left = 2 * i + 1
        right = 2 * i + 2

        # Check left child.
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check right child.
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If the largest element is not the root,
        # swap and continue heapifying.
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]

            heapify(n, largest)

    n = len(arr)

    # Build a max heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Extract elements from the heap one by one.
    for i in range(n - 1, 0, -1):

        # Move the largest element to the end.
        arr[0], arr[i] = arr[i], arr[0]

        # Restore heap property.
        heapify(i, 0)

    return arr


# ============================================================
# Performance Measurement
# ============================================================
def measure_time(sort_function, data):
    """
    Measure the execution time of a sorting algorithm.
    """

    start = time.perf_counter()

    result = sort_function(data)

    end = time.perf_counter()

    # Check that the algorithm sorted the data correctly.
    assert result == sorted(data)

    return end - start


# ============================================================
# Experiment
# ============================================================
def run_experiment():
    """
    Compare the three sorting algorithms
    using different input sizes.
    """

    # Different data sizes.
    sizes = [1000, 5000, 10000]

    print("=" * 60)
    print("Sorting Algorithm Performance Comparison")
    print("=" * 60)

    for size in sizes:

        # Generate random data.
        data = [
            random.randint(0, 100000)
            for _ in range(size)
        ]

        print(f"\nData size: {size}")
        print("-" * 40)

        # Insertion Sort
        insertion_time = measure_time(
            insertion_sort,
            data
        )

        # Quick Sort
        quick_time = measure_time(
            quick_sort,
            data
        )

        # Heap Sort
        heap_time = measure_time(
            heap_sort,
            data
        )

        print(
            f"Insertion Sort: {insertion_time:.6f} seconds"
        )

        print(
            f"Quick Sort:     {quick_time:.6f} seconds"
        )

        print(
            f"Heap Sort:      {heap_time:.6f} seconds"
        )


# ============================================================
# Main Program
# ============================================================
if __name__ == "__main__":
    run_experiment()

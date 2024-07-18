import sys
import time
import psutil
import os

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    steps = []
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        steps.append(f"{arr}")
    return steps

if __name__ == "__main__":
    # Measure start time
    start_time = time.time()

    # Measure memory usage before sorting
    process = psutil.Process(os.getpid())
    memory_before = process.memory_info().rss / (1024 * 1024)  # Memory in MB

    # Read input array
    array = list(map(int, sys.argv[1:]))

    # Perform heap sort
    steps = heap_sort(array)

    # Measure memory usage after sorting
    memory_after = process.memory_info().rss / (1024 * 1024)  # Memory in MB

    # Measure end time
    end_time = time.time()

    # Calculate execution time
    execution_time = end_time - start_time

    # Time Complexity and Space Complexity for Heap Sort
    time_complexity = "O(n log n)"
    space_complexity = "O(1)"  # Since heap sort is done in-place

    # Print sorting steps
    for step in steps:
        print(step)
    
    # Print performance metrics
    print(f"\nSpace Complexity: {space_complexity}")
    print(f"Memory Utilized: {memory_after - memory_before:.2f} MB")
    print(f"Time Complexity: {time_complexity}")
    print(f"Execution Time: {execution_time:.4f} seconds")

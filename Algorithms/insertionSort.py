import sys
import time
import psutil
import os

def insertion_sort(arr):
    steps = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
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

    # Perform insertion sort
    steps = insertion_sort(array)

    # Measure memory usage after sorting
    memory_after = process.memory_info().rss / (1024 * 1024)  # Memory in MB

    # Measure end time
    end_time = time.time()

    # Calculate execution time
    execution_time = end_time - start_time

    # Time Complexity and Space Complexity for Insertion Sort
    time_complexity = "O(n^2)"
    space_complexity = "O(1)"  # Since insertion sort is done in-place

    # Print sorting steps
    for step in steps:
        print(step)
    
    # Print performance metrics
    print(f"\nSpace Complexity: {space_complexity}")
    print(f"Memory Utilized: {memory_after - memory_before:.2f} MB")
    print(f"Time Complexity: {time_complexity}")
    print(f"Execution Time: {execution_time:.4f} seconds")

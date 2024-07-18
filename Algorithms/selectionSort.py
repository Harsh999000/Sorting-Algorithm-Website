import sys
import time
import psutil
import os

def selection_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
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

    # Perform selection sort
    steps = selection_sort(array)

    # Measure memory usage after sorting
    memory_after = process.memory_info().rss / (1024 * 1024)  # Memory in MB

    # Measure end time
    end_time = time.time()

    # Calculate execution time
    execution_time = end_time - start_time

    # Time Complexity and Space Complexity for Selection Sort
    time_complexity = "O(n^2)"  # Time complexity for selection sort
    space_complexity = "O(1)"   # Space complexity is constant

    # Print sorting steps
    for step in steps:
        print(step)
    
    # Print performance metrics
    print(f"\nSpace Complexity: {space_complexity}")
    print(f"Memory Utilized: {memory_after - memory_before:.2f} MB")
    print(f"Time Complexity: {time_complexity}")
    print(f"Execution Time: {execution_time:.4f} seconds")

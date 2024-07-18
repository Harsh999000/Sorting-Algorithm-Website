import sys
import time
import psutil
import os

def bubble_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            steps.append(f"{arr}")
        if not swapped:
            break
    return steps

if __name__ == "__main__":
    # Start time measurement
    start_time = time.time()

    # Capture initial memory usage
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss

    array = list(map(int, sys.argv[1:]))
    steps = bubble_sort(array)

    # Capture final memory usage
    final_memory = process.memory_info().rss
    memory_used = final_memory - initial_memory

    # End time measurement
    end_time = time.time()
    execution_time = end_time - start_time

    # Output the steps
    for step in steps:
        print(step)

    # Output the complexities and resource usage
    print(f"\nSpace Complexity: O(1)")
    print(f"Memory Utilized: {memory_used / 1024} KB")
    print(f"Time Complexity: O(n^2)")
    print(f"Execution Time: {execution_time:.6f} seconds")

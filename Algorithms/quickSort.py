import sys
import time
import psutil
import os

def quick_sort(arr):
    steps = []
    
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def sort(low, high):
        if low < high:
            pi = partition(low, high)
            sort(low, pi - 1)
            sort(pi + 1, high)
            steps.append(f"{arr}")

    sort(0, len(arr) - 1)
    return steps

if __name__ == "__main__":
    # Measure start time
    start_time = time.time()

    # Measure memory usage before sorting
    process = psutil.Process(os.getpid())
    memory_before = process.memory_info().rss / (1024 * 1024)  # Memory in MB

    # Read input array
    array = list(map(int, sys.argv[1:]))

    # Perform quick sort
    steps = quick_sort(array)

    # Measure memory usage after sorting
    memory_after = process.memory_info().rss / (1024 * 1024)  # Memory in MB

    # Measure end time
    end_time = time.time()

    # Calculate execution time
    execution_time = end_time - start_time

    # Time Complexity and Space Complexity for Quick Sort
    time_complexity = "O(n^2) worst case, O(n log n) average case"
    space_complexity = "O(log n)"  # Due to recursive stack space

    # Print sorting steps
    for step in steps:
        print(step)
    
    # Print performance metrics
    print(f"\nSpace Complexity: {space_complexity}")
    print(f"Memory Utilized: {memory_after - memory_before:.2f} MB")
    print(f"Time Complexity: {time_complexity}")
    print(f"Execution Time: {execution_time:.4f} seconds")

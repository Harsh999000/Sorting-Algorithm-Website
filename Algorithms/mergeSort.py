import sys
import time
import psutil
import os

def merge_sort(arr):
    steps = []

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = sort(arr[:mid])
        right = sort(arr[mid:])
        merged = merge(left, right)
        steps.append(f"{merged}")  # Record the state of the merged array
        return merged

    sort(arr)
    return steps

if __name__ == "__main__":
    # Measure start time
    start_time = time.time()

    # Measure memory usage before sorting
    process = psutil.Process(os.getpid())
    memory_before = process.memory_info().rss / (1024 * 1024)  # Memory in MB

    # Read input array
    array = list(map(int, sys.argv[1:]))

    # Perform merge sort
    steps = merge_sort(array)

    # Measure memory usage after sorting
    memory_after = process.memory_info().rss / (1024 * 1024)  # Memory in MB

    # Measure end time
    end_time = time.time()

    # Calculate execution time
    execution_time = end_time - start_time

    # Time Complexity and Space Complexity for Merge Sort
    time_complexity = "O(n log n)"
    space_complexity = "O(n)"  # Merge sort requires additional space for merging

    # Print sorting steps
    for step in steps:
        print(step)
    
    # Print performance metrics
    print(f"\nSpace Complexity: {space_complexity}")
    print(f"Memory Utilized: {memory_after - memory_before:.2f} MB")
    print(f"Time Complexity: {time_complexity}")
    print(f"Execution Time: {execution_time:.4f} seconds")

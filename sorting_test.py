import time
import random

# 📌 Bubble Sort Implementation
def bubble_sort(arr):
    swap = True  # Initialize swap flag to True to enter the loop
    while swap:
        swap = False  # Reset swap flag at the start of each pass
        for i in range(len(arr) - 1):  # Iterate through the list
            if arr[i] > arr[i + 1]:  # Compare adjacent elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap if out of order
                swap = True  # Set swap flag to True if a swap occurred
    return arr  # Return the sorted array


# 📌 Selection Sort Implementation (Ascending Order)
def selection_sort(arr):
    for step in range(len(arr)):  
        min_idx = step  # Assume the current index holds the minimum value
        for i in range(step + 1, len(arr)):  
            if arr[i] < arr[min_idx]:  
                min_idx = i  # Update min_idx if a smaller element is found
        arr[step], arr[min_idx] = arr[min_idx], arr[step]  
    return arr  # Return the fully sorted array


# 📌 Insertion Sort Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Select the element to be inserted
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements that are greater than key
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert the key at the correct position
    return arr


# 📌 Function to test sorting performance
def test_sorting_performance():
    """
    Generates a list of random numbers and tests the execution time of sorting algorithms.
    """
    small_dataset = [random.uniform(1, 100) for _ in range(50)]
    large_dataset = [random.uniform(1, 100) for _ in range(1000)]
    
    print("\n🔹 Small Dataset (50 elements):")
    
    # Bubble Sort test
    bubble_test = small_dataset.copy()
    start_time = time.time()
    bubble_sort(bubble_test)
    end_time = time.time()
    print(f"✅ Bubble Sort took {end_time - start_time:.6f} seconds.")
    
    # Selection Sort test
    selection_test = small_dataset.copy()
    start_time = time.time()
    selection_sort(selection_test)
    end_time = time.time()
    print(f"✅ Selection Sort took {end_time - start_time:.6f} seconds.")
    
    # Insertion Sort test
    insertion_test = small_dataset.copy()
    start_time = time.time()
    insertion_sort(insertion_test)
    end_time = time.time()
    print(f"✅ Insertion Sort took {end_time - start_time:.6f} seconds.")
    
    # Python Built-in Sort test
    python_sort_test = small_dataset.copy()
    start_time = time.time()
    python_sort_test.sort()
    end_time = time.time()
    print(f"🚀 Python Built-in Sort took {end_time - start_time:.6f} seconds.")
    
    print("\n🔹 Large Dataset (1000 elements):")
    
    # Bubble Sort test
    bubble_test = large_dataset.copy()
    start_time = time.time()
    bubble_sort(bubble_test)
    end_time = time.time()
    print(f"⚠️ Bubble Sort took {end_time - start_time:.6f} seconds.")
    
    # Selection Sort test
    selection_test = large_dataset.copy()
    start_time = time.time()
    selection_sort(selection_test)
    end_time = time.time()
    print(f"✅ Selection Sort took {end_time - start_time:.6f} seconds.")
    
    # Insertion Sort test
    insertion_test = large_dataset.copy()
    start_time = time.time()
    insertion_sort(insertion_test)
    end_time = time.time()
    print(f"✅ Insertion Sort took {end_time - start_time:.6f} seconds.")
    
    # Python Built-in Sort test
    python_sort_test = large_dataset.copy()
    start_time = time.time()
    python_sort_test.sort()
    end_time = time.time()
    print(f"🚀 Python Built-in Sort took {end_time - start_time:.6f} seconds.")

# Run the performance test
test_sorting_performance()

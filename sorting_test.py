import time
import random

# 📌 Bubble Sort Implementation
def bubble_sort(arr):
    swap = True
    while swap:
        swap = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
    return arr

# 📌 Selection Sort Implementation
def selection_sort(arr):
    for step in range(len(arr)):
        min_idx = step
        for i in range(step + 1, len(arr)):
            if arr[i] < arr[min_idx]:
                min_idx = i
        arr[step], arr[min_idx] = arr[min_idx], arr[step]
    return arr

# 📌 Insertion Sort Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 📌 Radix Sort (base 10, integers only)
def radix_sort(arr):
    arr = arr.copy()
    if len(arr) == 0:
        return arr
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Digits 0–9

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    return output

# 📌 Function to test sorting performance
def test_sorting_performance():
    """
    Generates lists of random integers and tests the execution time of sorting algorithms.
    """
    small_dataset = [random.randint(1, 1000) for _ in range(50)]
    large_dataset = [random.randint(1, 1000) for _ in range(10000)]

    print("\n🔹 Small Dataset (50 elements):")

    # Bubble Sort
    start = time.time()
    bubble_sort(small_dataset.copy())
    print(f"✅ Bubble Sort took {time.time() - start:.6f} seconds.")

    # Selection Sort
    start = time.time()
    selection_sort(small_dataset.copy())
    print(f"✅ Selection Sort took {time.time() - start:.6f} seconds.")

    # Insertion Sort
    start = time.time()
    insertion_sort(small_dataset.copy())
    print(f"✅ Insertion Sort took {time.time() - start:.6f} seconds.")

    # Python Built-in Sort
    start = time.time()
    sorted(small_dataset.copy())
    print(f"🚀 Python Built-in Sort took {time.time() - start:.6f} seconds.")

    # Radix Sort
    start = time.time()
    radix_sort(small_dataset.copy())
    print(f"⚡ Radix Sort took {time.time() - start:.6f} seconds.")

    print("\n🔹 Large Dataset (10,000 elements):")

    # Bubble Sort (this will be slow)
    start = time.time()
    bubble_sort(large_dataset.copy())
    print(f"⚠️ Bubble Sort took {time.time() - start:.6f} seconds.")

    # Selection Sort
    start = time.time()
    selection_sort(large_dataset.copy())
    print(f"✅ Selection Sort took {time.time() - start:.6f} seconds.")

    # Insertion Sort
    start = time.time()
    insertion_sort(large_dataset.copy())
    print(f"✅ Insertion Sort took {time.time() - start:.6f} seconds.")

    # Python Built-in Sort
    start = time.time()
    sorted(large_dataset.copy())
    print(f"🚀 Python Built-in Sort took {time.time() - start:.6f} seconds.")

    # Radix Sort
    start = time.time()
    radix_sort(large_dataset.copy())
    print(f"⚡ Radix Sort took {time.time() - start:.6f} seconds.")

# Run the performance test
test_sorting_performance()

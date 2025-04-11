Sorting Algorithms Performance Test
==================================================

This project implements and tests **five sorting algorithms**—Bubble Sort, Selection Sort, Insertion Sort, Radix Sort, and Python's built-in sorting function (`sort()`)—on both small and large datasets. It compares their performance to demonstrate efficiency across different scenarios.

Algorithms Implemented
----------------------

1. **Bubble Sort**
   - A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. Repeats until no more swaps are needed.

2. **Selection Sort**
   - Selects the smallest (or largest) element from the unsorted portion and swaps it with the current position. Repeats until the entire list is sorted.

3. **Insertion Sort**
   - Builds the sorted array one item at a time by inserting each new element into its correct position. More efficient than Bubble or Selection Sort for small datasets.

4. **Radix Sort**
   - A non-comparative integer sorting algorithm that processes numbers digit by digit. Highly efficient for sorting large lists of integers.

5. **Python Built-in Sort**
   - Uses Timsort (hybrid of Merge Sort and Insertion Sort). Highly optimized and used as a benchmark.

Project Structure
-----------------
- `bubble_sort(arr)` – Implements Bubble Sort to sort an array in ascending order.
- `selection_sort(arr)` – Implements Selection Sort.
- `insertion_sort(arr)` – Implements Insertion Sort.
- `radix_sort(arr)` – Implements Radix Sort for integers.
- `test_sorting_performance()` – Generates random datasets and tests all sorting functions.

Getting Started
---------------

### Prerequisites
- Python 3.x

### Installation
Clone this repository to your local machine:

```bash
git clone https://github.com/LaniAyoub/Sorting-_Algorithms-_Performance-_Test.git
```

### Running the Tests
Navigate to the project folder and run the script to test the sorting algorithms:

```bash
python sorting_test.py
```

This will generate random datasets, sort them using each algorithm, and print the execution times for comparison.

Example Output
--------------
```bash
🔹 Small Dataset (50 elements):
✅ Bubble Sort took 0.002000 seconds.
✅ Selection Sort took 0.001800 seconds.
✅ Insertion Sort took 0.001500 seconds.
⚡ Radix Sort took 0.000900 seconds.
🚀 Python Built-in Sort took 0.000700 seconds.

🔹 Large Dataset (10000 elements):
⚠️ Bubble Sort took 5.300000 seconds.
✅ Selection Sort took 0.980000 seconds.
✅ Insertion Sort took 0.820000 seconds.
⚡ Radix Sort took 0.040000 seconds.
🚀 Python Built-in Sort took 0.010000 seconds.
```

Algorithm Performance
---------------------

- **Bubble Sort** performs poorly on large datasets due to its time complexity of O(n²).
- **Selection Sort** also has a time complexity of O(n²) but usually performs slightly better than Bubble Sort.
- **Insertion Sort** is generally faster than both for small datasets but is still O(n²) in the worst case.
- **Radix Sort** performs efficiently on large integer datasets with a time complexity of O(nk), where k is the number of digits.
- **Python Built-in Sort** (Timsort) is highly optimized and significantly outperforms all other algorithms, especially on large datasets.

Contributing
------------
If you would like to contribute, feel free to fork the repository, make changes, and submit a pull request.


Sorting Algorithms Performance Test
This project implements and tests three basic sorting algorithms—Bubble Sort, Selection Sort, and Insertion Sort—on both small and large datasets. It also compares their performance with Python's built-in sorting function (sort()).

Algorithms Implemented
1. Bubble Sort
Bubble Sort is a simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until no more swaps are needed.

2. Selection Sort
Selection Sort works by selecting the smallest (or largest) element from the unsorted portion of the list and swapping it with the element at the current position. This process is repeated until the entire list is sorted.

3. Insertion Sort
Insertion Sort builds the sorted array one item at a time by inserting elements into their correct positions. It is generally more efficient than Bubble Sort and Selection Sort for small datasets.

4. Python Built-in Sort
In addition to the three sorting algorithms above, the Python built-in sort() method is used as a benchmark to compare the execution time of sorting in Python's optimized implementation.

Project Structure
bubble_sort(arr) - Implements Bubble Sort to sort an array in ascending order.
selection_sort(arr) - Implements Selection Sort to sort an array in ascending order.
insertion_sort(arr) - Implements Insertion Sort to sort an array in ascending order.
test_sorting_performance() - Generates random datasets and tests the performance of Bubble Sort, Selection Sort, Insertion Sort, and Python's built-in sort.

Getting Started
Prerequisites
Python 3.x

Installation
Clone this repository to your local machine.

```bash
git clone https://github.com/LaniAyoub/Sorting-_Algorithms-_Performance-_Test.git
```

Running the Tests
Once you have cloned the repository, navigate to the project folder and run the script to test the sorting algorithms:

```bash
python sorting_test.py
```

This will generate random datasets, sort them using each algorithm, and print the execution times for comparison.

Example Output
```bash
🔹 Small Dataset (50 elements):
✅ Bubble Sort took 0.002000 seconds.
✅ Selection Sort took 0.001800 seconds.
✅ Insertion Sort took 0.001500 seconds.
🚀 Python Built-in Sort took 0.000700 seconds.

🔹 Large Dataset (1000 elements):
⚠️ Bubble Sort took 0.120000 seconds.
✅ Selection Sort took 0.010000 seconds.
✅ Insertion Sort took 0.008000 seconds.
🚀 Python Built-in Sort took 0.001200 seconds.
```

Algorithm Performance
- **Bubble Sort** tends to perform poorly on large datasets due to its time complexity of O(n^2), which makes it inefficient for larger arrays.
- **Selection Sort** also has a time complexity of O(n^2), but it usually performs better than Bubble Sort because it reduces the number of swaps.
- **Insertion Sort** is generally faster than both Bubble Sort and Selection Sort for small datasets but still has a worst-case time complexity of O(n^2).
- **Python Built-in Sort** (using Timsort) is highly optimized and performs much better than all three sorting algorithms, especially for larger datasets.

Contributing
If you would like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request.

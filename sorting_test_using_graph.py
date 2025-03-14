import time
import random
import matplotlib.pyplot as plt

# Bubble Sort Implementation
def bubble_sort(arr):
    arr_copy = arr.copy()  # Create a copy to avoid modifying the original
    swap = True
    while swap:
        swap = False
        for i in range(len(arr_copy) - 1):
            if arr_copy[i] > arr_copy[i + 1]:
                arr_copy[i], arr_copy[i + 1] = arr_copy[i + 1], arr_copy[i]
                swap = True
    return arr_copy

# Selection Sort Implementation
def selection_sort(arr):
    arr_copy = arr.copy()  # Create a copy to avoid modifying the original
    for step in range(len(arr_copy)):
        min_idx = step
        for i in range(step + 1, len(arr_copy)):
            if arr_copy[i] < arr_copy[min_idx]:
                min_idx = i
        arr_copy[step], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[step]
    return arr_copy

# Insertion Sort Implementation
def insertion_sort(arr):
    arr_copy = arr.copy()  # Create a copy to avoid modifying the original
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and key < arr_copy[j]:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy

# Python's built-in sort
def python_sort(arr):
    arr_copy = arr.copy()  # Create a copy to avoid modifying the original
    arr_copy.sort()
    return arr_copy

# Function to measure sorting algorithm performance
def measure_performance(algorithm, data):
    start_time = time.time()
    algorithm(data)
    end_time = time.time()
    return end_time - start_time

# Function to generate random data
def generate_data(size):
    return [random.uniform(1, 1000) for _ in range(size)]

# Main function to run the sorting performance analysis
def analyze_sorting_performance():
    # Define available sorting algorithms with assigned colors
    sorting_algorithms = {
        "1": {"name": "Bubble Sort", "function": bubble_sort, "color": "crimson"},
        "2": {"name": "Selection Sort", "function": selection_sort, "color": "forestgreen"},
        "3": {"name": "Insertion Sort", "function": insertion_sort, "color": "royalblue"},
        "4": {"name": "Python Built-in Sort", "function": python_sort, "color": "darkorange"},
        "5": {"name": "All Algorithms", "function": None, "color": None}
    }
    
    # Print menu of sorting algorithms
    print("\n📊 Sorting Algorithm Performance Analyzer")
    print("----------------------------------------")
    print("Available sorting algorithms:")
    for key, value in sorting_algorithms.items():
        print(f"{key}. {value['name']}")
    
    # Get user input for algorithm choice
    while True:
        algorithm_choice = input("\nSelect an algorithm (1-5): ")
        if algorithm_choice in sorting_algorithms:
            break
        print("Invalid choice. Please try again.")
    
    # Get user input for array size
    while True:
        try:
            array_size = int(input("\nEnter the size of the array: "))
            if array_size > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Generate random data
    data = generate_data(array_size)
    
    # Run performance analysis and plot results
    if algorithm_choice == "5":  # All algorithms
        results = {}
        colors = []
        
        for key, algo_info in sorting_algorithms.items():
            if key != "5":  # Skip "All Algorithms" option
                algo_name = algo_info["name"]
                algo_function = algo_info["function"]
                algo_color = algo_info["color"]
                
                time_taken = measure_performance(algo_function, data)
                results[algo_name] = time_taken
                colors.append(algo_color)
                
                print(f"✅ {algo_name} took {time_taken:.6f} seconds for {array_size} elements.")
        
        # Plot comparison of all algorithms with different colors
        plt.figure(figsize=(10, 6))
        bars = plt.bar(results.keys(), results.values(), color=colors)
        
        # Add value labels on top of each bar
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.001,
                    f'{height:.6f}s',
                    ha='center', va='bottom', rotation=0, fontsize=9)
        
        plt.xlabel("Sorting Algorithm")
        plt.ylabel("Time (seconds)")
        plt.title(f"Sorting Algorithm Performance Comparison ({array_size} elements)")
        plt.xticks(rotation=30, ha='right')
        plt.grid(True, axis='y', linestyle='--', alpha=0.3)
        plt.tight_layout()
        plt.show()
    else:
        # Run and plot single algorithm
        algo_name = sorting_algorithms[algorithm_choice]["name"]
        algo_function = sorting_algorithms[algorithm_choice]["function"]
        algo_color = sorting_algorithms[algorithm_choice]["color"]
        
        # Run multiple tests with different array sizes for trend analysis
        sizes = [array_size//4, array_size//2, array_size, array_size*2]
        times = []
        
        for size in sizes:
            test_data = generate_data(size)
            time_taken = measure_performance(algo_function, test_data)
            times.append(time_taken)
            print(f"✅ {algo_name} took {time_taken:.6f} seconds for {size} elements.")
        
        # Plot performance trend with the algorithm's color
        plt.figure(figsize=(10, 6))
        plt.plot(sizes, times, marker='o', linestyle='-', color=algo_color, linewidth=2)
        
        # Add data points with values
        for i, (size, time) in enumerate(zip(sizes, times)):
            plt.text(size, time + max(times)/50, f'{time:.6f}s', 
                    ha='center', va='bottom', fontsize=9)
        
        plt.xlabel("Array Size")
        plt.ylabel("Time (seconds)")
        plt.title(f"{algo_name} Performance Analysis")
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

# Run the program
if __name__ == "__main__":
    analyze_sorting_performance()
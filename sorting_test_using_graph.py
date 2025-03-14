import time
import random
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

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
    # Define available sorting algorithms with assigned colors and improved visualization properties
    sorting_algorithms = {
        "1": {"name": "Bubble Sort", "function": bubble_sort, "color": "#FF5252", "pattern": ''},
        "2": {"name": "Selection Sort", "function": selection_sort, "color": "#4CAF50", "pattern": ''},
        "3": {"name": "Insertion Sort", "function": insertion_sort, "color": "#2196F3", "pattern": ''},
        "4": {"name": "Python Built-in Sort", "function": python_sort, "color": "#FF9800", "pattern": ''},
        "5": {"name": "All Algorithms", "function": None, "color": None, "pattern": None}
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
    
    # Apply custom style for plots
    plt.style.use('seaborn-v0_8-whitegrid')
    
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
        
        # Plot comparison of all algorithms with improved visualization
        plt.figure(figsize=(12, 8))
        
        # Create gradient effect for bars
        bars = plt.bar(results.keys(), results.values(), color=colors, alpha=0.8, 
                      edgecolor='black', linewidth=1.2)
        
        # Add value labels on top of each bar with improved formatting
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.0001,
                    f'{height:.6f}s',
                    ha='center', va='bottom', rotation=0, fontsize=10, 
                    fontweight='bold', color='#333333')
        
        # Add enhanced axis labels, title and grid
        plt.xlabel("Sorting Algorithm Implementation", fontsize=14, fontweight='bold', labelpad=10)
        plt.ylabel("Execution Time (Seconds)", fontsize=14, fontweight='bold', labelpad=10)
        plt.title(f"Comparative Performance of Sorting Algorithms\n({array_size:,} elements)", 
                 fontsize=16, fontweight='bold', pad=20)
        
        # Improve x-axis formatting to avoid overlap
        plt.xticks(rotation=30, ha='right', fontsize=12, fontweight='semibold')
        plt.yticks(fontsize=12)
        
        # Add grid only on y-axis with improved styling
        plt.grid(True, axis='y', linestyle='--', alpha=0.7)
        
        # Add a box around the plot
        plt.box(True)
        
        # Add a text annotation explaining the test environment
        plt.figtext(0.5, 0.01, 
                   f"Test conducted on arrays with {array_size:,} random floating-point numbers between 1 and 1000", 
                   ha="center", fontsize=10, style='italic')
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to make room for annotation
        plt.show()
        
    else:
        # Run and plot single algorithm with enhanced visualization
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
            print(f"✅ {algo_name} took {time_taken:.6f} seconds for {size:,} elements.")
        
        # Plot performance trend with enhanced visualization
        plt.figure(figsize=(12, 8))
        
        # Create gradient color for line
        cmap = cm.get_cmap('viridis')
        colors = [cmap(i) for i in np.linspace(0, 0.8, len(sizes))]
        
        # Plot line with gradient markers
        for i in range(len(sizes)-1):
            plt.plot(sizes[i:i+2], times[i:i+2], color=algo_color, linewidth=3, alpha=0.8)
        
        # Add markers with gradient colors
        for i, (size, time) in enumerate(zip(sizes, times)):
            plt.scatter(size, time, s=150, color=colors[i], edgecolor='black', linewidth=1.5, zorder=10)
            
            # Add data points with improved label formatting
            plt.annotate(f'{time:.6f}s', 
                        (size, time),
                        textcoords="offset points", 
                        xytext=(0, 10),
                        ha='center',
                        fontsize=11,
                        fontweight='bold',
                        bbox=dict(boxstyle="round,pad=0.3", fc='white', ec="gray", alpha=0.8))
        
        # Format x-axis to use comma as thousand separator
        from matplotlib.ticker import FuncFormatter
        def format_number(x, pos):
            return f'{int(x):,}'
        plt.gca().xaxis.set_major_formatter(FuncFormatter(format_number))
        
        # Add enhanced axis labels, title and grid
        plt.xlabel("Array Size (Number of Elements)", fontsize=14, fontweight='bold', labelpad=10)
        plt.ylabel("Execution Time (Seconds)", fontsize=14, fontweight='bold', labelpad=10)
        plt.title(f"Performance Scaling of {algo_name}", fontsize=16, fontweight='bold', pad=20)
        
        # Improve tick label formatting
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        
        # Add grid with improved styling
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # Add annotation explaining the test methodology
        plt.figtext(0.5, 0.01, 
                   "Tests conducted with arrays of random floating-point numbers between 1 and 1000",
                   ha="center", fontsize=10, style='italic')
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to make room for annotation
        plt.show()

# Run the program
if __name__ == "__main__":
    analyze_sorting_performance()
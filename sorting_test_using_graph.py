import time
import random
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# Bubble Sort Implementation
def bubble_sort(arr):
    arr_copy = arr.copy()
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
    arr_copy = arr.copy()
    for step in range(len(arr_copy)):
        min_idx = step
        for i in range(step + 1, len(arr_copy)):
            if arr_copy[i] < arr_copy[min_idx]:
                min_idx = i
        arr_copy[step], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[step]
    return arr_copy

# Insertion Sort Implementation
def insertion_sort(arr):
    arr_copy = arr.copy()
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
    arr_copy = arr.copy()
    arr_copy.sort()
    return arr_copy

# Radix Sort Implementation (for integers)
def radix_sort(arr):
    arr_copy = arr.copy()
    max_val = max(arr_copy)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr_copy, exp)
        exp *= 10
    return arr_copy

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
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
    for i in range(n):
        arr[i] = output[i]

# Function to measure sorting algorithm performance
def measure_performance(algorithm, data):
    start_time = time.time()
    algorithm(data)
    end_time = time.time()
    return end_time - start_time

# Function to generate random integer data
def generate_integer_data(size):
    return [random.randint(1, 1000) for _ in range(size)]

def generate_three_digit_data(size):
    return [random.randint(100, 999) for _ in range(size)]

# Main function to run the sorting performance analysis
def analyze_sorting_performance():
    sorting_algorithms = {
        "1": {"name": "Bubble Sort", "function": bubble_sort, "color": "#FF5252", "pattern": ''},
        "2": {"name": "Selection Sort", "function": selection_sort, "color": "#4CAF50", "pattern": ''},
        "3": {"name": "Insertion Sort", "function": insertion_sort, "color": "#2196F3", "pattern": ''},
        "4": {"name": "Python Built-in Sort", "function": python_sort, "color": "#FF9800", "pattern": ''},
        "5": {"name": "Radix Sort", "function": radix_sort, "color": "#9C27B0", "pattern": ''},
        "6": {"name": "All Algorithms", "function": None, "color": None, "pattern": None}
    }
    
    print("\n📊 Sorting Algorithm Performance Analyzer")
    print("----------------------------------------")
    print("Available sorting algorithms:")
    for key, value in sorting_algorithms.items():
        print(f"{key}. {value['name']}")
    
    while True:
        algorithm_choice = input("\nSelect an algorithm (1-6): ")
        if algorithm_choice in sorting_algorithms:
            break
        print("Invalid choice. Please try again.")
    
    while True:
        try:
            array_size = int(input("\nEnter the size of the array: "))
            if array_size > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    data1 = generate_integer_data(array_size)
    data2 = generate_three_digit_data(array_size)
    
    plt.style.use('seaborn-v0_8-whitegrid')
    
    if algorithm_choice == "6":
        results1 = {}
        results2 = {}
        colors = []
        
        for key, algo_info in sorting_algorithms.items():
            if key != "6":
                algo_name = algo_info["name"]
                algo_function = algo_info["function"]
                algo_color = algo_info["color"]
                
                time_taken1 = measure_performance(algo_function, data1.copy())
                time_taken2 = measure_performance(algo_function, data2.copy())
                results1[algo_name] = time_taken1
                results2[algo_name] = time_taken2
                colors.append(algo_color)
                
                print(f"✅ {algo_name} (Random): {time_taken1:.6f}s, (3-digit): {time_taken2:.6f}s for {array_size} elements.")
        
        plt.figure(figsize=(12, 8))
        
        x = np.arange(len(results1))
        width = 0.35
        
        bars1 = plt.bar(x - width/2, results1.values(), width, label='Random', color=colors, alpha=0.8, edgecolor='black', linewidth=1.2)
        bars2 = plt.bar(x + width/2, results2.values(), width, label='3-digit', color=[c + '80' for c in colors], alpha=0.8, edgecolor='black', linewidth=1.2)
        
        for bar in bars1 + bars2:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.0001, f'{height:.6f}s', ha='center', va='bottom', rotation=0, fontsize=8, fontweight='bold', color='#333333')
        
        plt.xlabel("Sorting Algorithm Implementation", fontsize=14, fontweight='bold', labelpad=10)
        plt.ylabel("Execution Time (Seconds)", fontsize=14, fontweight='bold', labelpad=10)
        plt.title(f"Comparative Performance of Sorting Algorithms\n({array_size:,} elements)", fontsize=16, fontweight='bold', pad=20)
        
        plt.xticks(x, results1.keys(), rotation=30, ha='right', fontsize=12, fontweight='semibold')
        plt.yticks(fontsize=12)
        
        plt.grid(True, axis='y', linestyle='--', alpha=0.7)
        plt.box(True)
        plt.legend()
        
        plt.figtext(0.5, 0.01, f"Test conducted on arrays with {array_size:,} random numbers and {array_size:,} 3-digit numbers", ha="center", fontsize=10, style='italic')
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()
        
    else:
        algo_name = sorting_algorithms[algorithm_choice]["name"]
        algo_function = sorting_algorithms[algorithm_choice]["function"]
        algo_color = sorting_algorithms[algorithm_choice]["color"]
        
        times1 = []
        times2 = []
        sizes = [array_size//4, array_size//2, array_size, array_size*2]
        
        for size in sizes:
            time_taken1 = measure_performance(algo_function, generate_integer_data(size))
            time_taken2 = measure_performance(algo_function, generate_three_digit_data(size))
            times1.append(time_taken1)
            times2.append(time_taken2)
            print(f"✅ {algo_name} (Random): {time_taken1:.6f}s, (3-digit): {time_taken2:.6f}s for {size:,} elements.")
        
        plt.figure(figsize=(12, 8))
        
        cmap = cm.get_cmap('viridis')
        colors = [cmap(i) for i in np.linspace(0, 0.8, len(sizes))]
        
        plt.plot(sizes, times1, label='Random', color=algo_color, linewidth=3, alpha=0.8)
        plt.plot(sizes, times2, label='3-digit', color=algo_color + '80', linewidth=3, alpha=0.8)
        
        for i, (size, time1, time2) in enumerate(zip(sizes, times1, times2)):
            plt.scatter(size, time1, s=150, color=colors[i], edgecolor='black', linewidth=1.5, zorder=10)
            plt.scatter(size, time2, s=150, color=colors[i], edgecolor='black', linewidth=1.5, zorder=10)
            plt.annotate(f'{time1:.6f}s', (size, time1), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=11, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc='white', ec="gray", alpha=0.8))
            plt.annotate(f'{time2:.6f}s', (size, time2), textcoords="offset points", xytext=(0, -25), ha='center', fontsize=11, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc='white', ec="gray", alpha=0.8))
        
        from matplotlib.ticker import FuncFormatter
        def format_number(x, pos):
            return f'{int(x):,}'
        plt.gca().xaxis.set_major_formatter(FuncFormatter(format_number))
        
        plt.xlabel("Array Size (Number of Elements)", fontsize=14, fontweight='bold', labelpad=10)
        plt.ylabel("Execution Time (Seconds)", fontsize=14, fontweight='bold', labelpad=10)
        plt.title(f"Performance Scaling of {algo_name}", fontsize=16, fontweight='bold', pad=20)
        
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        
        plt.figtext(0.5, 0.01, "Tests conducted with arrays of random numbers and 3-digit numbers", ha="center", fontsize=10, style='italic')
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()

if __name__ == "__main__":
    analyze_sorting_performance()
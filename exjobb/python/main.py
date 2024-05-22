import time
import random
from quicksort import quicksort
from selectionsort import selection_sort
from mergesort import mergesort
from linearsearch import linear_search
from binarysearch import binary_search
from data import generate_random_array, generate_sorted_array, generate_descending_array
import sys
sys.setrecursionlimit(500000)

def main():
    while True:
        print("Select an algorithm to test:")
        print("1. Quicksort")
        print("2. Selection Sort")
        print("3. Mergesort")
        print("4. Linear Search")
        print("5. Binary Search")
        print("6. Exit")
        choice = int(input("Enter your choice (1-6): "))

        if choice == 6:
            print("Exiting...")
            break

        if choice in [4, 5]:
            size = int(input("Enter the size of the data (100, 1000, 10000, 100000, 1000000): "))
            sorted_array = generate_sorted_array(size)
            key = random.randint(0, size - 1)
        else:
            size = int(input("Enter the size of the data (100, 1000, 10000, 100000, 1000000): "))
            data_type = int(input("What type of data do you want to test (1. Random, 2. Descending): "))
            
            if data_type == 1:
                array = generate_random_array(size)
            elif data_type == 2:
                array = generate_descending_array(size)
            else:
                print("Invalid data type.")
                continue

        if choice == 1:
            measure_sort_performance("Quicksort", quicksort, array)
        elif choice == 2:
            measure_sort_performance("Selection Sort", selection_sort, array)
        elif choice == 3:
            measure_sort_performance("Mergesort", mergesort, array)
        elif choice == 4:
            measure_search_performance("Linear Search", linear_search, sorted_array, key)
        elif choice == 5:
            measure_search_performance("Binary Search", binary_search, sorted_array, key)
        else:
            print("Invalid choice. Please select again.")
        print()

def measure_sort_performance(algorithm_name, sort_func, array):
    start_time = time.time()
    sort_func(array)
    end_time = time.time()
    print(f"{algorithm_name}: {(end_time - start_time) * 1_000_000:.2f} ns, {(end_time - start_time) * 1000:.2f} ms, {(end_time - start_time):.2f} s")

def measure_search_performance(algorithm_name, search_func, array, key):
    start_time = time.time()
    search_func(array, key)
    end_time = time.time()
    print(f"{algorithm_name}: {(end_time - start_time) * 1_000_000:.2f} ns, {(end_time - start_time) * 1000:.2f} ms, {(end_time - start_time):.2f} s")

if __name__ == "__main__":
    main()

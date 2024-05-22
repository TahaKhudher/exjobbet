package main

import (
	"fmt"
	"time"
)

func main() {
	for {
		// Display menu
		fmt.Println("Select an algorithm to test:")
		fmt.Println("1. Quicksort")
		fmt.Println("2. Selection Sort")
		fmt.Println("3. Mergesort")
		fmt.Println("4. Linear Search")
		fmt.Println("5. Binary Search")
		fmt.Println("6. Exit")
		fmt.Print("Enter your choice (1-6): ")
		var choice int
		fmt.Scanln(&choice)

		if choice == 6 {
			fmt.Println("Exiting...")
			break
		}

		fmt.Println("Select the size of the array to test:")
		fmt.Println("1. 500 elements")
		fmt.Println("2. 5000 elements")
		fmt.Println("3. 50000 elements")
		fmt.Println("4. 500000 elements")
		fmt.Println("5. 1000000 elements")
		fmt.Print("Enter your choice (1-5): ")
		var sizeChoice int
		fmt.Scanln(&sizeChoice)
		var size int
		switch sizeChoice {
		case 1:
			size = 500
		case 2:
			size = 5000
		case 3:
			size = 50000
		case 4:
			size = 500000
		case 5:
			size = 1000000
		default:
			fmt.Println("Invalid choice. Please select again.")
			continue
		}

		fmt.Printf("Running test for %d elements...\n", size)

		// Generate array based on the chosen algorithm type
		var array []int
		if choice == 4 || choice == 5 {
			array = generateSortedArray(size)
		} else {
			array = generateDescendingArray(size)
		}

		var totalTime int64
		numRuns := 5

		for i := 0; i < numRuns; i++ {
			startTime := time.Now()
			switch choice {
			case 1:
				Quicksort(array)
			case 2:
				selectionSort(array)
			case 3:
				mergeSort(array)
			case 4:
				LinearSearch(array, size-1)
			case 5:
				BinarySearch(array, size-1)
			default:
				fmt.Println("Invalid choice. Please select again.")
			}
			endTime := time.Now()
			totalTime += endTime.Sub(startTime).Nanoseconds()
		}

		// Compute average time
		averageTimeInNanoseconds := float64(totalTime) / float64(numRuns)
		averageTimeInSeconds := averageTimeInNanoseconds / 1e9
		averageTimeInMilliseconds := averageTimeInNanoseconds / 1e6

		fmt.Println("Average time taken:")
		fmt.Printf("   Milliseconds: %.2f ms\n", averageTimeInMilliseconds)
		fmt.Printf("   Seconds: %.9f s\n", averageTimeInSeconds)
		fmt.Printf("   Nanoseconds: %.0f ns\n", averageTimeInNanoseconds)

		fmt.Println()
	}
}

func generateSortedArray(size int) []int {
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		arr[i] = i
	}
	return arr
}

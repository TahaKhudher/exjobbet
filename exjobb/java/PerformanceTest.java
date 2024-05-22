import java.util.Scanner;
import java.util.Random;
import java.util.Scanner;

public class PerformanceTest {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            // Display menu
            System.out.println("Select an algorithm to test:");
            System.out.println("1. Quicksort");
            System.out.println("2. Selection Sort");
            System.out.println("3. Mergesort");
            System.out.println("4. Linear Search");
            System.out.println("5. Binary Search");
            System.out.println("6. Exit");
            System.out.print("Enter your choice (1-6): ");
            int choice = scanner.nextInt();

            if (choice == 6) {
                System.out.println("Exiting...");
                break;
            }
            System.out.println("Select the size of the array to test: ");
            System.out.println("1. 500 elements");
            System.out.println("2. 5000 elements");
            System.out.println("3. 50000 elements");
            System.out.println("4. 500000 elements");
            System.out.println("5. 1000000 elements");
            System.out.print("Enter your choice (1-5): ");

            int sizeChoice = scanner.nextInt();
            int size;
            switch (sizeChoice) {
                case 1:
                    size = 500;
                    break;
                case 2:
                    size = 5000;
                    break;
                case 3:
                    size = 50000;
                    break;
                case 4:
                    size = 500000;
                    break;
                case 5:
                    size = 1000000;
                    break;
                default:
                    System.out.println("Invalid choice. Please select again.");
                    continue;
            }
            System.out.println("Running test for " + size + " elements...");;

            System.out.println("Running test for " + size + " elements...");

            // Generate array based on the chosen algorithm type
            int[] array;
            if (choice == 4 || choice == 5) {
                array = data.generateSortedArr(size);
            } else {
                array = data.generateDescendingArr(size);
            }

            long totalTime = 0;
            int numRuns = 5;

            for (int i = 0; i < numRuns; i++) {
                long startTime = System.nanoTime();
                switch (choice) {
                    case 1:
                        quicksort.sort(array.clone());
                        break;
                    case 2:
                        selectionsort.selectionSort(array.clone());
                        break;
                    case 3:
                        mergesort.sort(array);
                        data.checkSorted(array);
                        break;
                    case 4:
                        linearsearch.linearSearch(array, array.length - 1);
                        break;
                    case 5:
                        binarysearch.binarySearch(array, array.length - 1);
                        break;
                    default:
                        System.out.println("Invalid choice. Please select again.");
                        break;
                }
                long endTime = System.nanoTime();
                totalTime += (endTime - startTime);
            }

            // Compute average time
            double averageTimeInNanoseconds = (double) totalTime / numRuns;
            double averageTimeInSeconds = averageTimeInNanoseconds / 1_000_000_000.0;
            double averageTimeInMilliseconds = averageTimeInNanoseconds / 1_000_000.0;

            System.out.println("Average time taken:");
            System.out.printf("   Milliseconds: %.2f ms\n", averageTimeInMilliseconds);
            System.out.printf("   Seconds: %.9f s\n", averageTimeInSeconds);
            System.out.printf("   Nanoseconds: %.0f ns\n", averageTimeInNanoseconds);

            System.out.println();
        }
        scanner.close();
    }
}

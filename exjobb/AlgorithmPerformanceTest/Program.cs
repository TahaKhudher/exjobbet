using System;

namespace PerformanceTest
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                // Display menu
                Console.WriteLine("Select an algorithm to test:");
                Console.WriteLine("1. Quicksort");
                Console.WriteLine("2. Selection Sort");
                Console.WriteLine("3. Mergesort");
                Console.WriteLine("4. Exit");
                Console.Write("Enter your choice (1-4): ");
                int choice = int.Parse(Console.ReadLine());

                if (choice == 4)
                {
                    Console.WriteLine("Exiting...");
                    break;
                }

                Console.WriteLine("Select the size of the array to test:");
                Console.WriteLine("1. 500 elements");
                Console.WriteLine("2. 5000 elements");
                Console.WriteLine("3. 50000 elements");
                Console.WriteLine("4. 500000 elements");
                Console.WriteLine("5. 1000000 elements");
                Console.Write("Enter your choice (1-5): ");

                int sizeChoice = int.Parse(Console.ReadLine());
                int size;
                switch (sizeChoice)
                {
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
                        Console.WriteLine("Invalid choice. Please select again.");
                        continue;
                }

                Console.WriteLine($"Running test for {size} elements...");

                // Generate array based on the chosen algorithm type
                int[] array;
                if (choice == 4 || choice == 5)
                {
                    array = GenerateSortedArray(size);
                }
                else
                {
                    array = GenerateDescendingArray(size);
                }

                long totalTime = 0;
                int numRuns = 5;

                for (int i = 0; i < numRuns; i++)
                {
                    long startTime = DateTime.Now.Ticks;
                    switch (choice)
                    {
                        case 1:
                            Algorithms.Quicksort.Sort(array);
                            break;
                        case 2:
                            Algorithms.SelectionSort.Sort(array);
                            break;
                        case 3:
                            Algorithms.Mergesort.Sort(array);
                            break;
                        default:
                            Console.WriteLine("Invalid choice. Please select again.");
                            break;
                    }
                    long endTime = DateTime.Now.Ticks;
                    totalTime += (endTime - startTime);
                }

                // Compute average time
                double averageTimeInTicks = (double)totalTime / numRuns;
                double averageTimeInSeconds = averageTimeInTicks / TimeSpan.TicksPerSecond;
                double averageTimeInMilliseconds = averageTimeInTicks / TimeSpan.TicksPerMillisecond;

                Console.WriteLine("Average time taken:");
                Console.WriteLine($"   Milliseconds: {averageTimeInMilliseconds:F2} ms");
                Console.WriteLine($"   Seconds: {averageTimeInSeconds:F9} s");
                Console.WriteLine($"   Ticks: {averageTimeInTicks:F0} ticks");

                Console.WriteLine();
            }
        }
    static int[] GenerateDescendingArray(int size)
        {
            int[] arr = new int[size];
            for (int i = 0; i < size; i++)
            {
                arr[i] = size - i;
            }
            return arr;
        }

        static int[] GenerateSortedArray(int size)
        {
            int[] arr = new int[size];
            for (int i = 0; i < size; i++)
            {
                arr[i] = i;
            }
            return arr;
        }
    }
}


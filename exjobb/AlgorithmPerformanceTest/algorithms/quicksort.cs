namespace Algorithms
{
    public static class Quicksort
    {
        public static void Sort(int[] arr)
        {
            QuickSort(arr, 0, arr.Length - 1);
        }

        private static void QuickSort(int[] arr, int low, int high)
        {
            if (low < high)
            {
                int pivot = Partition(arr, low, high);
                QuickSort(arr, low, pivot - 1);
                QuickSort(arr, pivot + 1, high);
            }
        }

        private static int Partition(int[] arr, int low, int high)
        {
            int pivot = arr[high];
            int i = low - 1;
            for (int j = low; j < high; j++)
            {
                if (arr[j] < pivot)
                {
                    i++;
                    int tempValue = arr[i];
                    arr[i] = arr[j];
                    arr[j] = tempValue;
                }
            }
            int tempValue2 = arr[i + 1];
            arr[i + 1] = arr[high];
            arr[high] = tempValue2;
            return i + 1;
        }
    }
}

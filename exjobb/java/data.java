import java.util.Random;

public class data {
    public static int[] generateRandomArr(int size){
        Random rand = new Random();
        int[] arr = new int[size];
        for(int i = 0; i < size; i++){
            arr[i] = rand.nextInt(size);
        }
        return arr;
    }    

    public static int[] generateDescendingArr(int size){
        int[] arr = new int[size];
        for(int i = 0; i < size; i++){
            arr[i] = size - i;
        }
        return arr;
    }
    public static int[] generateSortedArr(int size){
        int[] array = generateRandomArr(size);
        java.util.Arrays.sort(array);
        return array;
    }
    public static int checkSorted(int[] arr){
        for(int i = 0; i < arr.length - 1; i++){
            if(arr[i] > arr[i + 1]){
                return i;
            }
        }
        return -1;
    }
}


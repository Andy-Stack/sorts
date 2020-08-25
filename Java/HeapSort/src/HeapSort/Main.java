package HeapSort;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = new int[]{6,3,2,5,7,7,2,3};
        System.out.println(Arrays.toString(HeapSort.heapSort(arr)));
    }
}

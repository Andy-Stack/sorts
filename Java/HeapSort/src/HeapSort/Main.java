package HeapSort;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = new int[]{2,5,3,7,2345,6543,3456,7254,7653432,23,6754,1,45,7,23,12443,756,432,13,5};
        System.out.println(Arrays.toString(HeapSort.heapSort(arr)));
    }
}

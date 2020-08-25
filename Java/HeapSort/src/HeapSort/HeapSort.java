package HeapSort;

public class HeapSort {
    public static int[] heapSort(int[] arr){
        //last index of unsorted items
        int e = arr.length - 1;
        while (e > 0){
            heapify(arr, e);
            //swap root with last unsorted item
            swap(arr,0,e);
            e--;
        }
        return arr;
    }
    private static void heapify(int[] arr, int e){
        //last parent node in unsorted items
        int p = Math.floorDiv(e + 1, 2);
        while (p >= 0){
            percUp(arr, p, e);
            p--;
        }
    }
    private static void percUp(int[] arr, int p, int e){
        int l = (p * 2) + 1;
        int r = (p * 2) + 2;
        if (l <= e && arr[l] > arr[p]){
            if (r <= e && arr[r] > arr[l]) {
                swap(arr, p, r);
            } else {
                swap(arr, p, l);
            }
        }
        else if (r <= e && arr[r] > arr[p]){
            swap(arr,p,r);
        }
    }
    private static void swap(int[] arr, int x, int y){
        int tmp = arr[x];
        arr[x] = arr[y];
        arr[y] = tmp;
    }
}

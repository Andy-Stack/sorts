function insertionSort(arr) {
	for (i = 1; i < arr.length; i++){
		let tmp = arr[i], j = i - 1;
		while (arr[j] && arr[j] > tmp){
			arr[j+1] = arr[j]; j--;
		}
		arr[j+1] = tmp;
	}
	return arr;
}

console.log(insertionSort([6,3,2,5,7,7,2,3]));
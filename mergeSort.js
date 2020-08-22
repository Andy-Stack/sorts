function mergeSort(arr){
	if (arr.length == 1) {return arr};
	let l = Math.round(arr.length / 2);
	let arr1 = mergeSort(arr.slice(0,l));
	let arr2 = mergeSort(arr.slice(l));
	return merge(arr1, arr2);
}
function merge(arr1, arr2){
	let arr3 = [];
	while (arr1.length && arr2.length){			
		arr1[0] < arr2[0] ? arr3.push(arr1.shift()) : arr3.push(arr2.shift());
	}
	return arr1.length ? arr3.concat(arr1) : arr3.concat(arr2);
}

console.log(mergeSort([6,3,2,5,7,7,2,3]));
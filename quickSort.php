<?php
function quickSort(&$arr, $first, $last){
	if ($first < $last){
		$pivotIdx = partition($arr, $first, $last);
		quickSort($arr, $first, $pivotIdx - 1);
		quickSort($arr, $pivotIdx + 1, $last);
	}
}
function partition(&$arr, $first, $last){
	$pivot = $arr[$first];
	$left = $first + 1;
	$right = $last;
	$finished = false;
	
	while (!$finished){
		while ($left <= $right && $arr[$left] <= $pivot){
			$left++;
		}
		while ($right >= $left && $arr[$right] >= $pivot){
			$right--;
		}
		if ($right < $left){$finished = true;}
		else{
			$tmp = $arr[$left];
			$arr[$left] = $arr[$right];
			$arr[$right] = $tmp;
		}
	}
	$tmp = $arr[$first];
	$arr[$first] = $arr[$right];
	$arr[$right] = $tmp;
	return $right;
}

$arr = array(2,6,4,8,5,2,1);
quickSort($arr, 0, count($arr) - 1);
print_r($arr);
?>
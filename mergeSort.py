def mergeSort(lst):
	if len(lst) == 1:
		return lst
	l = round(len(lst) / 2)
	lst1 = mergeSort(lst[0:l])
	lst2 = mergeSort(lst[l:])
	return merge(lst1, lst2)

def merge(lst1, lst2):
	lst3 = []
	while lst1 and lst2:
		if lst1[0] < lst2[0]:
			lst3.append(lst1.pop(0))
		else:
			lst3.append(lst2.pop(0))
	return lst3 + lst1 if lst1 else lst3 + lst2

print(mergeSort([6,3,2,5,7,7,2,3]))

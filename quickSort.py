def quickSort(lst, first, last):
    if first < last:
        pivotIdx = partition(lst, first, last)
        quickSort(lst, first, pivotIdx - 1)
        quickSort(lst, pivotIdx + 1, last)

def partition(lst, first, last):
    pivot = lst[first]
    left, right = first+1, last
    finished = False

    while not finished:
        while left <= right and lst[left] <= pivot:
            left += 1
        while right >= left and lst[right] >= pivot:
            right -= 1

        if right < left:
            finished = True
        else:
            lst[left], lst[right] = lst[right], lst[left]

    lst[first], lst[right] = lst[right], lst[first]
    return right

lst = [6,3,2,5,7,7,2,3]
quickSort(lst, 0, len(lst) - 1)
print(lst)

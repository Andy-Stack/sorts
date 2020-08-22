def insertionSort(lst):
    for i in range (len(lst)):
        tmp, j = lst[i], i - 1
        while lst[j] and lst[j] > tmp:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = tmp
    return lst

print(insertionSort([6,3,2,5,7,7,2,3]))

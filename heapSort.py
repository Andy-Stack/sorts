def heapSort(lst):
    #last index of unsorted items
    e = len(lst) - 1
    while e > 0:
        heapify(lst, e)
        #swap root with last unsorted item
        lst[0], lst[e] = lst[e], lst[0]
        e -= 1
    return lst

def heapify(lst, e):
    #last parent node in unsorted items
    p = (e + 1) // 2
    while p >= 0:
        percUp(lst, p, e)
        p -= 1

def percUp(lst, p, e):
    #left and right child node index
    l = (p * 2) + 1
    r = (p * 2) + 2
    if l <= e and lst[l] > lst[p]:
        if r <= e and lst[r] > lst[l]:
            lst[r], lst[p] = lst[p], lst[r]
        else:
            lst[l], lst[p] = lst[p], lst[l]
    elif r <= e and lst[r] > lst[p]:
        lst[r], lst[p] = lst[p], lst[r]
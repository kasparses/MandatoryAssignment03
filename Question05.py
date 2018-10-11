
def merge(left, right, compare):
    """Assumes left and right are sorted lists and
    compare defines an ordering on the elements.
    Returns a new sorted (by compare) list containing the
    same elements as (left + right) would contain."""
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    while (i < len(left)):
        result.append(left[i])
        i += 1
        
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

import operator

def mergeSort(L, compare = operator.lt):
    """Assumes L is a list, compare defines an ordering
    on elements of L
    Returns a new sorted list containing the same elements as L"""
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)


myList = [5,4,1,2,89,5]

mySortedList = mergeSort(myList)

print(mySortedList)









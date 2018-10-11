
# Question 03

def has_dup (Lst ):
    size = len(Lst )
    
    numberOfComparisons = 0
    
    for i in range ( size ):
        for j in range (i + 1, size ):
            numberOfComparisons += 1
            if Lst[i] == Lst[j]:
                print('numberOfComparisons: ', numberOfComparisons)
                return True
            
    print('numberOfComparisons: ', numberOfComparisons)        
    return False



myList1 = ['a','a','b','c','d','e','f']
lst = ['a','b','c','d','e','f','g','g']
lst2 = ['a','b','c','d','e','f','g','i','y','t']

has_dup(myList1)
has_dup(lst)
has_dup(lst2)















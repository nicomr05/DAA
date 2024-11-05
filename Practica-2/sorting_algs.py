# Sorting algorithms:
def insertionSort(v:list) -> list:
    '''
    Description
    -----------
    Sort the elements of a vector from smallest to largest.
    
    Parameters
    ----------
    v : list
        Integer numbers vector.

    Returns
    -------
    list
        Vector with elements sorted in ascending order.
        
    '''
    for i in range(1,len(v)):
        x = v[i]
        j = i-1
    
        while j >= 0 and v[j] > x:
            v[j+1] = v[j]
            j = j-1

        v[j+1] = x

    return v


def bubbleSort(v:list) -> list:
    '''
    Description
    -----------
    Sort the elements of a vector from smallest to largest.    
    Parameters
    ----------
    v : list
        Integer numbers vector.

    Returns
    -------
    list
        Vector with elements sorted in ascending order.
        
    '''
    n = len(v)

    for i in range(1,n):
        for j in range(n-i):
            if v[j+1] < v[j]:
                v[j], v[j+1] = v[j+1], v[j]
    
    return v


def selectionSort(v:list) -> list:
    '''
    Description
    -----------
    Sort the elements of a vector from smallest to largest.    
    Parameters
    ----------
    v : list
        Integer numbers vector.

    Returns
    -------
    list
        Vector with elements sorted in ascending order.
   
    '''
    n = len(v)

    for i in range(n-1):
        minj = i
        minx = v[i]

        for j in range(i+1, n):
            if v[j] < minx:
                minj = j
                minx = v[j]
        
        v[minj], v[i] = v[i], minx
    
    return v

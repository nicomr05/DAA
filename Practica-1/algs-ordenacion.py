import random

# Creador de arrays (?):
def SpawnIntArray(t:int, a:int, b:int) -> list:
    l = []
    for _ in range(t):
        r = random.randint(a,b)
        l.append(r)
    
    return l

# Algoritmo de ordenamiento por inserción:
def InsertionSort(T:list) -> list:
    for i in range(1,len(T)):
        x = T[i]
        j = i-1
        while j > 0 and T[j] > x:
            T[j+1] = T[j]
            j = j-1
        
        T[j+1] = x
    
    return T

# Algoritmo de ordenamiento por selección:
def SelectionSort(T:list) -> list:
    for i in range(len(T)-1):
        minj = i
        minx = T[i]
        for j in range(i+1,len(T)):
            if T[j] < minx:
                minj = j
                minx = T[j]
        
        T[minj], T[i] = T[i], minx
    
    return T


if __name__ == '__main__':
    ej = [1,6,2,7,5,3,9,4]
    
    #print(SpawnIntArray(10,0,10))
    print(InsertionSort(ej))
    print(SelectionSort(ej))    

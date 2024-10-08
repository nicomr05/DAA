from clases_casos import Caso, CasoPrueba


VECTORES_PRUEBA = [CasoPrueba(input=[-9,4,13,-1,-5],    output=[-9,-5,-1,4,13]),
                   CasoPrueba(input=[6,-3,-15,5,4,5,2], output=[-15,-3,2,4,5,5,6]),
                   CasoPrueba(input=[13,4],             output=[4,13]),
                   CasoPrueba(input=[9],                output=[9]),
                   CasoPrueba(input=[7,6,6,5,4,3,2,1],  output=[1,2,3,4,5,6,6,7]),
                   CasoPrueba(input=[1,2,3,4,4,5,6,7],  output=[1,2,3,4,4,5,6,7])
                   ]

def insertionSort(v:list) -> list:
    '''
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
    '''
    n = len(v)

    for i in range(1,n):
        for j in range(n-i):
            if v[j+1] < v[j]:
                v[j], v[j+1] = v[j+1], v[j]
    
    return v

def selectionSort(v:list) -> list:
    '''
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

def main() -> None:
    '''
    '''
    e = [2,5,7,4,8,0,9]
    
    print(insertionSort(e))
    print(bubbleSort(e))
    print(selectionSort(e))


if __name__ == '__main__':
    main()

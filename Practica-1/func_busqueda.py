# Funciones de búsqueda:
def SearchPairsWithLists(L:list, target:int) -> list[tuple]:
    '''
    Description
    -----------
    Función que ejecuta el algoritmo de búsqueda de parejas de números
    para una lista de python.
    
    Parameters
    ----------
    L : list
        Vector de números sobre el que se aplica el algoritmo.
    target : int
        Cantidad objetivo que suman dos números del vector. 
    
    Returns
    -------
    list[tuple]
        Lista con las parejas de números que suman el target.
    '''
    pairs = []
    for i in range(len(L)):
        for j in range(len(L)):
            if i != j:
                if L[i] + L[j] == target:
                    if (L[i],L[j]) and (L[j],L[i]) not in pairs:
                        pairs.append((L[i],L[j]))
    
    return pairs

def SearchPairsWithSets(L:list, target:int) -> set[tuple]:
    '''
    Description
    -----------
    Función que ejecuta el algoritmo de búsqueda de parejas de números
    para un set de python.
    
    Parameters
    ----------
    L : list
        Vector de números sobre el que se aplica el algoritmo.
    target : int
        Cantidad objetivo que suman dos números del vector. 
    
    Returns
    -------
    set[tuple]
        Set con las parejas de números que suman el target.
    '''
    pairs = set()
    seen = set()

    for i in L:
        c = target - i
        if c in seen:
            pairs.add((min(i,c), max(i,c)))
        seen.add(i)

    return pairs
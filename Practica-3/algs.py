from numpy import ndarray

# Auxiliary functions:
def _find (u:int, S:list) -> int: 
    u_S = S[u]

    while u_S != S[u_S]:
        u_S = S[u_S]

    return u_S

def _merge (u:int, v_S:int, S:list) -> None:
    u_S = S[u]

    while u_S != S[u_S]:
        aux = S[u_S]
        S[u_S] = v_S
        u_S = aux

    S[u_S] = v_S


# Graph Algorithms:
def kruskal(V:set[int], E:set[tuple]) -> set:
    '''
    '''
    E_list = sorted(E, key=lambda t: t[2])
    T = set()
    S = [i for i in V]

    idx = 0
    while len(T) < (len(V) - 1):
        a:tuple = E_list[idx]      # select the tuple (u,v,w) that has not been yet analized and that minimizes w;
        u_S = _find(a[0], S)    # "find" is a function that finds the set of S where u is
        v_S = _find(a[1], S)

        if u_S != v_S:
            _merge(a[1], u_S, S)
            T.add(a)

        idx += 1

    return T

def prim(M:ndarray) -> set:
    '''
    '''
    # Initialization:
    n = len(M)
    mindist = [0 for _ in range(n)] #size n
    nearest = [0 for _ in range(n)] #size n
    
    T = set()

    for i in range(1, n):
        mindist[i] = M[i,0]

    # Main loop:
    cnt = 0
    while cnt < n-1:
        minimum = float("inf")

        for j in range(1, n):
            if 0 < mindist[j] < minimum:
                minimum = mindist[j]
                k = j

        a = (nearest[k], k, M[nearest[k],k])
        T.add(a)
        mindist[k] = 0

        for j in range(1,n):
            if 0 < M[j,k] < mindist[j]:
                mindist[j] = M[j,k]
                nearest[j] = k

        cnt += 1

    return T

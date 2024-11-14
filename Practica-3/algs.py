from numpy import ndarray

# Auxiliary functions:
def _find (u:int, S:list) -> int:
    '''
    Description
    -----------
    Finds the related component u_S that contains u.

    Parameters
    ----------
    u : int
        Vertex that will be contained in the related component found.
    S : list
        Array of related components of the graph.

    Returns
    -------
    int
        Related component that was found.
    '''
    u_S = S[u]

    while u_S != S[u_S]:
        u_S = S[u_S]

    return u_S

def _merge (u:int, v_S:int, S:list) -> None:
    '''
    Description
    -----------
    Merges two related components into one inside the set S.

    Parameters
    ----------
    u : int
        Representant of the first r.c.
    v_S : int
        Another r.c. differente from the r.c. of u.
    S : list
        Array of r.cc. of the graph.

    Returns
    -------
    None
    '''
    u_S = S[u]

    while u_S != S[u_S]:
        aux = S[u_S]
        S[u_S] = v_S
        u_S = aux

    S[u_S] = v_S


# Graph Algorithms:
def kruskal(graph_tuple:tuple) -> set:
    '''
    Description
    -----------
    Finds a minimum spanning tree of a graph (V,E) via the Kruskal algorithm.

    Parameters
    ----------
    graph_tuple : tuple
        Tuple (V,E) which represents a graph, meaning that V is its set of vertices
        and E its set of weighted edges.

    Returns
    -------
    set
        A minimum spanning tree of the graph.
    '''
    V, E = graph_tuple
    E_list = sorted(E, key=lambda t: t[2])
    T = set()
    S = [i for i in V]

    idx = 0
    while len(T) < (len(V) - 1):
        a:tuple = E_list[idx]       # select the tuple (u,v,w) that has not been yet analized and that minimizes w;
        u_S = _find(a[0], S)
        v_S = _find(a[1], S)

        if u_S != v_S:
            _merge(a[1], u_S, S)
            T.add(a)
        idx += 1

    return T

def prim(M:ndarray) -> set:
    '''
    Description
    -----------
    Finds a minimum spanning tree of a graph (V,E) via the Prim algorithm.

    Parameters
    ----------
    M : ndarray
        Adjacency matrix of the graph

    Returns
    -------
    set
        A minimum spanning tree of the graph.
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

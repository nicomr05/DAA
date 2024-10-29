
def find (u, S): 
    u_S = S[u]
    while u_S != S[u_S]:
        u_S = S[u_S]
    return u_S

def merge (u, v_S, S):
    u_S = S[u]
    while u_S != S[u_S]:
        aux = S[u_S]
        S[u_S] = v_S
        u_S = aux
    S[u_S] = v_S

# Graph Algorithms:
def kruskal(V:set[int], E:set[tuple]) -> set:
    E = sorted(E, key=lambda x: x[2])
    T = {}
    S = [i for i in V]  
    while len(T) <= (len(V)-1):
        a = (E-T)[0]#select the tuple (u,v,w) that has not been yet analized and that minimizes w;
        u_S = find(a[0], S) # find is a function that finds the set of S where u is
        v_S = find(a[1], S)
        if u_S != v_S:
            merge(a[1], u_S, S)
            T = T + {a}
    return T

def prim(M:list[list]) -> set:
    '''
    '''
    # Initialization:
    n = len(M)
    [i for i in V]
    mindist = [0 for _ in range(n)] #size n
    nearest = [1 for _ in range(n)] #size n
    T = set()

    # Loops:
    for i in range(2,n):
        mindist[i] = M[i,1]
    
    for i in range(n-1):
        minimum = float('inf')
    
    for j in range(1,n):
        if 0 <mindist[j] < minimum:
            minimum = mindist[j]
            k = j

    a = (nearest[k], k, M[nearest[k],k])
    T = T.add(a)
    mindist[k] = 0
    
    for j in range(1,n):
        if 0 < M[j,k] < mindist[j]:
            mindist[j] = M[j,k]
            nearest[j] = k
    
    return T

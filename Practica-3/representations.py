import numpy as np

def to_adjacency_matrix(V, E) -> np.matrix:
    '''
    '''
    M = np.zeros((len(V), len(V)), dtype=int)
    
    for i,j,w in E:
        M[i][j] = w
        M[j][i] = w
    
    return M

def to_vertices_and_edges(M) -> tuple[set,set]:
    '''
    '''
    rows, cols = M.shape
    E = set([])
    V = set([])
    
    for i in range(rows):
        V.add(i)
    
    for j in range(i+1, cols):
        E.add((i,j,M[i][j]))
    
    return (V,E)


def create_graph(n:int, max_distance:int, adjacency_matrix=False) -> np.matrix|tuple[set,set]:
    '''
    '''
    a = np.random.randint(low=1, high=max_distance, size=(n,n))
    M = np.tril(a,-1) + np.tril(a, -1).T
    
    if adjacency_matrix:
        return M
    
    return to_vertices_and_edges(M)

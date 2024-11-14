import numpy as np


#Tuple-Matrix converting functions:
def to_adjacency_matrix(V:set, E:set) -> np.ndarray:
    '''
    Description
    -----------
    Transforms a set of vertices and a set of edges of a graph into a matrix.

    Parameters
    ----------
    V : set
        Set of ints that represents the vertices of a graph.
    E : set
        Set of tuples with 2 vertex identifiers and the weight of the edge that joins them.

    Returns
    -------
    np.ndarray
        Adjacency matrix with the weights of the graph with vertices V and edges E.
    '''
    M = np.zeros((len(V), len(V)), dtype=int)
    
    for i, j, w in E:
        M[i][j] = w
        M[j][i] = w
    
    return M

def to_vertices_and_edges(M:np.ndarray) -> tuple:
    '''
    Description
    -----------
    Transforms a matrix into a tuple of 2 sets.

    Parameters
    ----------
    M : np.ndarray
        Adjacency matrix with the weights of the edges of the graph.

    Returns
    -------
    tuple
        Graph tuple with 2 sets: V (set of ints that represents the vertices of the graph) and 
        E (set of edges (tuples) of the graph with each weigth). 
    '''
    rows, cols = M.shape
    V = set()
    E = set()
    
    for i in range(rows):
        V.add(i)
    
        for j in range(i+1, cols):
            E.add((i,j,M[i][j]))
    
    return (V,E)


#Graph creating function:
def create_graph(n:int, max_distance=50, adjacency_matrix=False) -> np.ndarray|tuple:
    '''
    Description
    -----------
    Creates a graph.

    Parameters
    ----------
    n : int
        Number of vertices of the graph.
    max_distance : int
        Maximum value that an element of the adjacency matrix can have.
    adjacency_matrix : bool
        Indicates whether the graph is returned in the form of a hue or a tuple.

    Returns
    -------
    np.ndarray
        Adjacency matrix with the weights of the graph with vertices V and edges E.

    or

    tuple
        Tuple with 2 sets: V (set of integer numbers that identifies the vertices of a graph) and 
        E (set of tuples with 2 vertex identifiers and the weight of the edge that joins them).
    '''
    a = np.random.randint(low=1, high=max_distance, size=(n,n))
    M = np.tril(a,-1) + np.tril(a, -1).T
    
    if adjacency_matrix:
        return M
    
    return to_vertices_and_edges(M)

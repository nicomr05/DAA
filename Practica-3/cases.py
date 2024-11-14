from numpy import ndarray

from representations import to_adjacency_matrix


# Test case class:
class TestCase:
    '''
    Description
    -----------
    Class for a test case to evaluate graph algorithms.

    Attributes
    ----------
    V : set
        Vertices of the graph.
    E : set
        Weighted edges of the graph.
    AdMatrix : ndarray
        Adjacency matrix of the graph.
    output : ndarray
        Adjacency matrix of the minimum spanning tree of the graph (expected solution).

    Methods
    -------
    __init__(self, V, E, output) -> None:
        Constructor of the TestCase class, initializes its attributes.
    '''
    def __init__(self, V:set, E:set, output:ndarray) -> None:
        '''
        Description
        -----------
        Class initializer that creates the sets needed for the class TestCase.

        Parameters
        ----------
        V : set
            Vertices of the graph.
        E : set
            Weighted edges of the graph.
        output : ndarray
            Adjacency matrix of the minimum spanning tree of the graph (expected solution).

        Returns
        -------
        None
        '''
        self._V = V
        self._E = E
        self._AdMatrix = to_adjacency_matrix(V, E)
        self._output = to_adjacency_matrix(V, output)
    
    @property
    def V(self) -> set:
        return self._V

    @property
    def E(self) -> set:
        return self._E

    @property
    def AdMatrix(self) -> ndarray:
        return self._AdMatrix

    @property
    def output(self) -> set:
        return self._output

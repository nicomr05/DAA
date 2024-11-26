
# Test case class:
class TestCase:
    '''
    Description
    -----------
    Class for a test case to evaluate graph algorithms.

    Attributes
    ----------
    A : str|list
       Vertices of the graph.
    B : str|list
        Weighted edges of the graph.
    C : str|list
       Vertices of the graph.

    Methods
    -------
    __init__(self, V, E, output) -> None:
        Constructor of the TestCase class, initializes its attributes.
    '''
    def __init__(self, A:str|list, B:str|list, C:str|list) -> None:
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
        self._A = A
        self._B = B
        self._C = C
    
    @property
    def A(self) -> str|list:
        return self._A

    @property
    def B(self) -> str|list:
        return self._B

    @property
    def C(self) -> str|list:
        return self._C

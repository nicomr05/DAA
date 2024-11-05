from representations import to_adjacency_matrix


# Test case class:
class TestCase:
    '''
    Description
    -----------
    Class for a test case to evaluate sorting algorithms.

    Attributes
    ----------
    input : list
        vector of integer numbers on which the algorithms will be applied.
    output : list
        expected vector with sorted elements after passing it through sorting algorithms.
        
    Methods
    -------
    __init__(self, input, output) -> None:
        Constructor of the TestCase class, initializes its attributes.
    '''
    def __init__(self, V:set, E:set, output:set) -> None:
        '''
        '''
        self._V = V
        self._E = E
        self._AdMatrix = to_adjacency_matrix(V,E)
        self._output = output
    
    @property
    def V(self) -> list:
        return self._V

    @property
    def E(self) -> list:
        return self._E

    @property
    def AdMatrix(self) -> list:
        return self._AdMatrix

    @property
    def output(self) -> list:
        return self._output

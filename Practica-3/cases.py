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
    def __init__(self, input, output) -> None:
        '''
        '''
        self._input = input
        self._output = output
    
    @property
    def output(self) -> list:
        return self._output
    
    @property
    def input(self) -> list:
        return self._input

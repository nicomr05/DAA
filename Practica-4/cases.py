#!env/bin/python

from words import mix_words


# Test case class:
class TestCase:
    '''
    Description
    -----------
    Class for a test case to evaluate graph algorithms.

    Attributes
    ----------
    A : `str|list`
       Vertices of the graph.
    B : `str|list`
        Weighted edges of the graph.
    C : `str|list`
       Vertices of the graph.

    Methods
    -------
    `__init__(self, A, B, C) -> None`:
        Constructor for the TestCase class. Initializes its attributes.
    '''
    def __init__(self, A:str|list, B:str|list, C:str|list, output:str) -> None:
        '''
        Description
        -----------
        Class initializer that creates the sets needed for the class `TestCase`.

        Parameters
        ----------
        A : `str|list`
            First string.
        B : `str|list`
            Second string.
        C : `str`
            Mixed array from A and B.
        output : `str`
            String indicating where each character of the solution belongs to.

        Returns
        -------
        `None`
        '''
        self.__A = A
        self.__B = B
        self.__C = C
        self.__output = output


    @property
    def A(self) -> str|list:
        return self.__A

    @property
    def B(self) -> str|list:
        return self.__B

    @property
    def C(self) -> str|list:
        return self.__C

    @property
    def output(self) -> str:
        return self.__output

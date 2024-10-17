from random import randint
from numpy import arange

from sorting_algs import *
from cases import TestCase

# Vector generators:
def descending_order(size:int) -> list:
    '''
    Description
    -----------
    Create a random number vector of a specified size in descending order.
    
    Parameters
    ----------
    casos : list[TestCase]
        Size of the vector you want to create. 
        
    Returns
    -------
    list
        Random numbers vector in descending order.
    '''
    return arange(size//2, -size//2, -1)



def random_order(size:int) -> list:
    '''
    Description
    -----------
    Create a random number vector of a specified size in no specific order.
    
    Parameters
    ----------
    size : int
        Size of the vector you want to create. 
        
    Returns
    -------
    list
        Random numbers vector in no specific order.
    '''
    vector = []

    for _ in range(size):
        vector.append(randint(-size//2, size//2))
    
    return vector



def ascending_order(size:int) -> list:
    '''
    Description
    -----------
    Create a random number vector of a specified size in ascending order.
    
    Parameters
    ----------
    size : int
        Size of the vector you want to create. 
        
    Returns
    -------
    list
        Random numbers vector in ascending order.
    '''
    return arange(-size//2, size//2, 1)



# Testing function:
def test(casos:list[TestCase], alg=insertionSort) -> str|AssertionError:
    '''
    Description
    -----------
    Test the test cases with the algorithm function that is indicated.
    
    Parameters
    ----------
    casos : list[TestCase]
        List of test case objects to be checked.
    alg: fuction
        Function of the algorithm to be evaluated. 
        
    Returns
    -------
    str
        A string that confirms that the execution is successful, in case you want to show it on the screen.
    
    AssertionError
        Error with its associated message indicating that the tests were not executed correctly.
    '''
    for caso in casos:
        sol = alg(caso.input)
        
        assert caso.output == sol, f'Lista {caso.input}. Esperada salida {caso.output}, pero obtuvo {sol}.'
    
    return 'Ejecución correcta.'

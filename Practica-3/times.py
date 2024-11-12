from time import time

from cases import TestCase
from algs import kruskal, prim
from representations import create_graph, to_adjacency_matrix


# Testing function:
def test(cases:list[TestCase], alg=kruskal) -> str|AssertionError:
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
    for case in cases:
        if alg == kruskal:
            graph = (case.V, case.E)
            sol = alg(*graph)

        elif alg == prim:
            graph = case.AdMatrix
            sol = alg(graph)

        result = to_adjacency_matrix(case.V, sol)
        
        size = len(case.output)
        for row in range(size):
            for col in range(size):
                assert case.output[row][col] == result[row][col], f'\n\nGraph:\n{graph}.\n\nExpected output:\n{case.output}\n\nBut got:\n{result}.\n'

    return 'Correct output.'


# Time measuring functions:
def time_ns() -> float:
    '''
    Description
    -----------
    Returns the current system time in nanoseconds.

    Returns
    -------
    float
        System time in ns.
    '''
    return time() * (10**9)

def measure_time(n:int, adjacency:bool, alg=kruskal) -> tuple[float,bool]:
    '''
    Description
    -----------
    It measures the execution time of an algorithm.
    
    Parameters
    ----------
    n : int
        Tamaño del vector que se va a utilizar para medir el tiempo.
    alg: function
        Function of the algorithm to be evaluated. 
    gen: function
        Fuction that generates an vector.
    
    Returns
    -------
    tuple[float,bool]
        Tuple containing the runtime that has been measured and a Boolean
        which indicates whether the response had to be averaged because it was the time of
        very small execution.
    '''
    graph = create_graph(n, adjacency_matrix=adjacency)
    ta = time_ns()
    alg(graph)
    tb = time_ns()
    t = tb - ta
    avg = False

    threshold = 5*(10**5)    # Confidence threshold 
    
    if t < threshold:
        K = 1000

        ta = time_ns()
        for _ in range(K):
            vector = create_graph(n, adjacency_matrix=adjacency)
            alg(vector)

        tb = time_ns()
        t1 = tb - ta

        ta = time_ns()
        for _ in range(K):
            vector = create_graph(n, adjacency_matrix=adjacency)

        tb = time_ns()
        t2 = tb - ta

        t = (t1 - t2) / K
        avg = True

    return t, avg

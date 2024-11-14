from time import time

from algs import kruskal, prim
from representations import create_graph, to_adjacency_matrix


# Testing function:
def test(cases:list, alg=kruskal) -> str|AssertionError:
    '''
    Description
    -----------
    Evaluate the test cases with the algorithm function (alg) that is indicated.

    Parameters
    ----------
    cases : list
        List of TestCase objects to be checked.
    alg: fuction
        Function of the algorithm to be evaluated. 

    Returns
    -------
    str
        A string that confirms that the execution is successful, in case you want to print it.

    or

    AssertionError
        Error with its associated message indicating that the tests failed to match the expected output.
    '''
    for case in cases:
        if alg == kruskal:
            graph = (case.V, case.E)
            sol = alg(graph)

        elif alg == prim:
            graph = case.AdMatrix
            sol = alg(graph)

        result = to_adjacency_matrix(case.V, sol)
        
        size = len(case.output)
        for row in range(size):
            for col in range(size):
                assert case.output[row][col] == result[row][col], f'\n\nGraph:\n{graph}.\n\nExpected output:\n{case.output}\n\nBut got:\n{result}.\n'

    return 'Correct output.'


# Time-measuring functions:
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
    Measures the execution time of an algorithm and averages it with other repetitions
    if the execution time was too small.

    Parameters
    ----------
    n : int
        Size of the sample that is going to be generated.
    adjacency : bool
        Value that indicates if the entry for the algorithm must be an adjacency
        matrix or a tuple.
    alg: function
        Function of the algorithm to be evaluated.

    Returns
    -------
    tuple
        Tuple containing the runtime that has been measured and a boolean value
        which indicates whether the response had to be averaged due to a small
        execution time.
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
            graph = create_graph(n, adjacency_matrix=adjacency)
            alg(graph)

        tb = time_ns()
        t1 = tb - ta

        ta = time_ns()
        for _ in range(K):
            graph = create_graph(n, adjacency_matrix=adjacency)

        tb = time_ns()
        t2 = tb - ta

        t = (t1 - t2) / K
        avg = True

    return t, avg

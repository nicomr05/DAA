#!env/bin/python

from cases import TestCase
from time import time
from algs import MixtureDP
from words import create_word, mix_words


# Sample creating function
def sampler(n:int, alphabet:tuple) -> str:
    '''
    Description
    -----------
    Sampling function that permits the 

    Parameters
    ----------
    n : `int`
        Size of the sample that is going to be generated.
    alphabet : `tuple`
        Tuple of characters that can be used in the new random words.

    Returns
    -------
    `str`, `str`
        Two random words (strings) to which to apply the algorithms.
    '''
    if alphabet == "AB-LENGTH":
        alphabet = [chr(i) for i in range(n)]

    A, B = create_word(n, alphabet), create_word(n, alphabet)

    return A, B


# Testing function:
def test(cases:list[TestCase], alg=MixtureDP) -> str|AssertionError:
    '''
    Description
    -----------
    Evaluate the test cases with the algorithm function (alg) that is indicated.

    Parameters
    ----------
    cases : `list`
        List of TestCase objects to be checked.
    alg: `function`
        Function of the algorithm to be evaluated. 

    Returns
    -------
    `str`
        A string that confirms that the execution is successful, in case you want to print it.

    or

    `AssertionError`
        Error with its associated message indicating that the tests failed to match the expected output.
    '''
    for case in cases:
        sol = alg(case.A, case.B, case.C)

        assert case.output == sol, f'Sample {case.A} + {case.B} = {case.C}. Expected output {case.output}, but got {sol}.'
    
    return 'Correct output.'


# Time-measuring functions:
def time_ns() -> float:
    '''
    Description
    -----------
    Returns the current system time in nanoseconds.

    Returns
    -------
    `float`
        System time in ns.
    '''
    return time() * (10**9)

def measure_time(n:int, alphabet:tuple, alg=MixtureDP) -> tuple[float,bool]:
    '''
    Description
    -----------
    Measures the execution time of an algorithm and averages it with other repetitions
    if the execution time was too small.

    Parameters
    ----------
    n : `int`
        Size of the sample that is going to be generated.
    alphabet : `tuple`
        Tuple of characters that can be used in the new random words.
    alg: `function`
        Function of the algorithm to be evaluated.

    Returns
    -------
    `tuple`
        Tuple containing the runtime that has been measured and a boolean value
        which indicates whether the response had to be averaged due to a small
        execution time.
    '''
    A, B = sampler(n, alphabet)
    C = mix_words(A, B, valid=True)

    ta = time_ns()
    alg(A,B,C)
    tb = time_ns()
    t = tb - ta
    avg = False

    threshold = 6*(10**5)    # Confidence threshold 
    
    if t < threshold:
        K = 1000

        ta = time_ns()
        for _ in range(K):
            A, B = sampler(n, alphabet)
            C = mix_words(A, B, valid=True)
            alg(A,B,C)

        tb = time_ns()
        t1 = tb - ta

        ta = time_ns()
        for _ in range(K):
            A, B = sampler(n, alphabet)
            C = mix_words(A, B, valid=True)

        tb = time_ns()
        t2 = tb - ta

        t = (t1 - t2) / K
        avg = True

    return t, avg

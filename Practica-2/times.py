from time import time


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


def measure_time(n:int, alg:function, gen:function) -> tuple[float,bool]:
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
    vector = gen(n)
    ta = time_ns()
    alg(vector)
    tb = time_ns()
    t = tb - ta
    avg = False

    threshold = 5*(10**5)    # Confidence threshold 
    
    if t < threshold:
        K = 1000

        ta = time_ns()
        for _ in range(K):
            vector = gen(n) 
            alg(vector)
        
        tb = time_ns()
        t1 = tb - ta

        ta = time_ns()
        for _ in range(K):
            vector = gen(n)

        tb = time_ns()
        t2 = tb - ta

        t = (t1 - t2) / K
        avg = True
    
    
    return t, avg

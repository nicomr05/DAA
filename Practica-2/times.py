from time import time

from sorting_algs import *
from test_func import *


# Time measuring functions:
def time_ns() -> float:
    '''
    Description
    -----------
    Devuelve el tiempo actual del sistema en nanosegundos.

    Returns
    -------
    float
        Tiempo del sistema en ns.
    '''
    return time() * (10**9)

def measure_time(n:int, alg=selectionSort, gen=ascending_order) -> tuple[float,bool]:
    '''
    Description
    -----------
    Mide el tiempo de ejecución de un algoritmo.
    
    Parameters
    ----------
    n : int
        Tamaño del vector que se va a utilizar para medir el tiempo.
    alg : function
        Función del algoritmo que se quiere evaluar.
    
    Returns
    -------
    tuple[float,bool]
        Tupla que contiene el tiempo de ejecución que se ha medido y un booleano
        que indica si se tuvo que promediar la respuesta por ser el tiempo de
        ejecución muy pequeño.
    '''
    vector = gen(n)
    ta = time_ns()
    alg(vector)
    tb = time_ns()
    t = tb - ta
    avg = False

    umbral = 5*(10**5)    # Umbral de confianza
    if t < umbral:
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

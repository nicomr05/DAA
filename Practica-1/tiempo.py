from time import time
from random import randint, choice

from func_busqueda import *
from clases_casos import *


# Variable de los tamaños de los casos:
SIZES = [50,
         100,
         200,
         400,
         800,
         1600,
         2000,
         3200,
         4000,
         5000,
         6000,
         6500,
         8000,
         9000,
         10000
         ]

# Generador de tuplas (lista, target):
def generate_input(n) -> tuple[list,int]:
    '''
    Description
    -----------
    Generates a sorted list of "n" unique, non-consecutive integers and a target sum.
    
    Parameters
    ----------
    n : int
        The number of elements to generate in the list.
    
    Returns
    -------
    tuple[list,int]
        A tuple containing:
        - A list of "n" unique, non-consecutive integers in sorted order.
        - An integer representing the target sum of two randomly selected numbers from the list.
        Example:
        >>> generate_input(5)
        ([2, 4, 6, 9, 11], 13)
    '''
    nums = []
    current_value = randint(1, 10)
    for _ in range(n):
        nums.append(current_value)
        current_value += randint(1, 5)
    target = choice(nums) + choice(nums)
    return nums, target


# Funciones de tiempos:
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

def medir_tiempo(n:int, g=SearchPairsWithLists) -> tuple[float,bool]:
    '''
    Description
    -----------
    Mide el tiempo de ejecución de un algoritmo.
    
    Parameters
    ----------
    n : int
        Tamaño del vector que se va a utilizar para medir el tiempo.
    g : function
        Función del algoritmo que se quiere evaluar.
    
    Returns
    -------
    tuple[float,bool]
        Tupla que contiene el tiempo de ejecución que se ha medido y un booleano
        que indica si se tuvo que promediar la respuesta por ser el tiempo de
        ejecución muy pequeño.
    '''
    casos = []

    vector, target = generate_input(n)
    ta = time_ns()
    g(vector, target)
    tb = time_ns()
    t = tb - ta
    avg = False

    umbral = 5*(10**5)    # Umbral de confianza
    if t < umbral:
        K = 1000

        ta = time_ns()
        for _ in range(K):
            vector, target = generate_input(n)
            casos.append(Caso(vector,target))  
            g(vector, target)
        tb = time_ns()
        t1 = tb - ta

        ta = time_ns()
        for _ in range(K):
            vector, target = generate_input(n)
            casos.append(Caso(vector,target))  
        tb = time_ns()
        t2 = tb - ta

        t = (t1 - t2) / K
        avg = True
    
    
    return t, avg
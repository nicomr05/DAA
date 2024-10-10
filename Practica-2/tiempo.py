from time import time
from random import randint, choice, seed

from func_ord import *
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
         8000
         ]


# Generador de listas para ordenar:
def generate_random_input(sizes:list, f=selectionSort) -> list:
    '''
    '''
    seed(1)
    for size in sizes:
        array = randint(-10,10,size) #creates an array with size random elements between -10 and 10
    
    return array


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

def medir_tiempo(n:int, f=selectionSort) -> tuple[float,bool]:
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
    f(vector, target)
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
            f(vector, target)
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
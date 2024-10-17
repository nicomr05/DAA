from random import randint
from numpy import arange

from sorting_algs import *
from cases import TestCase

# Vector generators:
def descending_order(size:int) -> list:
    '''
    '''
    return arange(size//2, -size//2, -1)

def random_order(size:int) -> list:
    '''
    '''
    vector = []

    for _ in range(size):
        vector.append(randint(-size//2, size//2))
    
    return vector

def ascending_order(size:int) -> list:
    '''
    '''
    return arange(-size//2, size//2, 1)


# Testing function:
def test(casos:list[TestCase], f=insertionSort) -> str|AssertionError:
    '''
    Description
    -----------
    Testea los casos de prueba con la función del algoritmo que se le indique.
    
    Parameters
    ----------
    casos : list[CasoPrueba]
        Lista de objetos CasoPrueba que se quieren comprobar.

    Returns
    -------
    str
        String que confirma que la ejecución es correcta, por si se quiere mostrar por pantalla.
    
    AssertionError
        Error con su mensaje asociado que indica que los tests no se ejecutaron correctamente.
    '''
    for caso in casos:
        sol = f(caso.input)
        
        assert caso.output == sol, f'Lista {caso.input}. Esperada salida {caso.output}, pero obtuvo {sol}.'
    
    return 'Ejecución correcta.'

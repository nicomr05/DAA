from random import randint
from numpy import arange

from sorting_algs import *
from cases import TestCase

# Generadores de listas para ordenar:
def descending_order(size:int) -> list:
    '''
    '''
    array = arange(size//2, -size//2, -1)
    return array

def random_order(size:int) -> list:
    '''
    '''
    array = randint(-100, 100, size)
    return array

def ascending_order(size:int) -> list:
    '''
    '''
    array = arange(-size//2, size//2, 1)
    return array


# Función de testeo:
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

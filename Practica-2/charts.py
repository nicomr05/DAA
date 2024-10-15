from math import log
from prettytable import PrettyTable

from times import measure_time
from sorting_algs import *


# Función de creación de tablas:
def create_table(sizes:list, f=selectionSort) -> PrettyTable:
    '''
    Description
    -----------
    Crea una tabla con las columnas "n" (tamaño de muestra), "Averaged"
    (indica si se promedió el tiempo), "Time" (tiempo), "O(nlog(n))", "O(n²)"
    y "O(n²·²)" (relaciones del algoritmo con un algoritmo nlogn, uno n² y
    uno n²·²).
    
    Parameters
    ----------
    sizes : list
        Lista de los tamaños de muestra.
    f : function
        Función del algoritmo que se quiere evaluar.
    
    Returns
    -------
    PrettyTable
        Tabla con la información del algoritmo.
    '''
    table = PrettyTable()
    
    table.add_row()
    
    
    return table

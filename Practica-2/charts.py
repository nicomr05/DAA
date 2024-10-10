from math import log

from prettytable import PrettyTable

from tiempo import medir_tiempo
from func_ord import *


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
    
    times = []
    booleans = []
    logs = []
    nlogs = []
    n_squared = []
    n_22 = []
    linear = []
    
    # Creación de las columnas de la tabla:
    for size in sizes:
        time, averaged = medir_tiempo(size,f)

        logn = time/(log(size))
        lin = time/size
        nlogn = time/(size*log(size))
        n2 = time/(size**2)
        n22 = time/(size**(2.2))

        times.append(f'{time:.4f}')
        booleans.append(averaged)

        logs.append(f'{logn:.4f}')
        linear.append(f'{lin:.4f}')
        nlogs.append(f'{nlogn:.4f}')
        n_squared.append(f'{n2:.4f}')
        n_22.append(f'{n22:.4f}')
    
    # Añadido de las columnas a la tabla:
    table.add_column('n', sizes)
    table.add_column('Averaged', booleans)
    table.add_column('Time', times)

    if f == selectionSort:
        table.add_column('O(nlog(n))', nlogs)
        table.add_column('O(n²)', n_squared)
        table.add_column('O(n²·²)', n_22)
    
    else:
        table.add_column('O(logn)', logs)
        table.add_column('O(n)', linear)
        table.add_column('O(nlogn)', nlogs)

    return table
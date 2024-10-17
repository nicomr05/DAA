from math import log
from prettytable import PrettyTable

from times import measure_time
from sorting_algs import *
from test_func import *

# Table creation function:
def create_table(sizes:list, alg=insertionSort, gen=ascending_order) -> PrettyTable:
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
    
    rows = []
    
    table.field_names = ['Size','Averaged','Time','O(nlog(n))','O(n²)','O(n²·²)']
    for size in sizes:
        time, flag = measure_time(size, alg=alg, gen=gen)
        
        lower_bound = f'{time / (size*log(size)):.4f}'
        exact_bound = f'{time / (size**2):.4f}'
        higher_bound = f'{time / (size**2.2):.4f}'
        
        rows.append([size, flag, time, lower_bound, exact_bound, higher_bound])
    
    table.add_rows(rows)
    
    return table

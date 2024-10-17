from math import log
from prettytable import PrettyTable

from times import measure_time
from sorting_algs import insertionSort
from test_func import ascending_order


# Table creation function:
def create_table(sizes:list, alg:function, gen:function) -> PrettyTable:
    '''
    Description
    -----------
    Create a table with the columns "n" (sample size), "Averaged"
    (indicates if the time was averaged), "Time" (execution time), "O(nlog(n))", "O(n²)"
    and "O(n²·²)" (algorithm relationships with a nlogn algorithm, a n² algorithm and a n²·²).
    
    Parameters
    ----------
    sizes: list
        List with sample sizes.
    alg: function
        Function of the algorithm to be evaluated. 
    gen: function
        Fuction that generates an vector.
    
    Returns
    -------
    PrettyTable
        Table with the information of the algorithm.
    '''
    table = PrettyTable()
    rows = []
    
    if alg == insertionSort and gen == ascending_order:
        table.field_names = ['Size','Averaged','Time','O(log(n))','O(n)','O(nlog(n))']

        for size in sizes:
            time, flag = measure_time(size, alg=alg, gen=gen)

            lower_bound = f'{time / (log(size)):.6f}'
            exact_bound = f'{time / size:.6f}'
            higher_bound = f'{time / (size*log(size)):.6f}'

            rows.append([size, flag, time, lower_bound, exact_bound, higher_bound])
    
    else:
        table.field_names = ['Size','Averaged','Time','O(nlog(n))','O(n²)','O(n²·²)']

        for size in sizes:
            time, flag = measure_time(size, alg=alg, gen=gen)

            lower_bound = f'{time / (size*log(size)):.6f}'
            exact_bound = f'{time / (size**2):.6f}'
            higher_bound = f'{time / (size**2.2):.6f}'

            rows.append([size, flag, time, lower_bound, exact_bound, higher_bound])
    
    table.add_rows(rows)
    
    return table

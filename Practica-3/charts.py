from prettytable import PrettyTable

from times import measure_time
from algs import kruskal, prim


# Table creation function:
def create_table(sizes:list, couts:list, cout_names:list, alg=kruskal) -> PrettyTable:
    '''
    Description
    -----------
    Create a table with the columns "Size" (sample size), "Averaged"
    (indicates if the time was averaged), "Time" (execution time) and
    the corresponding cout labels.

    Parameters
    ----------
    sizes : list
        List with sample sizes.
    couts : list
        List of lambda functions that will represent a certain cout and
        will be evaluated with each of the size n cases.
    cout_names : list
        List of labels for each of the couts. 
    alg : function
        Function of the algorithm to be evaluated. 

    Returns
    -------
    table : PrettyTable
        Table with the result of the algorithm evaluated on each of the samplesizes.
    '''
    table = PrettyTable()
    rows = []

    if alg == kruskal:
        adjacency = False
    elif alg == prim:
        adjacency = True

    table.field_names = ['Size','Averaged','Time'] + cout_names

    for size in sizes:
        time, flag = measure_time(size, alg=alg, adjacency=adjacency)
        inf, adj, sup = couts(size)

        rows.append([size, flag, time, f'{time/inf:.6f}', f'{time/adj:.6f}', f'{time/sup:.6f}'])

    table.add_rows(rows)

    return table

from prettytable import PrettyTable

from times import measure_time
from algs import kruskal, prim


# Table creation function:
def create_table(sizes:list, couts, cout_names:list, alg=kruskal) -> PrettyTable:
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

    if alg == kruskal:
        adjacency = False
    elif alg == prim:
        adjacency = True

    table.field_names = ['Size','Averaged','Time'] + cout_names

    for size in sizes:
        time, flag = measure_time(size, alg=alg, adjacency=adjacency)
        inf, adj, sup = couts(size)

        for _ in couts:
            rows.append([size, flag, time, inf, adj, sup])

    table.add_rows(rows)

    return table

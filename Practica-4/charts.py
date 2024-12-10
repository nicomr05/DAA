from prettytable import PrettyTable

from times import measure_time
from algs import MisxtureDP


# Table creation function:
def create_table(sizes:list, alphabet:tuple, couts, cout_names:list, alg=MisxtureDP) -> PrettyTable:
    '''
    Description
    -----------
    Create a table with the columns "Size" (sample size), "Averaged"
    (indicates if the time had to be averaged), "Time" (execution time)
    plus the corresponding cout labels.

    Parameters
    ----------
    sizes : list
        List with sample sizes.
    couts : function
        Lambda function that will output a tuple with the three necessary couts
        for a certain algorithm (inferior, adjusted and superior) and will be
        evaluated on each of the size n cases. For example:
        >>> first_set_of_couts = lambda n: (log(n), n, n**2)
    cout_names : list
        List of string labels corresponding to each of the couts. 
    alg : function
        Function of the algorithm to be evaluated.

    Returns
    -------
    PrettyTable
        Table with the result of the algorithm evaluated on each of the samplesizes.
    '''
    table = PrettyTable()
    rows = []

    table.field_names = ['Size','Averaged','Time'] + cout_names

    for size in sizes:
        time, flag = measure_time(size, alphabet=alphabet, alg=alg)
        inf, adj, sup = couts(size)

        rows.append([size, flag, time, f'{time/inf:.6f}', f'{time/adj:.6f}', f'{time/sup:.6f}'])

    table.add_rows(rows)

    return table

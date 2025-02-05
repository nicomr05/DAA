#!env/bin/python

from cases import TestCase
from sorting_algs import insertionSort, bubbleSort, selectionSort
from test_func import test, ascending_order, random_order, descending_order
from charts import create_table


# Vector variables:
TEST_VECTORS = [TestCase(input=[-9,4,13,-1,-5],    output=[-9,-5,-1,4,13]),
                TestCase(input=[6,-3,-15,5,4,5,2], output=[-15,-3,2,4,5,5,6]),
                TestCase(input=[13,4],             output=[4,13]),
                TestCase(input=[9],                output=[9]),
                TestCase(input=[7,6,6,5,4,3,2,1],  output=[1,2,3,4,5,6,6,7]),
                TestCase(input=[1,2,3,4,4,5,6,7],  output=[1,2,3,4,4,5,6,7])
                ]

SIZES = [50*2**x for x in range(8)]


# Main function:
def main() -> None:
    '''
    Description
    -----------
    It calls up the table creation functions and displays them on the screen.
    
    Returns
    -------
    None
    '''
    algorithms = [insertionSort, bubbleSort, selectionSort]
    alg_names = ['INSERTION SORT:','BUBBLE SORT:', 'SELECTION SORT:']
    
    generators = [ascending_order, random_order, descending_order]
    gen_names = ['ASCENDING ORDER:', 'RANDOM ORDER:', 'DESCENDING ORDER:']
    

    for alg in algorithms:
        test(TEST_VECTORS, alg=alg)
    
    for alg in range(len(algorithms)):
        print(f'\n\n{alg_names[alg]}\n')

        for gen in range(len(generators)):
            print('\t',gen_names[gen],'\n')
            print(f'{create_table(SIZES, alg=algorithms[alg], gen=generators[gen])}\n')

    

if __name__ == '__main__':
    main()

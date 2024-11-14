#!env/bin/python
from math import log

from times import test
from cases import TestCase
from algs import kruskal, prim
from charts import create_table


# Test and size variables:
TEST_CASES = [
            TestCase(V={0,1,2,3}, 
                     E={(0,2,9), (3,2,2), (0,3,6), (1,2,4), (0,1,5), (1,3,3)},
                     output={(3,2,2), (0,1,5), (1,3,3)}
                ),

            TestCase(V={0,1,2,3,4},
                     E={(3,4,6), (1,2,1), (0,2,9), (1,4,7), (0,3,4), (3,1,2), (2,3,3), (2,4,9), (0,4,8), (0,1,5)},
                     output={(3,4,6), (1,2,1), (0,3,4), (3,1,2)}
                )
]

SIZES = [10*2**x for x in range(1,9)]


# Main function:
def main() -> None:
    '''
    Description
    -----------
    Main function that initializes the test cases and then evaluates the times for
    different sized vectors and prints a table with the results.

    Returns
    -------
    None
    '''
    test(TEST_CASES, kruskal)
    test(TEST_CASES, prim)

    kruskal_couts = lambda n: (n, log(n)*n**2, n**2.5)
    prim_couts = lambda n: (n*log(n), n**2, n**2.5)

    kruskal_cout_names = ['O(n)', 'O(n²log(n))', 'O(n²·⁵)']
    prim_cout_names = ['O(nlog(n))', 'O(n²)', 'O(n²·⁵)']

    print(f'\tKRUSKAL:\n\n{create_table(SIZES, kruskal_couts, kruskal_cout_names, kruskal)}')
    print(f'\tPRIM:\n\n{create_table(SIZES, prim_couts, prim_cout_names, prim)}')


if __name__ == '__main__':
    main()

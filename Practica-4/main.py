#!env/bin/python

from math import log

from charts import create_table
from cases import TestCase
from times import test
from algs import MixtureDP, MixtureCX


# Test and size global variables
TEST_CASES = [
    TestCase(A="Hello", B="World", C="HelloWorld", output="AAAAABBBBB"),
    TestCase(A="Hello", B="World", C="WorldHello", output="BBBBBAAAAA"),
    TestCase(A="Hello", B="World", C="HWeolrllod", output="ABABABABAB")
]

SIZES = [10*2**x for x in range(1,9)]


# Main function
def main() -> None:
    '''
    Description
    -----------
    Main function that initializes the test cases and then evaluates the times for
    different sized vectors and prints a table with the results.

    Returns
    -------
    `None`
    '''
    test(TEST_CASES, alg=MixtureDP)
    test(TEST_CASES, alg=MixtureCX)

    dp_cout_names = ['O(nlog(n))', 'O(n²)', 'O(n²·²)']
    cx_cout_names = ['O(n)', 'O(nlog(n))', 'O(n²)']

    dp_couts = lambda n: ( n*log(n), n**2, n**2.2 )
    cx_couts = lambda n: ( n, n*log(n), n**2 )

    alphabets = [ (0,1), tuple([i for i in range(256)]) ]

    print("\nDYNAMIC PROGRAMING")
    for alphabet in alphabets:
        print(f"\n\tALPHABET : {alphabet}")
        print(create_table(SIZES, alphabet=alphabet, alg=MixtureDP, couts=dp_couts, cout_names=dp_cout_names))
    
    print("\nCOMPLEX DP ALGORITHM")
    for alphabet in alphabets:
        print(f"\n\tALPHABET : {alphabet}")
        print(create_table(SIZES, alphabet=alphabet, alg=MixtureCX, couts=cx_couts, cout_names=cx_cout_names))



if __name__ == "__main__":
    main()

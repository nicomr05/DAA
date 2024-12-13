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

    dp_cout_names = ['O(nlog(n))', 'O(n²)', 'O(n²·³)']
    cx_cout_names = ['O(n)', 'O(nlog(n))', 'O(n²)']

    dp_couts = lambda n: ( n*log(n), n**2, n**2.3 )
    cx_couts = lambda n: ( n, n*log(n), n**2 )

    alphabet_names = ["BINARY", "ASCII", "AB-LENGTH"]
    alphabets = [
        (0,1),
        tuple([chr(i) for i in range(256)]),
        "AB-LENGTH"
        ]


    print("\n\nDYNAMIC PROGRAMING")
    for idx in range(len(alphabets)):
        print(f"\n\tALPHABET : {alphabet_names[idx]}")
        print(create_table(SIZES, alphabet=alphabets[idx], alg=MixtureDP, couts=dp_couts, cout_names=dp_cout_names))

    print("\n\nCOMPLEX DP ALGORITHM")
    for idx in range(len(alphabets)):
        print(f"\n\tALPHABET : {alphabet_names[idx]}")
        print(create_table(SIZES, alphabet=alphabets[idx], alg=MixtureCX, couts=cx_couts, cout_names=cx_cout_names))



if __name__ == "__main__":
    main()

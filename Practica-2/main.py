#!env/bin/python

from cases import *
from sorting_algs import *
from test_func import test

TEST_VECTORS = [TestCase(input=[-9,4,13,-1,-5],    output=[-9,-5,-1,4,13]),
                TestCase(input=[6,-3,-15,5,4,5,2], output=[-15,-3,2,4,5,5,6]),
                TestCase(input=[13,4],             output=[4,13]),
                TestCase(input=[9],                output=[9]),
                TestCase(input=[7,6,6,5,4,3,2,1],  output=[1,2,3,4,5,6,6,7]),
                TestCase(input=[1,2,3,4,4,5,6,7],  output=[1,2,3,4,4,5,6,7])
                ]

# Variable de los tamaños de los casos:
SIZES = [50,
         100,
         200,
         400,
         800,
         1600,
         2000,
         3200,
         4000,
         5000,
         6000,
         6500
         ]


# Función principal:
def main() -> None:
    '''
    Description
    -----------
    LLama a las funciones de creación de tablas y las muestra por pantalla.
    
    Returns
    -------
    None
    '''
    print('\n', test(TEST_VECTORS, f=insertionSort), '\n',
                test(TEST_VECTORS, f=bubbleSort), '\n',
                test(TEST_VECTORS, f=selectionSort), '\n',
    )

    for size in SIZES:
        pass



if __name__ == '__main__':
    main()

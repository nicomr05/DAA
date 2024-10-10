#!env/bin/python

from clases_casos import Caso, CasoPrueba
from func_ord import *

VECTORES_PRUEBA = [CasoPrueba(input=[-9,4,13,-1,-5],    output=[-9,-5,-1,4,13]),
                   CasoPrueba(input=[6,-3,-15,5,4,5,2], output=[-15,-3,2,4,5,5,6]),
                   CasoPrueba(input=[13,4],             output=[4,13]),
                   CasoPrueba(input=[9],                output=[9]),
                   CasoPrueba(input=[7,6,6,5,4,3,2,1],  output=[1,2,3,4,5,6,6,7]),
                   CasoPrueba(input=[1,2,3,4,4,5,6,7],  output=[1,2,3,4,4,5,6,7])
                   ]


# Función de testeo:
def test(casos:list[CasoPrueba], f=insertionSort) -> str|AssertionError:
    '''
    Description
    -----------
    Testea los casos de prueba con la función del algoritmo que se le indique.
    
    Parameters
    ----------
    casos : list[CasoPrueba]
        Lista de objetos CasoPrueba que se quieren comprobar.

    Returns
    -------
    str
        String que confirma que la ejecución es correcta, por si se quiere mostrar por pantalla.
    
    AssertionError
        Error con su mensaje asociado que indica que los tests no se ejecutaron correctamente.
    '''
    for caso in casos:
        sol = f(caso.input)
        
        assert caso.output == sol, f'Lista {caso.input}. Esperada salida {caso.output}, pero obtuvo {sol}.'
    
    return 'Ejecución correcta.'

# Función principal:
def main() -> None:
    '''
    '''
    print('\n', test(VECTORES_PRUEBA, f=insertionSort), '\n',
    test(VECTORES_PRUEBA, f=bubbleSort), '\n',
    test(VECTORES_PRUEBA, f=selectionSort), '\n',
    )


if __name__ == '__main__':
    main()
    #print('hola')

#!env/bin/python

from clases_casos import *
from func_busqueda import *
from tiempo import *
from charts import create_table

# Variable para los casos de prueba:
CASOS_PRUEBA = [CasoPrueba(input=[1,2,3,4,5,6], output=set([(1,6),(2,5),(3,4)]), target=7),
                CasoPrueba(input=[1,2,3,4,5,6,7,8,9,10], output=set([(5,10),(6,9),(7,8)]), target=15),
                CasoPrueba(input=[1,3,5], output=set(), target=20),
                CasoPrueba(input=[], output=set(), target=3)
                ]


# Función de testeo:
def test(casos:list[CasoPrueba], f=SearchPairsWithLists) -> str|AssertionError:
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
        sol = f(caso.input, caso.target)
        
        if isinstance(sol, list):
            sol = set(sol)
        
        assert caso.output == sol, f'Lista {caso.input}. Esperada salida {caso.output}, pero obtuvo {sol}.'
    
    return 'Ejecución correcta.'


# Función principal:
def main() -> None:
    '''
    Description
    -----------
    LLama a las funciones de creación de tablas y las muestra por pantalla.
    Además, hemos dejado comentadas las llamadas
    
    Returns
    -------
    None
    '''
    test(CASOS_PRUEBA, SearchPairsWithLists)
    test(CASOS_PRUEBA, SearchPairsWithSets)
    
    print()
    print(f'TABLA CON LISTAS:\n{create_table(SIZES, SearchPairsWithLists)}\n')
    print(f'TABLA CON CONJUNTOS:\n{create_table(SIZES, SearchPairsWithSets)}\n')

if __name__ == '__main__':
    main()

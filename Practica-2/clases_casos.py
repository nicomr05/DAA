# Clases de los Casos:
class Caso:
    '''
    Description
    -----------
    Clase para un caso que se quiere evaluar.
    La clase contiene el vector y el target necesarios para evaluar los
    algoritmos.

    Attributes
    ----------
    input : list|set
        Vector de números sobre el que se aplicarán los algoritmos.
    target : int
        Cantidad objetivo que sumarán las parejas de números.
        
    Methods
    -------
    __init__(self, input, target) -> None:
        Constructor de la clase Caso, inicializa sus atributos.
    '''
    def __init__(self, input) -> None:
        '''
        Description
        -----------
        Asigna atributos al objeto.
        
        Parameters
        ----------
        input : list|set
            Vector de números sobre el que se aplicarán los algoritmos.
        target : int
            Cantidad objetivo que sumarán las parejas de números.
        
        Returns
        -------
        None.
        '''
        self._input = input

    @property
    def input(self) -> list:
        return self._input

class CasoPrueba(Caso):
    '''
    Description
    -----------
    Clase para un caso de prueba que se quiere evaluar.
    La clase CasoPrueba es una clase hija de la clase Caso, por lo que
    hereda sus atributos, pero además añade la solución esperada al ejecutar
    los algoritmos.

    Attributes
    ----------
    input : list|set
        vector de números sobre el que se aplicarán los algoritmos.
    target : int
        cantidad objetivo que sumarán las parejas de números.
    output : set[tuple]
        Conjunto con las tuplas esperadas al pasar los algoritmos por el vector.
        
    Methods
    -------
    __init__(self, input, output, target) -> None:
        Constructor de la clase CasoPrueba, inicializa sus atributos.
    '''
    def __init__(self, input, output) -> None:
        '''
        '''
        Caso.__init__(self,input)
        self._output = output
    
    @property
    def output(self) -> list:
        return self._output

class Circulo():

    '''
    TEST:

    >>> [Circulo().area()]
    [78.5]
    >>> [Circulo().perimetro()]
    [31.4]
    >>> [Circulo().multiplicacion()]
    [25]
    
    '''

    def area(self, radio=5):
        self.radio = radio
        resultado = (3.14*(radio*radio))
        try:
            if radio>0:
                return resultado
            else:
                print("El radio del circulo debe ser mayor a 0 (cero)")
        except:
            print("No es posible que el radio sea menor o igual a 0 (cero)")

    def perimetro(self, radio=5):
        self.radio = radio
        resultado = round((2*3.14)*radio, 2)
        try:
            if radio>0:
                return resultado
            else:
                print("El radio del circulo debe ser mayor a 0 (cero)")
        except:
            print("No es posible que el radio sea menor o igual a 0 (cero)")

    def multiplicacion(self, n=5, radio=5):
        self.n = radio
        self.radio = radio
        resultado = n*radio
        try:
            if n>0:
                return resultado
            else:
                while n <= 0:
                    print("La multiplicación del circulo debe ser mayor a 0 (cero)")
        except:
            print("No es posible que el radio sea menor o igual a 0 (cero)")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
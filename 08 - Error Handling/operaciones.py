class   Mates:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def suma_lista(self):
        resultado = 0
        for elem in self.lista:
            resultado = elem + resultado
        return resultado
    
    def producto_lista(self):
        resultado = 1
        for elem in self.lista:
            resultado = elem*resultado
        return resultado
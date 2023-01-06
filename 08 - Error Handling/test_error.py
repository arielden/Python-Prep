import unittest
from operaciones import Mates

class PruebaError(unittest.TestCase):

    def testSuma (self):
        #lista_prueba = [1,2,3,4,5]
        matematicas_prueba = Mates(list(range(1,4)))
        resultado = matematicas_prueba.suma_lista()
        esperado = 6
        self.assertEqual(resultado, esperado)

    def testProducto (self):
        lista_prueba = [1,2,3]
        matematicas_prueba = Mates(list(range(1,4)))
        resultado = matematicas_prueba.producto_lista()
        esperado = 6
        self.assertEqual(resultado, esperado)

unittest.main(argv=[''], verbosity=2, exit=False)
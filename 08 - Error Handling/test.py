from operaciones import Mates

matematica = Mates(list(range(1,5)))

result1 = matematica.suma_lista()
print(f"La suma es: {result1}")

result2 = matematica.producto_lista()
print(f"El producto es: {result2}")
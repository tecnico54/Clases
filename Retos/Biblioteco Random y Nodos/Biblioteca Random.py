import numpy as np
class nodo:
    def __init__(self, dato, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente
    def __str__(self):
        return str(self.dato)
lista = nodo
lista1 = nodo(1)
lista2 = nodo(2)
lista3 = nodo(3)
lista4 = nodo(4)
lista5 = nodo(5)
class biblioteca_random():
    dato = np.random.randint(-1, 100)
    print(f"El Dato aleatorio es: ")
    print(dato)
    print(f"Los datos son: ")
    print(lista1, lista2, lista3, lista4, lista5)
class nodo():
    def __init__(self, dato, apuntador, siguiente = None):
        self.dato = dato
        self.apuntador = apuntador
        self.siguiente = siguiente
    def __str__(self):
        return str(self.dato)
def recorrer(lista):
    if lista != None:
        print(lista.dato)
        lista = lista.siguiente
        pass
    else:
        print(f"No corresponde ")
lista = nodo
lista1 = nodo(1, None)
lista2 = nodo(2, None)
lista3 = nodo(3, None)
lista4 = nodo(4, None)
lista5 = nodo(5, None)
print(f"Los datos son: ")
print(lista1, lista2, lista3, lista4, lista5)
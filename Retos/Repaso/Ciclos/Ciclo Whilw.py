list = [2, 3, 4, 5]
class nodo:
    def __init__(self, lista, apuntador = None):
        self.lista = lista
        self.apuntador = apuntador
    def __str__(self):
        return str(self.lista)
lista = nodo
lista1 = nodo(2, None)
lista2 = nodo(3, None)
lista3 = nodo(4, None)
lista4 = nodo(1, None)
lista5 = nodo(5, None)
print(f"La lista es: ")
print(lista1, lista2, lista4, lista3, lista5)
while list == [2, 3, 4, 5]:
    print(f"La lista modificada es: {list}")
    list = 5
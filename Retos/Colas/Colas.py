from .tipos import Item
class Nodo:
    def __init__(self, valor: Item):
        self.valor = valor
        self.siguiente = None
class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    def esta_vacia(self):
        return self.primero is None
    def encolar(self, valor: Item):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
        self.ultimo = nuevo_nodo
    def desencolar(self):
        if self.esta_vacia():
            return None
        valor = self.primero.valor
        self.primero = self.primero.siguiente
        if self.primero is None:
            self.ultimo = None
        return valor
    def ver_listado(self):
        mostrar = read_root
        mostrar = estado
        mostrar = encolar
        mostrar = desencolar
        mostrar =  ver_todos
        return mostrar
    pass
    def ver_primero(self):
        mostrar = read_root
        return mostrar
    pass
    def ver_ultimo(self):
        show = ver_todos
        return show
    pass
    def contar(self):
        total = 5
        return total

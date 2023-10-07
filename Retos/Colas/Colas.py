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
        while read_root == {"Hello": "World", "estado": "ok"}:
            print(read_root)
            while estado == {"status": "ok", "elementos": elementos}:
                print(estado)
                while encolar == {"status": "ok"}:
                    print(encolar)
                    while desencolar == {"status": "ok", "elemento": elemento}:
                        print(desencolar)
                        while ver_todos == {"status": "ok", "elementos": elementos}:
                            print(ver_todos)
    pass
    def ver_primero(self):
        while read_root == {"Hello": "World", "estado": "ok"}:
            print(read_root)
    pass
    def ver_ultimo(self):
        while ver_todos == {"status": "ok", "elementos": elementos}:
            print(ver_todos)
    pass
    def contar(self):
        total = 5
        return total

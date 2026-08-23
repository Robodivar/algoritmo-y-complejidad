class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class PilaLista:
    def __init__(self):
        self.__cabeza = None
        self.__tamaño = 0

    @classmethod
    def crear(cls):
        return cls()

    def apilar(self, x):
        self.__cabeza = Nodo(x, self.__cabeza)
        self.__tamaño += 1

    def desapilar(self):
        if self.estaVacia():
            raise IndexError("No se puede desapilar: la pila está vacía.")
        elemento = self.__cabeza.dato
        self.__cabeza = self.__cabeza.siguiente
        self.__tamaño -= 1
        return elemento

    def cima(self):
        if self.estaVacia():
            raise IndexError("No se puede consultar la cima: la pila está vacía.")
        return self.__cabeza.dato

    def estaVacia(self):
        return self.__cabeza is None

    def tamaño(self):
        return self.__tamaño

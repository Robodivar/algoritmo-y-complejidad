from ctypes import py_object

class PilaArreglo:
    def __init__(self, capacidad_inicial=4):
        if capacidad_inicial <= 0:
            raise ValueError("La capacidad inicial debe ser mayor que cero.")
        self.__capacidad = capacidad_inicial
        self.__datos = (py_object * self.__capacidad)()
        self.__tope = -1

    @classmethod
    def crear(cls):
        return cls()

    def apilar(self, x):
        if self.__tope + 1 == self.__capacidad:
            self.__redimensionar(self.__capacidad * 2)
        self.__tope += 1
        self.__datos[self.__tope] = x

    def desapilar(self):
        if self.estaVacia():
            raise IndexError("No se puede desapilar: la pila está vacía.")
        elemento = self.__datos[self.__tope]
        self.__datos[self.__tope] = None
        self.__tope -= 1
        return elemento

    def cima(self):
        if self.estaVacia():
            raise IndexError("No se puede consultar la cima: la pila está vacía.")
        return self.__datos[self.__tope]

    def estaVacia(self):
        return self.__tope == -1

    def tamaño(self):
        return self.__tope + 1

    def __redimensionar(self, nueva_capacidad):
        nuevo = (py_object * nueva_capacidad)()
        for i in range(self.__tope + 1):
            nuevo[i] = self.__datos[i]
        self.__datos = nuevo
        self.__capacidad = nueva_capacidad

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)

        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, actual, nuevo_nodo):
        if nuevo_nodo.valor < actual.valor:
            if actual.izquierdo is None:
                actual.izquierdo = nuevo_nodo
            else:
                self._insertar_recursivo(actual.izquierdo, nuevo_nodo)

        elif nuevo_nodo.valor > actual.valor:
            if actual.derecho is None:
                actual.derecho = nuevo_nodo
            else:
                self._insertar_recursivo(actual.derecho, nuevo_nodo)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, actual, valor):
        if actual is None:
            return False

        if actual.valor == valor:
            return True

        if valor < actual.valor:
            return self._buscar_recursivo(actual.izquierdo, valor)

        return self._buscar_recursivo(actual.derecho, valor)

    def inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, actual, resultado):
        if actual is not None:
            self._inorden_recursivo(actual.izquierdo, resultado)
            resultado.append(actual.valor)
            self._inorden_recursivo(actual.derecho, resultado)

    def preorden(self):
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado

    def _preorden_recursivo(self, actual, resultado):
        if actual is not None:
            resultado.append(actual.valor)
            self._preorden_recursivo(actual.izquierdo, resultado)
            self._preorden_recursivo(actual.derecho, resultado)

    def postorden(self):
        resultado = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado

    def _postorden_recursivo(self, actual, resultado):
        if actual is not None:
            self._postorden_recursivo(actual.izquierdo, resultado)
            self._postorden_recursivo(actual.derecho, resultado)
            resultado.append(actual.valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, actual, valor):
        if actual is None:
            return None

        if valor < actual.valor:
            actual.izquierdo = self._eliminar_recursivo(
                actual.izquierdo, valor
            )

        elif valor > actual.valor:
            actual.derecho = self._eliminar_recursivo(
                actual.derecho, valor
            )

        else:
            # Caso 1: no tiene hijos
            if actual.izquierdo is None and actual.derecho is None:
                return None

            # Caso 2: tiene solamente hijo derecho
            if actual.izquierdo is None:
                return actual.derecho

            # Caso 3: tiene solamente hijo izquierdo
            if actual.derecho is None:
                return actual.izquierdo

            # Caso 4: tiene dos hijos
            sucesor = self._minimo(actual.derecho)
            actual.valor = sucesor.valor
            actual.derecho = self._eliminar_recursivo(
                actual.derecho, sucesor.valor
            )

        return actual

    def _minimo(self, nodo):
        actual = nodo

        while actual.izquierdo is not None:
            actual = actual.izquierdo

        return actual


# Programa principal
arbol = ArbolBinarioBusqueda()

arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(80)

print("Recorrido inorden:", arbol.inorden())
print("Recorrido preorden:", arbol.preorden())
print("Recorrido postorden:", arbol.postorden())

print("¿Está el 40?", arbol.buscar(40))
print("¿Está el 90?", arbol.buscar(90))

arbol.eliminar(30)

print("Inorden después de eliminar 30:", arbol.inorden())
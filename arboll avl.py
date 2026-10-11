"""Árbol AVL en Python.

Convenciones:
  - Altura de un subárbol vacío = 0; altura de una hoja = 1.
  - Factor de Equilibrio (FE) = altura(derecho) - altura(izquierdo).
  - Un nodo está desbalanceado cuando FE = 2 o FE = -2.
"""


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1  # una hoja tiene altura 1


class ArbolAVL:
    def __init__(self):
        self.raiz = None
        self.ultima_rotacion = None  # guarda el último caso aplicado (para mostrar/probar)

    # ------------------------------------------------------------------
    # Alturas y factor de equilibrio
    # ------------------------------------------------------------------
    @staticmethod
    def altura(nodo):
        return nodo.altura if nodo else 0

    def actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self.altura(nodo.izq), self.altura(nodo.der))

    def factor_equilibrio(self, nodo):
        """FE = altura(derecho) - altura(izquierdo)."""
        return self.altura(nodo.der) - self.altura(nodo.izq) if nodo else 0

    # ------------------------------------------------------------------
    # Rotaciones simples
    # ------------------------------------------------------------------
    def rotacion_derecha(self, z):
        """Caso LL: el hijo izquierdo 'y' sube y 'z' pasa a ser su hijo derecho."""
        y = z.izq
        t = y.der
        y.der = z
        z.izq = t
        self.actualizar_altura(z)  # primero el nodo que bajó
        self.actualizar_altura(y)
        return y

    def rotacion_izquierda(self, z):
        """Caso RR: el hijo derecho 'y' sube y 'z' pasa a ser su hijo izquierdo."""
        y = z.der
        t = y.izq
        y.izq = z
        z.der = t
        self.actualizar_altura(z)
        self.actualizar_altura(y)
        return y

    # ------------------------------------------------------------------
    # Balanceo de un nodo (detecta LL, RR, LR, RL)
    # ------------------------------------------------------------------
    def balancear(self, nodo):
        self.actualizar_altura(nodo)
        fe = self.factor_equilibrio(nodo)

        if fe == -2:  # pesado a la izquierda
            if self.factor_equilibrio(nodo.izq) <= 0:
                self.ultima_rotacion = ("LL", nodo.valor)
                return self.rotacion_derecha(nodo)
            # LR: rotación izquierda sobre el hijo, luego derecha sobre el nodo
            self.ultima_rotacion = ("LR", nodo.valor)
            nodo.izq = self.rotacion_izquierda(nodo.izq)
            return self.rotacion_derecha(nodo)

        if fe == 2:  # pesado a la derecha
            if self.factor_equilibrio(nodo.der) >= 0:
                self.ultima_rotacion = ("RR", nodo.valor)
                return self.rotacion_izquierda(nodo)
            # RL: rotación derecha sobre el hijo, luego izquierda sobre el nodo
            self.ultima_rotacion = ("RL", nodo.valor)
            nodo.der = self.rotacion_derecha(nodo.der)
            return self.rotacion_izquierda(nodo)

        return nodo  # ya está balanceado

    # ------------------------------------------------------------------
    # Inserción (reglas del BST + rebalanceo al volver de la recursión)
    # ------------------------------------------------------------------
    def insertar(self, valor):
        self.ultima_rotacion = None
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izq = self._insertar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._insertar(nodo.der, valor)
        else:
            return nodo  # sin duplicados
        return self.balancear(nodo)

    # ------------------------------------------------------------------
    # Recorridos y utilidades
    # ------------------------------------------------------------------
    def inorden(self):
        res = []

        def rec(n):
            if n:
                rec(n.izq)
                res.append(n.valor)
                rec(n.der)

        rec(self.raiz)
        return res

    def preorden(self):
        res = []

        def rec(n):
            if n:
                res.append(n.valor)
                rec(n.izq)
                rec(n.der)

        rec(self.raiz)
        return res

    def mostrar(self):
        """Imprime el árbol de lado: la raíz a la izquierda, la rama derecha arriba."""
        def rec(n, nivel):
            if n is None:
                return
            rec(n.der, nivel + 1)
            fe = self.factor_equilibrio(n)
            fe_txt = f"{fe:+d}" if fe else "0"
            print("    " * nivel + f"{n.valor} (FE={fe_txt}, h={n.altura})")
            rec(n.izq, nivel + 1)

        if self.raiz is None:
            print("(árbol vacío)")
        else:
            rec(self.raiz, 0)

    def es_avl_valido(self):
        """Verifica BST, alturas guardadas correctas y |FE| <= 1 en todos los nodos."""
        def rec(n, minimo, maximo):
            if n is None:
                return True, 0
            if (minimo is not None and n.valor <= minimo) or (maximo is not None and n.valor >= maximo):
                return False, 0
            ok_i, hi = rec(n.izq, minimo, n.valor)
            ok_d, hd = rec(n.der, n.valor, maximo)
            h = 1 + max(hi, hd)
            ok = ok_i and ok_d and abs(hd - hi) <= 1 and n.altura == h
            return ok, h

        return rec(self.raiz, None, None)[0]


# ----------------------------------------------------------------------
# Demostración con las 3 secuencias
# ----------------------------------------------------------------------
if __name__ == "__main__":
    secuencias = [
        [10, 20, 30, 40, 50, 25],
        [30, 10, 40, 20, 15, 35],
        [50, 40, 30, 20, 10, 25],
    ]
    for seq in secuencias:
        print("=" * 50)
        print("Secuencia:", seq)
        arbol = ArbolAVL()
        for v in seq:
            arbol.insertar(v)
            rot = arbol.ultima_rotacion
            texto = f"rotación {rot[0]} sobre {rot[1]}" if rot else "sin rotación"
            print(f"\nInsertar {v}: {texto}")
            arbol.mostrar()
            assert arbol.es_avl_valido()
        print("\nInorden :", arbol.inorden())
        print("Preorden:", arbol.preorden())
from pila_arreglo import PilaArreglo
from pila_enlazada import PilaLista

def comprobar(mensaje, condicion):
    if not condicion:
        raise AssertionError("FALLÓ: " + mensaje)
    print("OK:", mensaje)

def probar(nombre, Pila):
    print(f"\n--- {nombre} ---")
    p = Pila.crear()
    comprobar("crear() produce una pila vacía", p.estaVacia())
    comprobar("tamaño() inicial = 0", p.tamaño())

    for x in (10, 20, 30, 40, 50):
        p.apilar(x)

    comprobar("apilar() agrega 5 elementos", p.tamaño() == 5)
    comprobar("estaVacia() = False", not p.estaVacia())
    comprobar("cima() = 50", p.cima() == 50)
    comprobar("desapilar() devuelve 50", p.desapilar() == 50)
    comprobar("cima() después de desapilar = 40", p.cima() == 40)
    comprobar("tamaño() = 4", p.tamaño() == 4)

    while not p.estaVacia():
        p.desapilar()

    comprobar("la pila termina vacía", p.estaVacia())
    comprobar("tamaño() final = 0", p.tamaño() == 0)

    try:
        p.desapilar()
    except IndexError as e:
        comprobar("desapilar() controla pila vacía", "pila está vacía" in str(e))

    try:
        p.cima()
    except IndexError as e:
        comprobar("cima() controla pila vacía", "pila está vacía" in str(e))

def comparar():
    a = PilaArreglo.crear()
    l = PilaLista.crear()
    for x in (5, 8, 13, 21, 34):
        a.apilar(x)
        l.apilar(x)

    comprobar("ambas tienen igual tamaño", a.tamaño() == l.tamaño())
    comprobar("ambas tienen igual cima", a.cima() == l.cima())

    while not a.estaVacia():
        comprobar("ambas devuelven el mismo elemento", a.desapilar() == l.desapilar())

    comprobar("ambas terminan vacías", a.estaVacia() and l.estaVacia())

if __name__ == "__main__":
    probar("Arreglo dinámico", PilaArreglo)
    probar("Lista enlazada", PilaLista)
    print("\n--- Comparación ---")
    comparar()
    print("\nTODAS LAS PRUEBAS FINALIZARON CORRECTAMENTE.")

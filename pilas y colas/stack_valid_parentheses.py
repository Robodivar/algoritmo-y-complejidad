class Solution:
    def isValid(self, s: str) -> bool:
        pila = []
        pares = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for caracter in s:
            if caracter in '([{':
                pila.append(caracter)
            elif caracter in ')]}':
                if not pila or pila[-1] != pares[caracter]:
                    return False
                pila.pop()

        return len(pila) == 0

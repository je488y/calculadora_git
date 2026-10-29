def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def potencia(base, exponente):
    return base ** exponente

def raiz_cuadrada(n):
    if n < 0:
        raise ValueError("No existe raiz real de un negativo")
    return n ** 0.5
class HistorialOperaciones:
    def __init__(self):
        self._historial = []

    def registrar(self, operacion, a, b, resultado):
        self._historial.append(
            {"operacion": operacion, "a": a, "b": b, "resultado": resultado}
        )

    def obtener_historial(self):
        return self._historial.copy()
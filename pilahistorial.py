REMOVER = '-'
AGREGAR = '+'

class Accion:
    def __init__(self, cancion, tipo=AGREGAR, posicion=None):
        """Recibe un objeto de la clase cancion y un tipo de accion (AGREGAR/REMOVER)"""
        self.tipo = tipo
        self.cancion = cancion
        self.posicion = posicion

class PilaHistorial:
    """Pila que contiene objetos de la clase Accion"""

    def __init__(self):
        self.historial = []

    def apilar(self, accion):
        self.historial.append(accion)

    def desapilar(self):
        if not self.historial:
            return None
        return self.historial.pop()

    def ver_tope(self):
        if not self.historial:
            return None
        tope = self.historial.pop()
        self.historial.append(tope)
        return tope
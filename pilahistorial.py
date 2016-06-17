REMOVER = '-'
AGREGAR = '+'

class Accion:
    def __init__(self, cancion, tipo = AGREGAR, posicion = None):
        """Recibe un objeto de la clase cancion y un tipo de accion (AGREGAR/REMOVER)"""
        self.tipo = tipo
        self.cancion = cancion
        self.posicion = posicion

class PilaHistorial:
    """Pila que contiene objetos de la clase Accion"""

    def __init__(self):
        """Inicializa una pila vacia"""
        self.historial = []

    def apilar(self, accion):
        """Agrega una acción en el tope de la pila"""
        self.historial.append(accion)

    def desapilar(self):
        """Elimina y devuelve el elemento del tope de la pila"""
        if not self.historial:
            return None
        return self.historial.pop()

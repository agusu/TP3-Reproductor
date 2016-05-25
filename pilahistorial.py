class Accion:
    def __init__(self, cancion, tipo=SUSTRACCION):
        """Recibe un objeto de la clase cancion y un tipo de accion (ADICION/SUSTRACCION)"""
        self.tipo=tipo
        self.cancion=cancion
class PilaHistorial:
    """Pila que contiene objetos de la clase Accion"""
    def __init__(self):
        self.historial=[]

    def apilar(self, accion):
        self.historial.append(accion)

    def desapilar(self):
        return self.historial.pop()

    def ver_tope(self):
        tope = self.historial.pop()
        self.historial.append(tope)
        return tope
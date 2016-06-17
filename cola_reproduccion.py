import os
from cancion import Cancion
from pilahistorial import PilaHistorial, Accion, REMOVER, AGREGAR

EXTENSIONES_ACEPTADAS = ("wav", "mp3", "flac", "ogg", "wma")

class ColaDeReproduccion:
    """Clase que representa la cola de reproduccion del reproductor. Permite agregar y remover
    canciones, ademas de poder hacer y deshacer estas acciones. Las canciones se guardan en la
    cola como objetos de clase Cancion."""

    def __init__(self, lista_canciones=[]):
        """ Recibe una lista de objetos de clase Cancion con las canciones que se quieren
        reproducir."""
        self.canciones = lista_canciones
        self.actual = 0
        self.largo = len(lista_canciones)
        self.historial = PilaHistorial()
        self.deshechos = PilaHistorial()

    def cancion_actual(self):
        """ Devuelve un objeto de clase Cancion que corresponde a la cancion actual, o None si no
        hay canciones cargadas en la cola."""
        if not self.canciones:
            return None
        return self.canciones[self.actual]

    def cancion_siguiente(self):
        """ Devuelve un objeto de clase Cancion que corresponde a la cancion siguiente en la cola,
        o None si no hay mas canciones."""
        if self.actual == self.largo-1 or not self.canciones:
            return None
        self.actual += 1
        return self.canciones[self.actual]

    def cancion_anterior(self):
        """ Devuelve un objeto de clase Cancion que corresponde a la cancion anterior en la cola,
        o None si no hay canciones en la misma o la actual es la primera de la cola."""
        if self.actual == 0 or not self.canciones:
            return None
        self.actual -= 1
        return self.canciones[self.actual]

    def agregar_cancion(self, ruta_cancion):
        """ Agrega una Cancion a la cola a partir de su ruta. Devuelve True si se agrego
        correctamente, False en caso contrario. Esta accion puede deshacerse y rehacerse."""
        if not os.path.exists(ruta_cancion) or \
                not os.path.splitext(ruta_cancion)[1][1:] in EXTENSIONES_ACEPTADAS:
            return False
        try:
            self.canciones.append(Cancion(ruta_cancion))
            self.largo += 1
            self.historial.apilar(Accion(Cancion(ruta_cancion)))
            return True
        except IOError:
            return False

    def remover_cancion(self, ruta_cancion):
        """ Remueve una Cancion de la cola a partir de su ruta. Devuelve True si se removio
        correctamente, False en caso contrario. Esta accion puede deshacerse y rehacerse."""
        if not self.canciones:
            return False
        for x in range(self.largo):
            if self.canciones[x].obtener_ruta() == ruta_cancion:
                self.historial.apilar(Accion(self.canciones.pop(x), REMOVER, x))
                self.largo -= 1
                return True
        return False

    def deshacer_modificacion(self):
        """ Deshace la ultima accion realizada. Devuelve True si pudo deshacerse, False en caso
        contrario."""
        try:
            ultima_accion = self.historial.desapilar()
            if not ultima_accion:
                raise TypeError
            if ultima_accion.tipo == AGREGAR:
                # si uso remover_cancion, se apila la accion de remover en el historial, no sirve.
                self._deshacer_agregado(ultima_accion)
            else:
                # lo mismo que lo anterior
                self._deshacer_remocion(ultima_accion)
            self.deshechos.apilar(ultima_accion)
            return True
        except TypeError:  # pila esta vacia
            return False

    def _deshacer_agregado(self, accion):
        """Recibe por parametro un objeto de la clase Accion y agrega la cancion que contiene a la Cola de Rep."""
        if accion.posicion:
            self.canciones.pop(accion.posicion)
        else:
            self.canciones.pop()
        self.largo -= 1
    def _deshacer_remocion(self, accion):
        """Recibe por parametro un objeto de la clase Accion y remueve la cancion que contiene de la Cola de Rep."""
        if accion.posicion:
            self.canciones.insert(accion.cancion, accion.posicion)
        else:
            self.canciones.append(accion.cancion)
        self.largo += 1
    def rehacer_modificacion(self):
        """ Rehace la ultima accion que se deshizo. Devuelve True si pudo rehacerse, False en caso
        contrario."""
        try:
            ultima_deshecha = self.deshechos.desapilar()
            if not ultima_deshecha:
                raise TypeError
            if ultima_deshecha and ultima_deshecha.tipo == AGREGAR:
                self._deshacer_remocion(ultima_deshecha)
            else:
                self._deshacer_agregado(ultima_deshecha)
            self.historial.apilar(ultima_deshecha)
            return True
        except TypeError:
            return False

    def obtener_n_siguientes(self, n_canciones):
        """ Devuelve una lista con las siguientes n canciones. Si en la cola de reproduccion
        quedan menos canciones que las pedidas, la lista contendra menos elementos que los
        pedidos."""
        n_siguientes = []
        for x in range(self.actual + 1, self.actual + n_canciones + 1):
            try:
                n_siguientes.append(self.canciones[x])
            except IndexError:
                break
        return n_siguientes

import os

from cancion import Cancion

EXTENSIONES_ACEPTADAS = ("wav", "mp3", "flac", "ogg", "wma")

class ColaDeReproduccion:
	"""Clase que representa la cola de reproduccion del reproductor. Permite agregar y remover 
	canciones, ademas de poder hacer y deshacer estas acciones. Las canciones se guardan en la 
	cola como objetos de clase Cancion."""
	
	def __init__(self, lista_canciones = []):
		""" Recibe una lista de objetos de clase Cancion con las canciones que se quieren 
		reproducir."""
		raise NotImplementedError()

	def cancion_actual(self):
		""" Devuelve un objeto de clase Cancion que corresponde a la cancion actual, o None si no 
		hay canciones cargadas en la cola."""
		raise NotImplementedError()

	def cancion_siguiente(self):
		""" Devuelve un objeto de clase Cancion que corresponde a la cancion siguiente en la cola, 
		o None si no hay mas canciones."""
		raise NotImplementedError()

	def cancion_anterior(self):
		""" Devuelve un objeto de clase Cancion que corresponde a la cancion anterior en la cola, 
		o None si no hay canciones en la misma o la actual es la primera de la cola."""
		raise NotImplementedError()

	def agregar_cancion(self, ruta_cancion):
		""" Agrega una Cancion a la cola a partir de su ruta. Devuelve True si se agrego 
		correctamente, False en caso contrario. Esta accion puede deshacerse y rehacerse."""
		raise NotImplementedError()

	def remover_cancion(self, ruta_cancion):
		""" Remueve una Cancion de la cola a partir de su ruta. Devuelve True si se removio 
		correctamente, False en caso contrario. Esta accion puede deshacerse y rehacerse."""
		raise NotImplementedError()

	def deshacer_modificacion(self):
		""" Deshace la ultima accion realizada. Devuelve True si pudo deshacerse, False en caso 
		contrario."""
		raise NotImplementedError()

	def rehacer_modificacion(self):
		""" Rehace la ultima accion que se deshizo. Devuelve True si pudo rehacerse, False en caso 
		contrario."""
		raise NotImplementedError()

	def obtener_n_siguientes(self, n_canciones):
		""" Devuelve una lista con las siguientes n canciones. Si en la cola de reproduccion 
		quedan menos canciones que las pedidas, la lista contendra menos elementos que los 
		pedidos."""
		raise NotImplementedError()

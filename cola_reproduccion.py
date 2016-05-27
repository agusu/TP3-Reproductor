EXTENSIONES_ACEPTADAS = ("wav", "mp3", "flac", "ogg", "wma")
SUSTRACCION = '-'
ADICION = '+' 
# puse los import despues por que sino no funcionaba la llamada a SUSTRACCION en pilahistorial

import os
from cancion import Cancion
from pilahistorial import PilaHistorial, Accion



class ColaDeReproduccion:
	"""Clase que representa la cola de reproduccion del reproductor. Permite agregar y remover 
	canciones, ademas de poder hacer y deshacer estas acciones. Las canciones se guardan en la 
	cola como objetos de clase Cancion."""
	
	def __init__(self, lista_canciones = []):
		""" Recibe una lista de objetos de clase Cancion con las canciones que se quieren 
		reproducir."""
		self.canciones = lista_canciones
		self.actual = 0   
		self.historial = PilaHistorial()
	
	def cancion_actual(self):
		""" Devuelve un objeto de clase Cancion que corresponde a la cancion actual, o None si no 
		hay canciones cargadas en la cola."""
		if not self.canciones:
			#raise ValueError('La cola de reproducción está vacía')
			return None # tiraba error sino se ingresa ninguna ruta al llamar al programa, ahora te permite abrir 
						#el reproducto sin ingresar ningun directorio con canciones
		return self.canciones[self.actual]

	def cancion_siguiente(self):
		""" Devuelve un objeto de clase Cancion que corresponde a la cancion siguiente en la cola, 
		o None si no hay mas canciones."""
		if self.canciones[self.actual] == self.canciones[-1] or not self.canciones:
			return None
		self.actual += 1
		return self.canciones[self.actual]

	def cancion_anterior(self):
		""" Devuelve un objeto de clase Cancion que corresponde a la cancion anterior en la cola, 
		o None si no hay canciones en la misma o la actual es la primera de la cola."""
		if self.canciones[self.actual] == self.canciones[0] or not self.canciones:
			return None
		self.actual -= 1
		return self.canciones[self.actual]


	def agregar_cancion(self, ruta_cancion):
		""" Agrega una Cancion a la cola a partir de su ruta. Devuelve True si se agrego 
		correctamente, False en caso contrario. Esta accion puede deshacerse y rehacerse."""
		if not os.path.exists(ruta_cancion):
			return False
		if not os.path.splitext(ruta_cancion)[1][1:] in EXTENSIONES_ACEPTADAS: # te devolvia la extension con un punto, ahora se lo quité
			return False
		try:
			self.canciones.append(Cancion(ruta_cancion))
			'''# --------- esto lo tengo que re-ver.----------
			self.historial.apilar(self.canciones.append(Cancion(ruta_cancion)))
			# ---------------------------------------------'''
			return True
		except IOError:
			return False
	
	def remover_cancion(self, ruta_cancion):
		""" Remueve una Cancion de la cola a partir de su ruta. Devuelve True si se removio 
		correctamente, False en caso contrario. Esta accion puede deshacerse y rehacerse."""
		for x in range(len(self.canciones)):
			if self.canciones[x].obtener_ruta() == ruta_cancion:
				self.historial.apilar((Accion(self.canciones.pop(x)), x))
				# ---------re-ver---------------
				return True
		return False

	def deshacer_modificacion(self):
		""" Deshace la ultima accion realizada. Devuelve True si pudo deshacerse, False en caso 
		contrario."""
		try: # Devuelve la cancion en la posicion en la que estaba en la lista
			cancion, pos = self.historial.desapilar()
			if cancion and cancion.tipo == ADICION:
				self.canciones.insert(pos, cancion.cancion)				
				return True
		except TypeError: #pila esta vacia
			return False


	def rehacer_modificacion(self):
		""" Rehace la ultima accion que se deshizo. Devuelve True si pudo rehacerse, False en caso 
		contrario."""

		#incompleto
		se_pudo=False
		try:
			if self.historial.ver_tope().tipo == ADICION:
				for cancion in self.canciones:
					if cancion.ruta in self.historial.ver_tope().cancion.obtener_ruta():
						se_pudo=True
						self.canciones.remove(cancion)
			else:
				ultima_accion=self.historial.ver_tope()
				while ultima_accion.cancion.obtener_ruta() in \
						self.historial.ver_tope().cancion.obtener_ruta():
					self.canciones.append(self.historial.desapilar())
				se_pudo=True
			return se_pudo
		except:
			return False
	def obtener_n_siguientes(self, n_canciones):
		""" Devuelve una lista con las siguientes n canciones. Si en la cola de reproduccion 
		quedan menos canciones que las pedidas, la lista contendra menos elementos que los 
		pedidos."""
		n_siguientes=[]
		if n_canciones > len(self.canciones) - self.actual - 1:
			for x in range(self.actual, len(self.canciones)):
				n_siguientes.append(self.canciones[x])
		else:
			for x in range(self.actual + 1, self.actual + n_canciones + 1):
				n_siguientes.append(self.canciones[x])
		return n_siguientes

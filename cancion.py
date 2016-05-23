from tinytag import TinyTag

class Cancion:
	""" Objeto que almacena informacion de una cancion: su ruta, titulo y artista.
	Obtiene la informacion a partir de los tags del archivo, si los tiene."""

	def __init__(self, ruta, titulo = "Cancion desconocida", artista = "Autor desconocido"):
		# Usar TinyTag para obtener la informacion de la cancion, sobreescribir con lo pasado por 
		# parametro solo si la informacion no se encuentra disponible
		self.info={
			'ruta': ruta,
			'titulo': titulo,
			'artista': artista}
		# averiguar que carajo es tinytag y como se usa
		self.prox=None

	def obtener_ruta(self):
		""" Devuelve la ruta del archivo de la cancion."""
		return self.info['ruta']
	def obtener_titulo(self):
		""" Devuelve el titulo de la cancion."""
		return self.info['titulo']

	def obtener_artista(self):
		""" Devuelve el artista de la cancion."""
		return self.info['artista']
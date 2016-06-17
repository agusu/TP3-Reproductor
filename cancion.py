from tinytag import TinyTag

class Cancion:
	""" Objeto que almacena informacion de una cancion: su ruta, titulo y artista.
	Obtiene la informacion a partir de los tags del archivo, si los tiene."""

	def __init__(self, ruta, titulo = "Cancion desconocida", artista = "Autor desconocido"):
		self.ruta = ruta
		datos = TinyTag.get(ruta)
		self.artista = artista
		self.titulo = titulo
		if datos.title:
			self.titulo = datos.title
		if datos.artist:
			self.artista = datos.artist

	def obtener_ruta(self):
		""" Devuelve la ruta del archivo de la cancion."""
		return self.ruta

	def obtener_titulo(self):
		""" Devuelve el titulo de la cancion."""
		return self.titulo


	def obtener_artista(self):
		""" Devuelve el artista de la cancion."""
		return self.artista

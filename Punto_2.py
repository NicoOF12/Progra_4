

class Pagina:

    def __init__(self, contenido, numero):
        self._contenido = contenido
        self._numero = numero

    def getContenido(self):
        return self._contenido

    def getNumero(self):
        return self._numero

    def setContenido(self, contenido):
        self._contenido = contenido

    def setNumero(self, numero):
        self._mnumero = numero


class Libro:

    def __init__(self, titulo, isbn, autor, añoPublicacion):
        self._titulo = titulo
        self._isbn = isbn
        self._autor = autor
        self._añoPublicacion = añoPublicacion

    def getTitulo(self):
        return self._titulo

    def getIsbn(self):
        return self._isbn

    def getAutor(self):
        return self._autor

    def getAñoPublicacion(self):
        return self._añoPublicacion

    def setTitulo(self, titulo):
        self._titulo = titulo

    def setIsbn(self, isbn):
        self._isbn = isbn

    def setAutor(self, autor):
        self._autor = autor

    def setAñoPublicacion(self, añoPublicacion):
        self._añoPublicacion = añoPublicacion


pagina = Pagina("Obras", 3)

libro = Libro("Conferencias", 23441112-0, "Gabriel", 1973)

print(f'Autor : ', libro.getAutor())

print(f'Isbn : ', libro.getIsbn())

print(f'Contenido : ', pagina.getContenido())

from dis import dis


class Calle:

    def __init__(self, numero, atleta, tiempo):
        self._numero = numero
        self._atleta = atleta
        self._tiempo = tiempo

    def getNumero(self):
        return self._numero

    def getAtleta(self):
        return self._atleta

    def getTiempo(self):
        return self._tiempo

    def setNumero(self, numero):
        self._numero = numero

    def setAtleta(self, atleta):
        self._atleta = atleta

    def setTiempo(self, tiempo):
        self._tiempo = tiempo


class Carrera:

    def __init__(self, distancia, ronda, fecha):
        self._distancia = distancia
        self._ronda = ronda
        self._fecha = fecha

    def getDistancia(self):
        return self._distancia

    def getRonda(self):
        return self._ronda

    def getFecha(self):
        return self._fecha

    def setDistancia(self, distancia):
        self._distancia = distancia

    def setRonda(self, ronda):
        self._ronda = ronda

    def setFecha(self, fecha):
        self._fecha = fecha

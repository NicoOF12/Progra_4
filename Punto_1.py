#Función

class Punto():

    def __init__(self, coord_x, coord_y):
        self._coord_x = coord_x
        self._coord_y = coord_y

    def getX(self):
        return self._coord_x

    def getY(self):
        return self._coord_y

    def setX(self, coord_x):
        self._coord_x = coord_x

    def setY(self, coord_y):
        self._coord_y = coord_y


class CircunferenciaCentrada(Punto):

    def __init__(self, PI, radio, punto):
        self._PI = PI
        self._radio = radio
        self._punto = punto

    def getRadio(self):
        return self._radio

    def getDiametro(self):
        return self._radio * 2

    def getLongitud(self):
        return 2 * self._PI * self._radio

    def getArea(self):
        return self._PI * (self._radio ** 2)

    def getXCentro(self):
        return self._coord_x

    def getYCentro(self):
        return self._coord_y

    def setRadio(self, radio):
        self._radio = radio

    def setDiametro(self):
        self._diametro = self._radio * 2

    def setLongitud(self):
        self._longitud = 2 * self._PI * self._radio

    def setArea(self):
        self._area = self._PI * (self._radio ** 2)

    def setXCentro(self, coord_x):
        self._coord_x = coord_x

    def setYCentro(self, coord_y):
        self._coord_y = coord_y

    def transladarCircunferenciaCentrada(self, coord_x, coord_y):
        self._coord_x = coord_x
        self._coord_y = coord_y


punto = Punto(3, 5)

circunferencia = CircunferenciaCentrada(3.1416, 2, punto)

print(f'centro X : ', punto.getX())
print(f'centro Y : ', punto.getY())

circunferencia.transladarCircunferenciaCentrada(6, 12)

print(f'se transladó a centro X : ', circunferencia.getXCentro())
print(f'se transladó a centro Y : ', circunferencia.getYCentro())

print(f'Longitud : ', circunferencia.getLongitud())

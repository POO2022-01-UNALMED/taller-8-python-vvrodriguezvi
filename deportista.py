class Deportista:

    def __init__(self, year):
        self._deporte = "Futbol"
        self._añosPracticando = year

    def getDeporte(self):
        return self._deporte

    def setDeporte(self, sport):
        self._deporte = sport

    def getAñosPracticando(self):
        return self._añosPracticando

    def setAñosPracticando(self, year):
        self._añosPracticando = year
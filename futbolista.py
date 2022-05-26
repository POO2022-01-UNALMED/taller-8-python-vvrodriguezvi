from persona import Persona
from deportista import Deportista


class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, ap, gm, tr, ph):
        self._golesMarcados = gm
        self._tarjetasRojas = tr
        self._piernaHabil = ph
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, ap)
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self, gmgm):
        self._golesMarcados = gmgm

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setTarjetasRojas(self, trtr):
        self._tarjetasRojas = trtr

    def getPiernaHabil(self):
        return self._piernaHabil

    def setPiernaHabil(self, phph):
        self._piernaHabil = phph

    def __str__(self):
        return f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"
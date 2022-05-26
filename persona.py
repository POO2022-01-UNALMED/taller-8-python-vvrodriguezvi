class Persona():
    #cons.

    def __init__(self, nombre, edad, altura, sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo
    #get y set

    def getNombre(self):
        return self._nombre

    def setNombre(self, n):
        self._nombre = n

    def getEdad(self):
        return self._edad

    def setEdad(self, e):
        self._edad = e

    def getAltura(self):
        return self._altura

    def setEdad(self, a):
        self._edad = a

    def getSexo(self):
        return self._sexo

    def setSexo(self, s):
        self._sexo = s
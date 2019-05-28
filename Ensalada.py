from Fruta import Fruta

class Ensalada(Fruta):
    cantidad = 0

    def __init__(self, nombre, sabor):
        self.nombre = nombre
        self.sabor = sabor

    def preparar(self, cantidad_ensalada):
        ensalada = cantidad_ensalada / self.__TIPOS__[self.sabor][1]
        super(ensalada, self).cortar(ensalada)
        self.cantidad += super(ensalada, self).licuar(ensalada)
        return f'Se realizo {ensalada} cantidad de {self.sabor} sabor'



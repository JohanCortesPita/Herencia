from Fruta import Fruta

class Jugo(Fruta):
    cantidad = 0

    def __init__(self, nombre, sabor):
        self.nombre = nombre
        self.sabor = sabor

    def preparar(self, cantidad_jugo):
        fruta = cantidad_jugo / self.__TIPOS__[self.sabor][1]
        super(Jugo, self).cortar(fruta)
        self.cantidad += super(Jugo, self).licuar(fruta)
        return f'Se realizo el jugo de {cantidad_jugo} cantidad y de sabor {self.sabor}'

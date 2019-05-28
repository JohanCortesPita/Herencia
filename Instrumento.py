class Instrumento:

    def __init__(self, nombreinstrumento, melodias, afinacion, armonia):
        self.nombreinstrumento = nombreinstrumento
        self.armonia = melodias
        self.afinacion = afinacion
        self.melodia = armonia


    def percuxion(self, frecuencia, diametro):
        self.frecuencia = frecuencia
        self.diametro = diametro

        if diametro or frecuencia < 0:
            raise ValueError("No hay diametro ni frecuencias negativas")
        return f'{self.nombreinstrumento} tiene un diametro de {diametro} cm y una frecuencia de vibracion de {frecuencia} Hz'


    def cantidad(self, numero):
        if numero < 0:
            raise ValueError('Deben haber cantidades positivas')
        else:
            return f'{self.nombreinstrumento} cuenta con {numero} ejemplares'

    def cuerdas(self, ncuerdas, afinacion_cuerda):
        self.ncuerdas = ncuerdas
        self.afinacion_cuerda = afinacion_cuerda

        if ncuerdas < 0:
            raise ValueError('No deben haber cuerdas negativas')
        return f'{self.nombreinstrumento} tiene {ncuerdas} cuerdas y estan afinadas en {afinacion_cuerda}'


bateria = Instrumento('Bateria', 'I', 'Flauta', 'F')
guitarra = Instrumento('Guitarra', 'G', 'Piano', 'P')


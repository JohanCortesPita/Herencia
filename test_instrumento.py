from unittest import TestCase
from Instrumento import Instrumento

class TestInstrumento(TestCase):
    def test_percuxion(self):
        dado = Instrumento('Bateria', 'I', 'Flauta', 'F')
        self.assertRaises(ValueError, dado.percuxion, -10, 5)

        dado = Instrumento('Guitarra', 'G', 'Piano', 'P')
        espero = 'La Guitarra tiene un diametro de 40 y una frecuencia de vibracion de 50 Hz'
        resultado = dado.percuxion(40, 25)
        self.assertEqual(espero, resultado)

    def test_cantidad(self):
        dado = Instrumento('Guitarra', 'G', 'Piano', 'P')
        espero = 'La Guitarra cuenta con 5 cuerdas'
        resultado = dado.cantidad(5)
        self.assertEqual(espero, resultado)

        dado = Instrumento('Bateria', 'I', 'Flauta', 'F')
        self.assertRaises(ValueError, dado.cantidad, -10)

    def test_cuerdas(self):
        dado = Instrumento('Bateria', 'I', 'Flauta', 'F')
        self.assertRaises(ValueError, dado.cuerdas, -10, 'DoReMiFaSoLa')

        dado = Instrumento('Guitarra', 'G', 'Piano', 'P')
        espero = 'Tienen 5 cuerdas y estan afinadas correctamente'
        resultado = dado.cuerdas(5, '50Hz')
        self.assertEqual(espero, resultado)
from unittest import TestCase
from Fruta import Fruta
from Jugo import Jugo
from Ensalada import Ensalada


class TestFruta(TestCase):
    def test_pelar(self):
        # Probar con nuevas frutas
        dado = Fruta('banano', 10)
        espero = True
        real = dado.pelar()

        self.assertEqual(real, espero)

        # Probar cuando la fruta ya esta pelada
        self.assertRaises(ValueError, dado.pelar)


    def test_cortar(self):
        dado = Fruta('papaya', 1000)

        # Validar que la fruta este pelada para cortar
        self.assertRaises(ValueError, dado.cortar, 1)

        # Valida si la papaya produce la cantidad esperada
        dado.pelar()
        espero = 130
        real = dado.cortar(1)
        self.assertEqual(espero, real)

        mi_fruta = Fruta('Manzana', 10)
        espero = 'Se validaran los datos ingresados'
        resultado = mi_fruta.cortar(20)
        self.assertEqual(espero, resultado)

    def test_licuar(self):
        dado = Fruta('piña', 1000)

        # Validar que la fruta este pelada para cortar
        self.assertRaises(ValueError, dado.licuar, 1)

        # Valida si la piña produce la cantidad esperada
        dado.pelar()
        espero = 3000
        real = dado.licuar(2)
        self.assertEqual(espero, real)

        mi_fruta = Fruta('Manzana', 10)
        espero = 'Se validaran los dato ingresados'
        resultado = mi_fruta.licuar('AAA')
        self.assertEqual(espero, resultado)

    #Prueba Ensalada
    def test_preparar(self):
        dado = Ensalada('Frutas', 5, 'Manzana Piña Mora', 'mas', 60)
        espero = 'Usted pidio una ensalada de frutas de 5 0z, mas azucar y 60% de Helado'
        real = dado.alistar('Fruas', 5, 'Manzana Piña Mora')

        self.assertEqual(espero, real)

    #Prueba Jugo
    def test_preparar(self):
        dado = Jugo('Mandarina', 10, 'Helado', 'mas', 50)
        espero = 'Ested eligió Mandarina de 10 Oz con Helado, mas azucar y 30 % de agua'
        real = dado.preparar('Mandarina', 10, 'Helado', 'mas', 50)

        self.assertEqual(real, espero)
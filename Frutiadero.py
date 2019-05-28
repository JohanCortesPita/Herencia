from Ensalada import Ensalada
from Jugo import Jugo

class Frutiadero:

     tipo = ''
     inventario = {'Mora': [5, 80], 'Banano': [6, 90], 'Mandarina': [5, 100], 'Mango': [60, 150], 'Piña': [130, 1000]}
     ingredientes = ''

     def __init__(self, pedido, ingredientes):

         self.pedido = pedido
         self.ingredientes = ingredientes

     def preparar(self, pedido, ingredientes):
         if pedido == 'ensalada':
             return Ensalada.alistar(ingredientes)

         elif pedido == 'jugo':
             return Jugo.preparar(ingredientes)

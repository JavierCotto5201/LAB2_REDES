#-----------------------------------#
#|Universidad del Valle de Guatemala|
#|----------------------------------|
#| Redes - Sección 20 - 02/08/2022  |
#|----------------------------------|
#|Integrantes:                      |
#| Jose Abraham Gutierrez Corado    |
#| Walter Danilo Saldaña Salguero   |
#| Javier Alejandro Cotto Argueta   |
#-----------------------------------#

from bitarray import bitarray
import random
from Parity2Dcheck import *

class emisor(object):
    def enviar_cadena(self):
        msj = input("Ingrese mensaje a enviar: ")
        msjM, a = self.enviar_cadena_segura(msj)
        return msjM, a

    def enviar_cadena_segura(self, msj):
        a = bitarray()
        a.frombytes(msj.encode('utf-8'))
        p2d = Parity()
        msjM = p2d.matriz(a)
        a = self.agregar_ruido(a)

    def agregar_ruido(self, a):
        err = 0.5
        prob = round(random.random(), 2)
        #print(prob)

        if prob <= err:
            pos = random.randint(0, len(a))
            if a[pos] == 1:
                a[pos] = 0
            else:
                a[pos] = 1

        return a

    #def enviar_objeto():
        

#llamar = emisor()
#llamar.enviar_cadena()
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
from Parity2Dcheck import Parity


class emisor(object):
    def enviar_cadena(self, msj):
        msjM, a = self.enviar_cadena_segura(msj)
        return msjM, a

    def enviar_cadena_segura(self, msj):
        a = bitarray()
        a.frombytes(msj.encode('utf-8'))
        p2d = Parity()
        msjM = p2d.matriz(a)
        a = self.agregar_ruido(a)
        return msjM, a

    def agregar_ruido(self, a):
        err = 0.1
        prob = round(random.random(), 2)

        if prob <= err:
            pos = random.randint(0, len(a))
            if a[pos] == 1:
                a[pos] = 0
            else:
                a[pos] = 1

        return a
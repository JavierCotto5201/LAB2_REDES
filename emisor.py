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

class emisor(object):
    def enviar_cadena(self):
        msj = input("Ingrese mensaje a enviar: ")
        self.enviar_cadena_segura(msj)

    def enviar_cadena_segura(self, msj):
        a = bitarray()
        a.frombytes(msj.encode('utf-8'))
        self.agregar_ruido(a)

    def agregar_ruido(self, a):
        err = 0.10 
        prob = round(random.random(), 2)

        if prob <= err:
            pos = random.randint(0, len(a) - 1)
            if a[pos] == 1:
                a[pos] = 0
            else:
                a[pos] = 1

    def enviar_objeto():
        print("")

llamar = emisor()
llamar.enviar_cadena_segura("hola")
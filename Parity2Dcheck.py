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
import numpy as np
import random

class Parity():
    def matriz(self, msj):
        cont = 0
        f1 = []
        f2 = []
        for bin in range(0, len(msj)):
            cont += 1
            f1.append(str(msj[bin]))

            if(cont == 8):
                f2.append(''.join(f1))
                f1 = []
                cont = 0

        f3 = self.checkH(f2)
        f4 = self.checkV(f2)
        f4 = self.checkParity(f4)
        f3.append(f4)

        return f3

    def checkH(self, f2):
        cn = 0
        f3 = []
        for f in f2:
            for c in f:
                t = f
                if c == '1':
                    cn += 1
                    
            if cn%2 == 0:
                t += "0"
                cn = 0
            else:
                t += "1"
                cn = 0
            
            f3.append(t)
        #print("Verficación Horizontal: ", f3)
        return f3

    def checkV(self, f2):
        t = ""
        cn = 0
        f4 = []
        for c in range(0, 8):
            for f in range(0, len(f2)):
                t += f2[f][c]  
                if f2[f][c] == '1':
                    cn += 1

            if cn%2 == 0:
                t += "0"
                cn = 0
            else:
                t += "1"
                cn = 0

            f4.append(t[4])
            t = ""
        f4 = ''.join(f4)
        #print("Verificación Vertical: ", f4)
        return f4

    def checkParity(self, f4):
        cn = 0
        for bit in f4:
            if bit == "1":
                cn += 1
            
        if cn%2 == 0:
            f4 = f4 + "0"
        else:
            f4 = f4 + "1"

        return f4

#p2d = Parity()
#p2d.matriz()
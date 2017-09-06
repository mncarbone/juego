from random import randint

class Juego:
    saldo = int()
    cantAciertos = int()
    cantErradas = int()
    maxApuesta = int()
    
    def __init__(self, saldoInicial):
        self.saldo = saldoInicial
        self.cantAciertos = 0
        self.cantErradas = 0
        self.maxApuesta = 0
        
    def apostar(self, apuesta, sombrero):
        self.maxApuesta = apuesta if apuesta > self.maxApuesta else self.maxApuesta
        return self.ganar(apuesta) if self.estaLaMonedaEn(sombrero) else self.perder(apuesta)

    def apostar1(self, apuesta, sombrero):
        if apuesta > self.maxApuesta:
            self.maxApuesta = apuesta
        if self.estaLaMonedaEn(sombrero):
            return self.ganar(apuesta)
        else:
            return self.perder(apuesta)

    def estaLaMonedaEn(self, sombrero):
        return sombrero == self.sombreroConMoneda()

    def sombreroConMoneda(self):
        return randint(1, 3)

    def getSaldo(self):
        return self.saldo

    def perder(self, apuesta):
        self.saldo = self.saldo + apuesta
        self.cantErradas = self.cantErradas + 1
        return 0
        
    def ganar(self, apuesta):
        self.saldo = self.saldo - apuesta
        self.cantAciertos = self.cantAciertos + 1
        return 2 * apuesta

    def getCantAciertos(self):
        return self.cantAciertos
    
    def getCantErradas(self):
        return self.cantErradas
        
    def getMaxApuesta(self):
        return self.maxApuesta

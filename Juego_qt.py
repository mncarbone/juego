from PyQt4.QtGui import QApplication
from PyQt4.uic import loadUi
from juego import *

class JuegoQt(QApplication):
    
    def iniciar(self):
        self.juego = Juego(500)
        self.ui = loadUi('ventana.ui')
        self.asociarEventos()
        self.ui.show()
        self.exec()

    def asociarEventos(self):
        self.ui.btn1.clicked.connect(self.btn1_click)

    def btn1_click(self):
        self.apostarPor(1)
        
    def btn2_click(self):
        self.apostarPor(2)
        
    def btn3_click(self):
        self.apostarPor(3)
        
    def apostarPor(self, unSombrero): 
        apuesta = int(self.ui.textApuesta.text())
        ganancia = self.juego.apostar(apuesta, unSombrero)
        salida = 'Ganó '+str(ganancia) if ganancia > 0 else 'Perdió'
        self.ui.lblSalida.setText(salida)
        
        
        

unJuego = JuegoQt([])
unJuego.iniciar()

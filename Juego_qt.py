from PyQt4.QtGui import QApplication
from PyQt4.uic import loadUi

class JuegoQt(QApplication):
    
    def iniciar(self):
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
        apuesta = self.ui.textApuesta.text()
        print(apuesta)
        

unJuego = JuegoQt([])
unJuego.iniciar()

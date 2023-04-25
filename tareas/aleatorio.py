import sys
import random
from PyQt6.QtWidgets import QMainWindow ,QPushButton, QVBoxLayout,QWidget,QApplication,QLabel
from PyQt6.QtCore import QSize

class Aleatorio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("aleatorio")#nombre de ventana
        self.setFixedSize(QSize(400,200))# modifica el tamaño de la interfaz
        caja=QVBoxLayout()  #interfaz con forma

        self.texto=QLabel("numerito")
        self.boton=QPushButton("numero")


        ventana=QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
        caja.addWidget(self.texto)
        caja.addWidget(self.boton)
        self.boton.clicked.connect(self.numero_aleatorio)

    def numero_aleatorio(self):
        self.texto.setText(f"{random.randint(-1000,1000)}")
if __name__=="__main__":
    app=QApplication(sys.argv)
    ventana=Aleatorio()
    ventana.show()
    app.exec()
import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QWidget,QPushButton,QVBoxLayout,QMainWindow,QLabel,QLineEdit,QApplication
class Letras(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("cantidad de letras")
        self.setFixedSize(QSize(400, 200))
        caja=QVBoxLayout()
        self.texto=QLabel("la palabra tiene: ")
        self.dato=QLineEdit("")
        self.boton=QPushButton("calcular")
        self.boton.clicked.connect(self.algo) #cuando se llama esta cosa se rompe la ventana

        caja.addWidget(self.texto)
        caja.addWidget(self.dato)
        caja.addWidget(self.boton)

        ventana=QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)

    def algo(self,a):                     # no se hacer como funcione esto
        self.texto.setText(len(a))  #setText no sirve con enteros
if __name__=="__main__":
    app=QApplication(sys.argv)
    ventana=Letras()
    ventana.show()
    app.exec()

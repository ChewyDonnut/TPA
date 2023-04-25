#muestra un boton en pantalla
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow ,QPushButton

#una clase que define el diseño y comporamineto de ventana
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atrubbutos y metodos de la clase QMAinWindow
        self.setWindowTitle("aplicacion pyqt6")#nombre de ventana
        self.setFixedSize(QSize(250,150))# modifica el tamaño de la interfaz
        boton=QPushButton("presiona")#esto es el boton
        boton.clicked.connect(self.reaccionar)
        self.clicks=0
        self.setCentralWidget(boton) # esto añade el boton( se usa cuando hay un componente o ¿boton? por que lo deja en el centro y se sobrepone
    #primera forma de manejar eventos
    def reaccionar(self):
        self.clicks += 1
        print("boton presionado")
        print("numero de veces presionado",self.clicks)
if __name__=="__main__":
    app= QApplication(sys.argv)
    ventana=VentanaPrincipal()
    ventana.show() #obligatoria (dentro o fuera del init)
    app.exec()

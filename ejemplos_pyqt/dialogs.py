
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow ,QPushButton,QDialog,QDialogButtonBox,QVBoxLayout,QLabel

class VentanitaCustom(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ventana flotante custom")
        btn=QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel #la barrita es un or
        self.boton=QDialogButtonBox(btn)
        self.boton.accepted.connect(self.accept)
        self.boton.rejected.connect(self.reject)
    
        self.layout=QVBoxLayout()
        mensaje=QLabel("ventanita desplegada")
        self.layout.addWidget(mensaje)
        self.layout.addWidget(self.boton)
        self.setLayout(self.layout)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atrubbutos y metodos de la clase QMAinWindow
        self.setWindowTitle("aplicacion pyqt6")#nombre de ventana
        self.setFixedSize(QSize(250,150))# modifica el tamaño de la interfaz
        boton=QPushButton("presiona")#esto es el boton
        boton.clicked.connect(self.reaccionar)
        self.setCentralWidget(boton) # esto añade el boton( se usa cuando hay un componente o ¿boton? por que lo deja en el centro y se sobrepone
    #primera forma de manejar eventos
    def reaccionar(self):
    #     #dialog simple
    #     ventanita=QDialog(self)
    #     ventanita.setWindowTitle("ventanitaaaa")
    #     ventanita.exec()
        ventanita=VentanitaCustom()
        if ventanita.exec():
            print("siiiiiiiii")
        else:
            print("nooooooo")
if __name__=="__main__":
    app= QApplication(sys.argv)
    ventana=VentanaPrincipal()
    ventana.show() #obligatoria (dentro o fuera del init)
    app.exec()

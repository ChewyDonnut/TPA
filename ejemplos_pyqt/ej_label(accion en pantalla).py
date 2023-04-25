#muestra boton en pantalla y se muestra acciones en interfaz en vez de consola
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow ,QPushButton, QHBoxLayout,QWidget, QLabel

#una clase que define el diseño y comporamineto de ventana
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atrubbutos y metodos de la clase QMAinWindow
        self.contador_clicks=0
        self.setWindowTitle("aplicacion pyqt6")#nombre de ventana
        self.setFixedSize(QSize(250,150))# modifica el tamaño de la interfaz
        caja= QHBoxLayout()  # crea la interfaz rectangular
        self.texto=QLabel("texto de prueba") # texto inicial como un titulo(no el nombre de ventana)


        self.boton1=QPushButton("boton1")
        self.boton1.clicked.connect(self.reaccionar)

                                                           #boton2=QPushButton("boton2")#se crean los dos botones(esto no los integra a la interfaz)
                                                            #boton2.clicked.connect(self.reaccionar)
        caja.addWidget(self.texto)
        caja.addWidget(self.boton1)# integra el boton 1 y 2 a la caja

        ventana=QWidget()#se asigna el layout a la ventana
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
    #primera forma de manejar eventos

    def reaccionar(self):
        self.contador_clicks+=1
        self.texto.setText("cambia en pantalla") # cambia el  mensaje en pantalla
        self.boton1.setText("presionado")

if __name__=="__main__":
    app= QApplication(sys.argv)
    ventana=VentanaPrincipal()
    ventana.show() #obligatoria (dentro o fuera del init)
    app.exec()

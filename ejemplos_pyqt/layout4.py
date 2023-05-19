import sys
from PyQt6.QtWidgets import QApplication, QMainWindow ,QPushButton, QStackedLayout,QWidget,QVBoxLayout,QHBoxLayout,QLabel

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atrubbutos y metodos de la clase QMAinWindow
        self.clicks=0
        self.setWindowTitle("aplicacion pyqt6")#nombre de ventana
        
        self.caja_grandre=QVBoxLayout()        
        self.caja_superior=QHBoxLayout()
        boton1=QPushButton("boton1")
        boton2=QPushButton("boton2")
        boton3=QPushButton("boton 3")
        
        self.cajita= QStackedLayout()
        texto1=QLabel("1")
        texto2=QLabel("2")
        texto3=QLabel("3")
        
   

        self.caja_superior.addWidget(boton1)
        self.caja_superior.addWidget(boton2)
        self.caja_superior.addWidget(boton3)

        self.cajita.addWidget(texto1)
        self.cajita.addWidget(texto2)
        self.cajita.addWidget(texto3)

        self.caja_grandre.addLayout(self.caja_superior)
        self.caja_grandre.addLayout(self.cajita)

        ventana=QWidget()
        ventana.setLayout(self.caja_grandre)
        self.setCentralWidget(ventana)
        
        boton2.clicked.connect(self.dos)
        boton1.clicked.connect(self.uno)
        boton3.clicked.connect(self.tres)


    def uno(self):
        self.cajita.setCurrentIndex(0)
    def dos(self):
        self.cajita.setCurrentIndex(1)
    def tres(self):
        self.cajita.setCurrentIndex(2)
if __name__=="__main__":
    app= QApplication(sys.argv)
    ventana=VentanaPrincipal()
    ventana.show() #obligatoria (dentro o fuera del init)
    app.exec()

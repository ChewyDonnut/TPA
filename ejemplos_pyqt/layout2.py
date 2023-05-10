#muestra dos botones en pantalla
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow ,QPushButton,QGridLayout,QWidget

#una clase que define el diseño y comporamineto de ventana
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atrubbutos y metodos de la clase QMAinWindow
        self.clicks=0
        self.setWindowTitle("aplicacion pyqt6")#nombre de ventana
        self.setFixedSize(QSize(250,150))# modifica el tamaño de la interfaz
        caja=QGridLayout()  # crea la interfaz rectangular

        b00=QPushButton("0,0")
        b01=QPushButton("0,1")
        b02=QPushButton("0,2")
        b10=QPushButton("1,0")
        b11=QPushButton("1,1")
        b12=QPushButton("1,2")
        b20=QPushButton("2,0")  
        b21=QPushButton("2,1")   
        b22=QPushButton("2,2")
        
        # boton2.clicked.connect(self.reaccionar)
        # boton1.clicked.connect(self.reaccionar)
        
        caja.addWidget(b00,0,0)
        caja.addWidget(b01,0,1)
        caja.addWidget(b02,0,2)
        caja.addWidget(b10,1,0)
        caja.addWidget(b11,1,1)
        caja.addWidget(b12,1,2)
        caja.addWidget(b20,2,0)
        caja.addWidget(b21,2,1)
        caja.addWidget(b22,2,2)
        
        ventana=QWidget()#se asigna el layout a la ventana
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
    #primera forma de manejar eventos

    def reaccionar(self):
        self.clicks += 1
        print("boton presionado")
        print("numero de veces presionado",self.clicks) ### se cierra por el self.clicks por alguna razon

if __name__=="__main__":
    app= QApplication(sys.argv)
    ventana=VentanaPrincipal()
    ventana.show() #obligatoria (dentro o fuera del init)
    app.exec()

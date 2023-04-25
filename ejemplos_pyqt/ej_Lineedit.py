#muestra boton en pantalla y se muestra acciones en interfaz en vez de consola
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow ,QPushButton, QVBoxLayout,QWidget, QLabel, QLineEdit

#una clase que define el diseño y comporamineto de ventana
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atrubbutos y metodos de la clase QMAinWindow
        self.setWindowTitle("aplicacion pyqt6")#nombre de ventana
        self.setFixedSize(QSize(400,200))# modifica el tamaño de la interfaz
        caja= QVBoxLayout()  # crea la interfaz rectangular

        self.texto=QLabel("texto de prueba") # texto que queremos que muestre , Es como un titulo, sin contar el nombre de la ventana
        self.entrada=QLineEdit("entrada de texto")# aqui es donde se ingresa el dato solicitado , tambien tiene ese texto que luego se borra
        self.boton1=QPushButton("ingresar")# lo que dice el boton
        self.boton1.clicked.connect(self.reaccionar) #hace la accion de boton

                                                           #boton2=QPushButton("boton2")#se crean los dos botones(esto no los integra a la interfaz)
                                                            #boton2.clicked.connect(self.reaccionar)
        caja.addWidget(self.texto)
        caja.addWidget(self.entrada)
        caja.addWidget(self.boton1)# integra el boton 1 y 2 a la caja
        #estas cajas se van agregando en el mismo orden que aparecen aqui

        ventana=QWidget()#se asigna el layout a la ventana, no termine de enteder
        ventana.setLayout(caja)
        self.setCentralWidget(ventana) #que era esto?
    #primera forma de manejar eventos

    def reaccionar(self):
        self.texto.setText("ingresaste: " + self.entrada.text()) # cambia el  mensaje en pantalla por el de self.entrada
        self.entrada.setText("")
        self.boton1.setText("ingresado")

if __name__=="__main__":
    app= QApplication(sys.argv)
    ventana=VentanaPrincipal()
    ventana.show() #obligatoria (dentro o fuera del init)
    app.exec()

#muestra boton en pantalla y se muestra acciones en interfaz en vez de consola
import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow ,QPushButton, QVBoxLayout,QWidget, QLabel, QLineEdit

#una clase que define el diseño y comporamineto de ventana
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atrubbutos y metodos de la clase QMAinWindow
        self.setWindowTitle("aplicacion pyqt6")#nombre de ventana
        self.setFixedSize(QSize(400,200))# modifica el tamaño de la interfaz
        caja= QVBoxLayout()  # crea la interfaz rectangular

        self.texto=QLabel("ingrese un numero") # texto que queremos que muestre , Es como un titulo, sin contar el nombre de la ventana
        self.entrada=QLineEdit("")# aqui es donde se ingresa el dato solicitado , tambien tiene ese texto que luego se borra
        self.boton1=QPushButton("calcular")# lo que dice el boton
        self.boton1.clicked.connect(self.reaccionar) #hace la accion de boton

                                                           #boton2=QPushButton("boton2")#se crean los dos botones(esto no los integra a la interfaz)
                                                            #boton2.clicked.connect(self.reaccionar)
        caja.addWidget(self.texto)
        caja.addWidget(self.entrada)
        caja.addWidget(self.boton1)# integra el boton 1 y 2 a la caja
        #estas cajas se van agregando en el mismo orden que aparecen aqui

        ventana=QWidget()#se asigna el layout a la ventana, no termine de enteder
        ventana.setLayout(caja)
    #primera forma de manejar eventos

    def reaccionar(self):
        n=int(self.entrada.text())
        self.texto.setText(f"el valor doble de {n} es {(n*2)}:") # cambia el  mensaje en pantalla por el de self.texto
        self.entrada.setText("")
        self.boton1.setText("Resultado")

if __name__=="__main__":
    app= QApplication(sys.argv)
    ventana=VentanaPrincipal()
    ventana.show()   #obligatoria (dentro o fuera del init)
    app.exec()

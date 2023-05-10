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
        
                                                          
        caja.addWidget(self.texto)
       
        #estas cajas se van agregando en el mismo orden que aparecen aqui

        ventana=QWidget()#se asigna el layout a la ventana, no termine de enteder
        ventana.setLayout(caja)
        self.setCentralWidget(ventana) 

    def mouseMoveEvent(self,e):
        self.texto.setText("se mueve el mouse")
        
    def mouseDoubleClickEvent(self,e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.texto.setText("se precionó  doble botón izquierdo")
        if e.button() == Qt.MouseButton.RightButton:
            self.texto.setText("se precionó doble botón Derecho")
        if e.button() == Qt.MouseButton.MiddleButton:
            self.texto.setText("se precionó doble botón Central")
    # def mousePressEvent(self, e):
    #     self.texto.setText("se precionó un botón")
    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.texto.setText("se precionó un botón izquierdo")
        if e.button() == Qt.MouseButton.RightButton:
            self.texto.setText("se precionó un botón Derecho")
        if e.button() == Qt.MouseButton.MiddleButton:
            self.texto.setText("se precionó un botón Central")  
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.texto.setText("se liberó un botón izquierdo")
        if e.button() == Qt.MouseButton.RightButton:
            self.texto.setText("se liberó un botón Derecho")
        if e.button() == Qt.MouseButton.MiddleButton:
            self.texto.setText("se liberó un botón Central")   
    def keyPressEvent(self,e):
        self.texto.setText(f"{e.key()}")
        
        
        

if __name__=="__main__":
    app= QApplication(sys.argv)
    ventana=VentanaPrincipal()
    ventana.show() #obligatoria (dentro o fuera del init)
    app.exec()
   

import sys
from PyQt6.QtWidgets import QWidget,QApplication

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
    def inicializarUI(self):
        self.setGeometry(100,100,500,500) #100,100 posicion y 500,500 es tamaño x,y
        self.setWindowTitle("titulo") #titulo de ventana
        self.show() # linea obligatoria para cargar interfaz
if __name__=="__main__":
    app=QApplication(sys.argv)
    programa1= Ventana()
    sys.exit(app.exec())# termina el desarrollo completo del codigo, no solo la interfaz
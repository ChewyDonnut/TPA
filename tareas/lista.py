import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QWidget,QLabel,QLayout,QPushButton,QLineEdit,QVBoxLayout,QListWidget
class Lista(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("lista")
        caja=QVBoxLayout()

        self.lista=QListWidget()
        self.texto=QLabel("ingrese fruta")
        self.dato=QLineEdit("")
        self.boton=QPushButton("ingresar")
        self.boton.clicked.connect(self.ingresar)

        caja.addWidget(self.lista)
        caja.addWidget(self.texto)
        caja.addWidget(self.dato)
        caja.addWidget(self.boton)
        
        ventana=QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)

    def ingresar(self):
        fruta=self.dato.text()
        self.lista.addItem(fruta)
        self.dato.clear()
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    ventana=Lista()
    ventana.show()
    sys.exit(app.exec())
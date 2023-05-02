import sys
from PyQt6.QtWidgets import QWidget,QApplication,QVBoxLayout,QLabel,QLineEdit,QPushButton,QMainWindow
from PyQt6.QtCore import QSize
class Reves(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("girar")
        self.setFixedSize(400,5000)
        caja=QVBoxLayout()
      
        self.texto=QLabel("ingrese palabra y se da vuelta")
        self.dato=QLineEdit("a")
        self.boton=QPushButton("voltear")
      
        self.boton.clicked.connect(self.girar)    
      
        caja.addWidget(self.texto)
        caja.addWidget(self.dato)
        caja.addWidget(self.boton)
      
        ventana=QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
    
    def girar(self):
        palabra=self.dato.text()
        invertido=" "
        for i in palabra:
            invertido=i + invertido
            self.texto.setText(invertido)


if __name__=="__main__":
    app=QApplication(sys.argv)
    ventana=Reves()
    ventana.show()
    sys.exit(app.exec())
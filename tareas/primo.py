import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QWidget,QApplication,QVBoxLayout,QLabel,QLineEdit,QPushButton
class Primo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("primo o no")
        self.setFixedSize(QSize(400,500))
        caja=QVBoxLayout()
        self.texto=QLabel("ingrese el numero para saber si es primo")
        self.dato=QLineEdit(" ")
        self.boton=QPushButton("verificar")
        self.boton.clicked.connect(self.primito)

        caja.addWidget(self.texto)
        caja.addWidget(self.dato)
        caja.addWidget(self.boton)
        
        ventana=QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)

    def primito(self):
        contador=0
        numero=self.dato.text()
        numero=int(numero) #o  colocar asisgnar el texto antes a numero y pasarlo a int
        if numero>1:
            cont=0
            for i in range(2,numero):
                resto=numero%i
                if resto==0:
                    cont+=1
            if cont>0:
                self.texto.setText("no es primo")
            else :
                    self.texto.setText("es primo")
                    
        else:
            self.texto.setText(f"no es primo")       
if __name__=="__main__":
    app=QApplication(sys.argv)
    ventana=Primo()
    ventana.show()
    app.exec()

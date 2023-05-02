import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QVBoxLayout,QLabel,QPushButton,QLineEdit,QWidget
class Calcular(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("calcular")
        self.setFixedSize(300,300)
        caja=QVBoxLayout()
        self.texto=QLabel("ingrese numero")
        self.dato=QLineEdit("")
        
        self.texto1=QLabel("ingrese numero")
        self.dato1=QLineEdit("")
        
        self.resultado=QLabel("")       

        self.boton=QPushButton("sumar")
        self.boton1=QPushButton("restar")

        self.boton.clicked.connect(self.suma)    
        self.boton1.clicked.connect(self.resta)

        caja.addWidget(self.texto)
        caja.addWidget(self.dato)
        caja.addWidget(self.texto1)
        caja.addWidget(self.dato1)
        caja.addWidget(self.boton)
        caja.addWidget(self.boton1)
        caja.addWidget(self.resultado)

        ventana=QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
    def suma(self):
        numero1=int(self.dato.text())
        numero2=int(self.dato1.text())
        suma=numero1+numero2
        self.resultado.setText(str(suma))
    def resta(self):
        numero1=int(self.dato.text())
        numero2=int(self.dato1.text())
        resta=numero1-numero2
        self.resultado.setText(str(resta))
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    ventana=Calcular()
    ventana.show()
    sys.exit(app.exec())
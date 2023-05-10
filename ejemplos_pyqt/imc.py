import sys
from PyQt6.QtWidgets import QWidget,QApplication,QVBoxLayout,QLabel,QLineEdit,QPushButton,QMainWindow,QGridLayout

class Imc(QMainWindow):
    def __init__(self):
        super().__init__()

        caja=QVBoxLayout()
        grid=QGridLayout()
        self.setWindowTitle("imc")
        #label
        self.titulo=QLabel("IMC")
        self.resultado=QLabel("resultadoaa")
        self.estatura=QLabel("altura en metros")
        self.masa=QLabel("peso")
        #datos
        self.altura=QLineEdit("")
        self.peso=QLineEdit("")
        #boton
        self.boton=QPushButton("calcular")

        self.boton.clicked.connect(self.calcular)
        grid.addWidget(self.masa,0,0)
        grid.addWidget(self.estatura,0,1)
        grid.addWidget(self.peso,1,0)
        grid.addWidget(self.altura,1,1)
        caja.addWidget(self.titulo)
        caja.addLayout(grid)
        caja.addWidget(self.boton)
        caja.addWidget(self.resultado)       

        ventana=QWidget()
        ventana.setLayout(caja)
        ventana.setLayout(grid)
        self.setCentralWidget(ventana)
    def calcular(self):
        altura=float(self.altura.text())
        peso=float(self.peso.text())
        res=peso/(altura**2)
        self.resultado.setText(f"imc es:,{res}")

if __name__=="__main__":
    app= QApplication(sys.argv)
    ventana=Imc()
    ventana.show() #obligatoria (dentro o fuera del init)
    sys.exit(app.exec())
        
        
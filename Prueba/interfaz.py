import sys
from PyQt6.QtWidgets import QWidget,QApplication,QVBoxLayout,QLabel,QLineEdit,QPushButton,QMainWindow,QGridLayout,QHBoxLayout
class Interfaz(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interfaz")
        #se crea lo que intrefa la mayor caja
        caja_grande=QVBoxLayout()
        self.nombre_usuario=QLabel("")
        self.boton=QPushButton("ok")
        
        # se crea lo que integra la segunda caja
        caja_med=QHBoxLayout()

        caja=QVBoxLayout()
        self.imagen=QLabel("imgaen")
        self.descripcion=QLabel("texto de descripcion usuario")
        
        
        valores=QGridLayout()

        self.atributo1=QLineEdit("atributo 1")
        self.atributo2=QLineEdit("atributo 2")
        self.atributo3=QLineEdit("atributo 3")
        self.atributo4=QLineEdit("atributo 4")
        self.atributo5=QLineEdit("atributo 5")
        self.atributo6=QLineEdit("atributo 6")

        self.valor1=QLineEdit("")        
        self.valor2=QLineEdit("")
        self.valor3=QLineEdit("")
        self.valor4=QLineEdit("")
        self.valor5=QLineEdit("")
        self.valor6=QLineEdit("")

        #integramos los datos de atributos y valores
        valores.addWidget(self.atributo1,0,0)
        valores.addWidget(self.atributo2,1,0)
        valores.addWidget(self.atributo3,2,0)
        valores.addWidget(self.atributo4,3,0)
        valores.addWidget(self.atributo5,4,0)
        valores.addWidget(self.atributo6,5,0)
        valores.addWidget(self.valor1,0,1)
        valores.addWidget(self.valor2,1,1)
        valores.addWidget(self.valor3,2,1)
        valores.addWidget(self.valor4,3,1)
        valores.addWidget(self.valor5,4,1)
        valores.addWidget(self.valor6,5,1)
        #agregamos los dos layout a la mediana
        caja.addWidget(self.imagen)
        caja.addWidget(self.descripcion)
        caja_med.addLayout(caja)
        caja_med.addLayout(valores)        

        caja_grande.addWidget(self.nombre_usuario)
        caja_grande.addLayout(caja_med)
        caja_grande.addWidget(self.boton)

        ventana=QWidget()
        ventana.setLayout(caja_grande)
        self.setCentralWidget(ventana)

if __name__=="__main__":
    app= QApplication(sys.argv)
    ventana=Interfaz()
    ventana.show()
    sys.exit(app.exec())








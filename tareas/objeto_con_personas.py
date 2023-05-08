import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout

class Persona():
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("perosnas")
        self.setFixedSize(400,500)
        
        self.nombre=QLabel("nombre")
        self.nombre_dato=QLineEdit("")
        self.apellido=QLabel("apellido")
        self.apellido_dato=QLineEdit("")
        self.boton=QPushButton("ingresar")
        self.boton.clicked.connect(self.agregar)
        self.boton1=QPushButton("mostar lista")
        self.boton1.clicked.connect(self.mostrar)
        caja=QVBoxLayout()
        
        caja.addWidget(self.nombre)
        caja.addWidget(self.nombre_dato)
        caja.addWidget(self.apellido)
        caja.addWidget(self.apellido_dato)
        caja.addWidget(self.boton)
        caja.addWidget(self.boton1)
        ventana=QWidget()
        ventana.setLayout(caja)
        self.setCentralWidget(ventana)
        self.lista_personas=[]

    def agregar(self):
        nombre=self.nombre_dato.text()
        apellido=self.apellido_dato.text()
        persona=Persona(nombre,apellido)
        self.lista_personas.append(persona)
        print(f"se ha agregado a {nombre},{apellido}")
    def mostrar(self):
        for persona in self.lista_personas:
            print(persona.nombre, persona.apellido)
if __name__=="__main__":
    app=QApplication(sys.argv)
    ventana=Ventana()
    ventana.show()
    sys.exit(app.exec())





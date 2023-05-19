import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow ,QPushButton, QStackedLayout,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QGridLayout,QLineEdit

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atrubbutos y metodos de la clase QMAinWindow
        self.clicks=0
        self.setWindowTitle("aplicacion pyqt6")#nombre de ventana
        
        self.caja_grandre=QVBoxLayout()        
        self.caja_superior=QHBoxLayout()
        #parte de arriba
        boton1=QPushButton("iniciar sesion")
        boton2=QPushButton("resgistrarse")
        boton3=QPushButton("¿olvido clave?")
        self.caja_superior.addWidget(boton1)
        self.caja_superior.addWidget(boton2)
        self.caja_superior.addWidget(boton3)
        self.cajita= QStackedLayout()
        boton1.clicked.connect(self.uno)
        boton2.clicked.connect(self.dos)
        boton3.clicked.connect(self.tres)




        #caja inferiror
         #Componentes caja inferior
        # QStackedLayout No tiene el metodo addLayout
        # QStackedLayout -> QWidget -> Layout
        contenedor1 = QWidget()
        ventanita=QVBoxLayout(contenedor1)
        contenedor2 = QWidget()
        ventanita2=QVBoxLayout(contenedor2)
        contenedor3 = QWidget()
        ventanita3=QVBoxLayout(contenedor3)
        
        #ventana 1
        self.sesion=QGridLayout()
        usuraio=QLabel("Usuario:")
        entrada_usuario=QLineEdit("")
        clave=QLabel("Clave")
        entrada_clave=QLineEdit("")
        self.boton=QPushButton("Iniciar")
       
        self.sesion.addWidget(usuraio,0,0)
        self.sesion.addWidget(entrada_usuario,0,1)
        self.sesion.addWidget(clave,1,0)
        self.sesion.addWidget(entrada_clave,1,1)
        self.sesion.addWidget(self.boton,2,1)

        ventanita.addLayout(self.sesion)



        #ventana 2
        self.registro=QGridLayout()

        formulario_registrar = QGridLayout()
        registrar_nombre = QLabel("Nombre")
        self.registrar_entrada_nombre = QLineEdit()
        registrar_apellido = QLabel("Apellido")
        self.registrar_entrada_apellido = QLineEdit()
        registrar_usuario = QLabel("Usuario")
        self.registrar_entrada_usuario = QLineEdit()
        registrar_psw = QLabel("Password")
        self.registrar_entrada_psw = QLineEdit()
        registrar_btn = QPushButton("registrarse ")

        formulario_registrar.addWidget(registrar_nombre, 0,0)
        formulario_registrar.addWidget(self.registrar_entrada_nombre, 0,1)
        formulario_registrar.addWidget(registrar_apellido, 0,2)
        formulario_registrar.addWidget(self.registrar_entrada_apellido, 0,3)
        formulario_registrar.addWidget(registrar_usuario, 1,0)
        formulario_registrar.addWidget(self.registrar_entrada_usuario, 1,1)
        formulario_registrar.addWidget(registrar_psw, 1,2)
        formulario_registrar.addWidget(self.registrar_entrada_psw, 1,3)
        formulario_registrar.addWidget(registrar_btn, 2,3)

        ventanita2.addLayout(formulario_registrar)


        #layout3
        formulario_recuperar = QHBoxLayout()
        recuperar_usuario = QLabel("Usuario")
        recuperar_entrada_usuario = QLineEdit()
        recuperar_btn = QPushButton("recuperar")
        
        formulario_recuperar.addWidget(recuperar_usuario)
        formulario_recuperar.addWidget(recuperar_entrada_usuario)
        
        ventanita3.addLayout(formulario_recuperar)
        ventanita3.addWidget(recuperar_btn)
        
        
        # Configuración para agregar layout en QStackedLayout
        self.cajita.addWidget(contenedor1)
        self.cajita.addWidget(contenedor2)
        self.cajita.addWidget(contenedor3)

        self.caja_grandre.addLayout(self.caja_superior)
        self.caja_grandre.addLayout(self.cajita)

        ventana=QWidget()
        ventana.setLayout(self.caja_grandre)
        self.setCentralWidget(ventana)
        
      


    def uno(self):
        print("Botón 1 clickeado")
        self.cajita.setCurrentIndex(0)
    def dos(self):
        self.cajita.setCurrentIndex(1)
    def tres(self):
        self.cajita.setCurrentIndex(2)
if __name__=="__main__":
    app= QApplication(sys.argv)
    ventana=VentanaPrincipal()
    ventana.show() #obligatoria (dentro o fuera del init)
    app.exec()

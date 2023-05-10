import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget,QVBoxLayout,QGridLayout,QLabel,QLineEdit,QPushButton
class Calculadora(QMainWindow):
    def __init__(self, ):
        super().__init__()
        self.setWindowTitle("calculadora")
        self.datos=QLabel("")
        self.dato=QLabel("")
        caja=QVBoxLayout()
        num=QGridLayout()
        
        self.dato1=None
        self.dato2=None


        self.uno=QPushButton("1")            
        self.texto=QPushButton("")
        self.dos=QPushButton("2")
        self.tres=QPushButton("3")
        self.cuatro=QPushButton("4")
        self.cinco=QPushButton("5")
        self.seis=QPushButton("6")
        self.siete=QPushButton("7")
        self.ocho=QPushButton("8")
        self.nueve=QPushButton("9")
        self.cero=QPushButton("0")        
        self.suma=QPushButton("+")
        self.resta=QPushButton("-")
        self.mult=QPushButton("*")
        self.div=QPushButton("/")
        self.resultado=QPushButton("=") 
        self.c=QPushButton("c")    
        #agregar grid
        num.addWidget(self.uno,2,0)        
        num.addWidget(self.dos,2,1)                
        num.addWidget(self.tres,2,2)     
        num.addWidget(self.cuatro,1,0)        
        num.addWidget(self.cinco,1,1)        
        num.addWidget(self.seis,1,2)        
        num.addWidget(self.siete,0,0)        
        num.addWidget(self.ocho,0,1)        
        num.addWidget(self.nueve,0,2)        
        num.addWidget(self.cero,3,1)
        num.addWidget(self.div,0,3)
        num.addWidget(self.mult,1,3)
        num.addWidget(self.resta,2,3)
        num.addWidget(self.suma,3,3)
        num.addWidget(self.resultado,3,2)
        num.addWidget(self.c,3,0)
        #datos de toda la ventana
        caja.addWidget(self.dato)
        caja.addWidget(self.datos)
        caja.addLayout(num)

        ventana=QWidget()
        ventana.setLayout(caja)
        ventana.setLayout(num)
        self.setCentralWidget(ventana)

        self.uno.clicked.connect(self.one)
        self.dos.clicked.connect(self.two)       
        self.tres.clicked.connect(self.three)
        self.cuatro.clicked.connect(self.four)
        self.cinco.clicked.connect(self.five)
        self.seis.clicked.connect(self.six)
        self.siete.clicked.connect(self.seven)
        self.ocho.clicked.connect(self.eight)
        self.nueve.clicked.connect(self.nine)
        self.cero.clicked.connect(self.cer) 
        self.suma.clicked.connect(self.sum)      
        self.mult.clicked.connect(self.multi)
        self.resta.clicked.connect(self.rest)
        self.div.clicked.connect(self.divi)
        self.resultado.clicked.connect(self.result)
        self.c.clicked.connect(self.clear)
    def one(self):
        texto=self.datos.text()
        self.datos.setText(texto + "1")
    def two(self):
        texto=self.datos.text()
        self.datos.setText(texto + "2")
    def three(self):
        texto=self.datos.text()
        self.datos.setText(texto + "3")
    def four(self):
        texto=self.datos.text()
        self.datos.setText(texto + "4")
    def five(self):
        texto=self.datos.text()
        self.datos.setText(texto + "5")
    def six(self):
        texto=self.datos.text()
        self.datos.setText(texto + "6")
    def seven(self):
        texto=self.datos.text()
        self.datos.setText(texto + "7")
    def eight(self):
        texto=self.datos.text()
        self.datos.setText(texto + "8")
    def nine(self):
        texto=self.datos.text()
        self.datos.setText(texto + "9")
    def cer(self):
        texto=self.datos.text()
        self.datos.setText(texto + "0")    
    def multi(self):
        self.dato1=int(self.datos.text())
        self.dato.setText(f"{self.dato1} *")
        self.datos.clear()
        
    def divi(self):
        self.dato1=int(self.datos.text())
        self.dato.setText(f"{self.dato1} /")
        self.datos.clear()        
    def sum(self):
        self.dato1=int(self.datos.text())
        self.dato.setText(f"{self.dato1} +")
        self.datos.clear()
        
    def rest(self):
        self.dato1=int(self.datos.text())
        self.dato.setText(f"{self.dato1} -")
        self.datos.clear()
        
    def result(self):
        self.dato2 = int(self.datos.text())
        dato=self.dato.text()
        if dato[-1]=="+":
            self.dato2=int(self.datos.text())
            self.datos.setText(f"{self.dato1+self.dato2}")
            self.dato.clear()
        elif dato[-1]=="-":
            self.dato2=int(self.datos.text())
            self.datos.setText(f"{self.dato1-self.dato2}")
           
            self.dato.clear()
        elif dato[-1]=="*":
            self.dato2=int(self.datos.text())
            self.datos.setText(f"{self.dato1*self.dato2}")
            self.dato.clear()
        elif dato[-1]=="/":
            self.dato2=int(self.datos.text())
            if self.dato2!=0:
                self.datos.setText(f"{self.dato1/self.dato2}")               
                self.dato.clear()
            else:
                self.datos.setText("indeterminado")  
                self.dato.clear()  
    def clear(self):
        self.dato1 = None
        self.dato2 = None
        self.dato.clear()
        self.datos.clear()

if __name__=="__main__":
    app=QApplication(sys.argv)
    ventana=Calculadora()
    ventana.show()
    sys.exit(app.exec())

import sys
from PyQt6.QtWidgets import QWidget,QApplication,QVBoxLayout,QLabel,QLineEdit,QPushButton,QMainWindow,QGridLayout,QHBoxLayout

class Mascota:
    def __init__(self,nombre,especie,edad,peso):
        self.nombre=nombre
        self.especie=especie
        self.edad=edad
        self.peso=peso
        
    def __str__(self) -> str:
        return f"Mascota {self.nombre} de {self.edad} anios de la especie {self.especie} con {self.peso} Kg."

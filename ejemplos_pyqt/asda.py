import sys
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QPushButton
from random import randrange

class RandomNumber(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Generador de Números Aleatorios')
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel(self)
        self.label.setText("Presione el botón para generar un número aleatorio")

        self.button = QPushButton('Generar número', self)
        self.button.clicked.connect(self.show_random_number)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.button)

        self.setLayout(vbox)

    def show_random_number(self):
        number = randrange(10**10)  # Generar cualquier número aleatorio sin restricciones de rango
        self.label.setText(f"El número generado es: {number}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RandomNumber()
    window.show()
    sys.exit(app.exec())

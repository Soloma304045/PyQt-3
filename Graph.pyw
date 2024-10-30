import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QDialog
from PyQt6.QtGui import QPixmap, QIcon

class GraphWindow(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle("Вычисление значения функции")
        self.setGeometry(100, 100, 400, 400)
        self.setWindowIcon(QIcon("Images/logo.png"))

        self.inputX = QLineEdit(self)
        self.inputX.setPlaceholderText("Введите значение X")
        
        self.outputY = QLabel("Значение Y:", self)

        solveButton = QPushButton("Решить", self)
        solveButton.clicked.connect(self.solveFunction)

        clearButton = QPushButton("Очистить", self)
        clearButton.clicked.connect(self.clearFields)

        exitButton = QPushButton("Выход", self)
        exitButton.clicked.connect(self.close)

        self.graph = QLabel(self)
        pixmap = QPixmap("Images/graph.webp")
        self.graph.setPixmap(pixmap)
        self.graph.setScaledContents(True)
        self.graph.setFixedSize(400, 150)

        layout = QVBoxLayout()
        layout.addWidget(self.graph)

        inputLayout = QHBoxLayout()
        inputLayout.addWidget(QLabel("X:"))
        inputLayout.addWidget(self.inputX)
        layout.addLayout(inputLayout)

        layout.addWidget(self.outputY)

        button_layout = QHBoxLayout()
        button_layout.addWidget(solveButton)
        button_layout.addWidget(clearButton)
        button_layout.addWidget(exitButton)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def solveFunction(self):
        try:
            x = float(self.inputX.text())
            y = self.calculate_y(x)
            self.outputY.setText(f"Значение Y: {y:.2f}")
        except ValueError:
            self.outputY.setText("Ошибка: введите число для X")

    def clearFields(self):
        self.inputX.clear()
        self.outputY.setText("Значение Y:")

    def calculate_y(self, x):
        if -9 <= x <= -5:
            y = np.cos(45 * (x+9))*2
        elif -5 < x <= -4:
            y = 2
        elif -4 < x <= 0:
            y = 0 + x * -0.5
        elif 0 < x <= np.pi:
            y = np.cos(x) + 1
        elif np.pi < x <= 5:
            y = np.tan(np.radians(45)) * (x - np.pi)
        else:
            y = 0
        return y

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GraphWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import (
    QApplication, QPushButton, QLabel, QLineEdit, 
    QVBoxLayout, QDialog, QMessageBox, QHBoxLayout, 
)

class InputWindow(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        self.setWindowTitle("Установка точки в графике")
        self.setGeometry(200, 200, 300, 200)
        self.setWindowIcon(QIcon("Images/logo.png"))

        self.graph = QLabel(self)
        pixmap = QPixmap("Images/graph2.webp")
        self.graph.setPixmap(pixmap)
        self.graph.setScaledContents(True)
        self.graph.setFixedSize(300, 150)

        self.labelX = QLabel("Введите X:")
        self.inputX = QLineEdit()

        self.labelY = QLabel("Введите Y:")
        self.inputY = QLineEdit()

        self.labelR = QLabel("Введите R:")
        self.inputR = QLineEdit()

        self.detButton = QPushButton("Определить")
        self.detButton.clicked.connect(self.detPoint)

        self.clearButton = QPushButton("Очистить")
        self.clearButton.clicked.connect(self.clearFields)

        self.exitButton = QPushButton("Выход")
        self.exitButton.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.graph)
        layout.addWidget(self.labelX)
        layout.addWidget(self.inputX)
        layout.addWidget(self.labelY)
        layout.addWidget(self.inputY)
        layout.addWidget(self.labelR)
        layout.addWidget(self.inputR)
        
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.detButton)
        buttonLayout.addWidget(self.clearButton)
        buttonLayout.addWidget(self.exitButton)
        
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

    def detPoint(self):
        try:
            x = float(self.inputX.text())
            y = float(self.inputY.text())
            r = float(self.inputR.text())

            if (x >= 0 and y >= 0 and x**2 + y**2 <= r**2) or \
                (x <= 0 and y <= 0 and x**2 + y**2 <= r**2):
                QMessageBox.information(self, "Результат", "Точка находится в серой области.")
            else:
                QMessageBox.information(self, "Результат", "Точка не находится в серой области.")
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите корректные значения для X, Y и R.")

    def clearFields(self):
        self.inputX.clear()
        self.inputY.clear()
        self.inputR.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = InputWindow()
    mainWindow.show()
    sys.exit(app.exec())

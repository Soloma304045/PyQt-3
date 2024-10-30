import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon, QGuiApplication
from PyQt6.QtCore import Qt
from Question import SurveyWindow # type: ignore
from Graph import GraphWindow # type: ignore
from DotGraph import InputWindow # type: ignore

class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setWindowTitle("Чайдаков Иван ИТД-21")
        self.setWindowIcon(QIcon("Images/Pepe.jpg"))

        screen = QGuiApplication.primaryScreen()
        siz = screen.size()
        window_width, window_height = 300, 200
        self.setGeometry(
            (siz.width() - window_width) // 2,
            (siz.height() - window_height) // 2,
            window_width,
            window_height
        )

        label = QLabel('''
            <center>
                <h1>Лабораторная работа №3</h1><br>
                <b>Основные компоненты. Размещение</b><br>
                <b>компонентов в окнах</b><br>
                Выполнил студент группы <span style="color: red;">ИТД-21
                <h2>Чайдаков Иван Миронович</h2></span>
            </center>
        ''')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button1 = QPushButton("Анкета", self)
        button1.setToolTip("Анкета с опросом насколько вы кот")
        button1.clicked.connect(self.openSurvey) 

        button2 = QPushButton("Значения графика", self)
        button2.setToolTip("Проверка значения Y на плоском графике")
        button2.clicked.connect(self.openGraph)

        button3 = QPushButton("Установка точки в графике", self)
        button3.setToolTip("Проверка попадания точки в закрашенную область на графике")
        button3.clicked.connect(self.openDotGraph)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        self.setLayout(layout)

    def openSurvey(self):
        self.surveyWindow = SurveyWindow(self)
        self.surveyWindow.show()

    def openGraph(self):
        self.graphWindow = GraphWindow(self)
        self.graphWindow.show()

    def openDotGraph(self):
        self.inputWindow = InputWindow(self)
        self.inputWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

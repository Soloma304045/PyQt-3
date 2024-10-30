import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QDialog, QDial
from PyQt6.QtGui import QIcon

class SurveyWindow(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle("Анкета")

        layout = QGridLayout()
        self.setWindowIcon(QIcon("Images/logo.png"))

        question_label = QLabel("Насколько процентов вы кот?")
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(50)
        self.dial.setNotchesVisible(True)

        submitButton = QPushButton("Отправить")
        submitButton.clicked.connect(self.submitResponse)

        layout.addWidget(question_label, 0, 0, 1, 2)
        layout.addWidget(self.dial, 1, 0, 1, 2)
        layout.addWidget(submitButton, 2, 0, 1, 2)

        self.setLayout(layout)

    def submitResponse(self):
        response_value = self.dial.value()
        print("Ответ пользователя:", response_value)
        self.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SurveyWindow()
    window.show()
    sys.exit(app.exec())

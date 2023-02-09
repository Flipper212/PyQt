from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys #system


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__() # 1 - цей клас 2 - self
        self.setWindowTitle("Program PyQt")
        self.setGeometry(300, 250, 800, 500)  # 1,2 - віддалення(x, y)    3,4 - розмір

        self.text = QtWidgets.QLabel(self)  # До якого вікна відноситься (window)
        '''
        QLabel - текст
        QPlainTextEdit - поле вводу
        QPushButton - кнопка
        '''
        self.text.setText("Hello World")  # задати текст
        self.text.move(100, 100)
        self.text.adjustSize()  # фіксить відстань

        self.button = QtWidgets.QPushButton(self)
        self.button.move(70, 150)
        self.button.setText("Tap")
        self.button.setFixedWidth(200)  # фіксований розмір
        self.button.clicked.connect(self.tap_button)

    def tap_button(self):
        self.setStyleSheet('background-color: grey;')
        self.text.setText("Hello All")
        self.text.adjustSize()

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()

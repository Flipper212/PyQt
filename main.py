from PyQt5 import QtCore, QtGui, QtWidgets
from sys import argv, exit
from math import pi, sqrt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(351, 342)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.operator_function = False # Чи виклик оператора
        self.index = None # Знак
        self.first_number = None # Перше число
        self.second_number = None # Друге число

        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 351, 60))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.label_result.setStyleSheet(
            "qproperty-alignment: AlignRight; border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174);"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(0, 60, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")
        self.button_1.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(140, 60, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_3.setFont(font)
        self.button_3.setObjectName("button_3")
        self.button_3.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(70, 60, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.button_2.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(140, 130, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_6.setFont(font)
        self.button_6.setObjectName("button_6")
        self.button_6.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(0, 130, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_4.setFont(font)
        self.button_4.setObjectName("button_4")
        self.button_4.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(70, 130, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_5.setFont(font)
        self.button_5.setObjectName("button_5")
        self.button_5.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(140, 200, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_9.setFont(font)
        self.button_9.setObjectName("button_9")
        self.button_9.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(0, 200, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_7.setFont(font)
        self.button_7.setObjectName("button_7")
        self.button_7.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(70, 200, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_8.setFont(font)
        self.button_8.setObjectName("button_8")
        self.button_8.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(0, 270, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_0.setFont(font)
        self.button_0.setObjectName("button_0")
        self.button_0.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_equal = QtWidgets.QPushButton(self.centralwidget)
        self.button_equal.setGeometry(QtCore.QRect(140, 270, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_equal.setFont(font)
        self.button_equal.setObjectName("button_equal")
        self.button_equal.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_plus = QtWidgets.QPushButton(self.centralwidget)
        self.button_plus.setGeometry(QtCore.QRect(210, 60, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_plus.setFont(font)
        self.button_plus.setStyleSheet("")
        self.button_plus.setObjectName("button_plus")
        self.button_plus.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_division = QtWidgets.QPushButton(self.centralwidget)
        self.button_division.setGeometry(QtCore.QRect(210, 270, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_division.setFont(font)
        self.button_division.setObjectName("button_division")
        self.button_division.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_multiplication = QtWidgets.QPushButton(self.centralwidget)
        self.button_multiplication.setGeometry(QtCore.QRect(210, 200, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_multiplication.setFont(font)
        self.button_multiplication.setObjectName("button_multiplication")
        self.button_multiplication.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_minus = QtWidgets.QPushButton(self.centralwidget)
        self.button_minus.setGeometry(QtCore.QRect(210, 130, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_minus.setFont(font)
        self.button_minus.setObjectName("button_minus")
        self.button_minus.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_erase = QtWidgets.QPushButton(self.centralwidget)
        self.button_erase.setGeometry(QtCore.QRect(280, 60, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_erase.setFont(font)
        self.button_erase.setStyleSheet("")
        self.button_erase.setObjectName("button_erase")
        self.button_erase.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_pi = QtWidgets.QPushButton(self.centralwidget)
        self.button_pi.setGeometry(QtCore.QRect(280, 200, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_pi.setFont(font)
        self.button_pi.setObjectName("button_pi")
        self.button_pi.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.button_sqrt.setGeometry(QtCore.QRect(280, 270, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_sqrt.setFont(font)
        self.button_sqrt.setObjectName("button_sqrt")
        self.button_sqrt.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_coma = QtWidgets.QPushButton(self.centralwidget)
        self.button_coma.setGeometry(QtCore.QRect(280, 130, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_coma.setFont(font)
        self.button_coma.setObjectName("button_coma")
        self.button_coma.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        self.button_ce = QtWidgets.QPushButton(self.centralwidget)
        self.button_ce.setGeometry(QtCore.QRect(70, 270, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_ce.setFont(font)
        self.button_ce.setObjectName("button_ce")
        self.button_ce.setStyleSheet(
            "border-radius: 2px; border: 1px solid; border-color: rgba(143, 150, 185, 174); "
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(143, 150, 185, 174), stop:1 rgba(255, 255, 255, 255));")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_equal.setText(_translate("MainWindow", "="))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_division.setText(_translate("MainWindow", "/"))
        self.button_multiplication.setText(_translate("MainWindow", "x"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_erase.setText(_translate("MainWindow", "⇦"))
        self.button_pi.setText(_translate("MainWindow", "π"))
        self.button_sqrt.setText(_translate("MainWindow", "√"))
        self.button_coma.setText(_translate("MainWindow", ","))
        self.button_ce.setText(_translate("MainWindow", "CE"))

    def add_function(self):
        self.button_0.clicked.connect(lambda: self.write_number(self.button_0.text()))
        self.button_1.clicked.connect(lambda: self.write_number(self.button_1.text()))
        self.button_2.clicked.connect(lambda: self.write_number(self.button_2.text()))
        self.button_3.clicked.connect(lambda: self.write_number(self.button_3.text()))
        self.button_4.clicked.connect(lambda: self.write_number(self.button_4.text()))
        self.button_5.clicked.connect(lambda: self.write_number(self.button_5.text()))
        self.button_6.clicked.connect(lambda: self.write_number(self.button_6.text()))
        self.button_7.clicked.connect(lambda: self.write_number(self.button_7.text()))
        self.button_8.clicked.connect(lambda: self.write_number(self.button_8.text()))
        self.button_9.clicked.connect(lambda: self.write_number(self.button_9.text()))
        self.button_erase.clicked.connect(lambda: self.erase_number())
        self.button_plus.clicked.connect(lambda: self.operators("+"))
        self.button_minus.clicked.connect(lambda: self.operators("-"))
        self.button_multiplication.clicked.connect(lambda: self.operators("x"))
        self.button_division.clicked.connect(lambda: self.operators("/"))
        self.button_equal.clicked.connect(lambda: self.equal(self.label_result.text()))
        self.button_pi.clicked.connect(lambda: self.write_number(str(pi)[:10]))
        self.button_sqrt.clicked.connect(lambda: self.sqrt(self.label_result.text()))
        self.button_coma.clicked.connect(lambda: self.write_number("."))
        self.button_ce.clicked.connect(lambda: self.ce())


    def operators(self, op): # Функція при виклику опепратора (+, -, *, /)
        self.first_number = float(self.label_result.text())
        self.index = op
        self.operator_function = True

    def equal(self, second_number): # Функція при виклику дорівнює
        self.second_number = float(self.label_result.text())
        self.counter()

    def sqrt(self, number):
        if len(str(sqrt(float(number)))) >= 13:
            if int(sqrt(float(number))) == sqrt(float(number)):
                self.label_result.setText(str(int(sqrt(float(number))))[:13] + "e")
            else:
                self.label_result.setText(str(sqrt(float(number)))[:13] + "e")
        else:
            if int(sqrt(float(number))) == sqrt(float(number)):
                self.label_result.setText(str(int(sqrt(float(number)))))
            else:
                self.label_result.setText(str(sqrt(float(number))))


    def ce(self):
        self.label_result.setText("0")
        self.operator_function = False
        self.index = None
        self.first_number = None
        self.second_number = None

    def write_number(self, number): # Написати число
        if len(self.label_result.text())<= 12:
            if self.operator_function == True:
                self.label_result.setText(number)
                self.operator_function = False
            elif self.label_result.text() == "0" and number == ".":
                self.label_result.setText("0" + number)
            elif self.label_result.text() == "0":
                self.label_result.setText(number)
            else: self.label_result.setText(self.label_result.text() + number)

    def erase_number(self): # Видалити число
        if len(self.label_result.text()) == 1 or self.label_result.text() == "division by 0":
            self.label_result.setText("0")
        else: self.label_result.setText(self.label_result.text()[:-1])


    def counter(self): # Загальний підрахунок, вивід результату
        first = self.first_number
        second = self.second_number
        try:
            if self.index == "+":
                if int(first + second) == first + second:
                    if len(str(first + second)) >= 13:
                        self.label_result.setText(str(int(first + second))[:13] + "e")
                    else:
                        self.label_result.setText(str(int(first + second)))
                else:
                    if len(str(first + second)) >= 13:
                        self.label_result.setText(str(first + second)[:13] + "e")
                    else:
                        self.label_result.setText(str(first + second))
            elif self.index == "-":
                if int(first - second) == first - second:
                    if len(str(first - second)) >= 13:
                        self.label_result.setText(str(int(first - second))[:13] + "e")
                    else:
                        self.label_result.setText(str(int(first - second)))
                else:
                    if len(str(first - second)) >= 13:
                        self.label_result.setText(str(first - second)[:13] + "e")
                    else:
                        self.label_result.setText(str(first - second))

            elif self.index == "x":
                if int(first * second) == first * second:
                    if len(str(first * second)) >= 13:
                        self.label_result.setText(str(int(first * second))[:13] + "e")
                    else:
                        self.label_result.setText(str(int(first * second)))
                else:
                    if len(str(first * second)) >= 13:
                        self.label_result.setText(str(first * second)[:13] + "e")
                    else:
                        self.label_result.setText(str(first * second))


            elif self.index == "/":
                if int(first / second) == first / second:
                    if len(str(first / second)) >= 13:
                        self.label_result.setText(str(int(first / second))[:13] + "e")
                    else: self.label_result.setText(str(int(first / second)))
                else:
                    if len(str(first / second)) >= 13:
                        self.label_result.setText(str(first / second)[:13] + "e")
                    else: self.label_result.setText(str(first / second))


        except ZeroDivisionError:
            self.label_result.setText("division by 0")
        finally:
            self.operator_function = False
            self.index = None
            self.first_number = None
            self.second_number = None


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    exit(app.exec_())

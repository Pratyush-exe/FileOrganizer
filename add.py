from PyQt5 import QtCore, QtGui, QtWidgets
import csv
from PyQt5.QtWidgets import QMessageBox


class Ui_add(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 262)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(-60, -60, 1181, 611))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("img_data/werwer.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 60, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 120, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 163, 161, 31))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img_data/ertert.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 27, 191, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img_data/sdfds.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 180, 371, 51))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.data_adding)
        self.pushButton.clicked.connect(MainWindow.close)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def data_adding(self):
        self.text1 = self.textEdit.toPlainText()
        self.text2 = self.textEdit_2.toPlainText()

        items = []

        with open(r"database\data.csv", 'r') as sd:
            reader = csv.reader(sd)
            for row in reader:
                items.append(row[0])

        if self.text1 not in items:
            infile = open(r"database\data.csv", 'a', newline='')
            writer = csv.writer(infile)
            writer.writerow([self.text1, self.text2])

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("'" + self.text1 + "'" + " Folder name is already taken")
            msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "CONFIRM"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_add()
    ui.setupUi(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon(r"img_data/icon.png"))
    MainWindow.setWindowTitle("Organizer")
    MainWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import csv
import os
import shutil
from add import Ui_add


class Ui_custom(object):

    def __init__(self, path):
        self.path = path

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(543, 550)
        MainWindow.setWindowTitle("Custom Setting")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 450, 281, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 460, 221, 81))
        self.pushButton_3.setObjectName("pushButton_3")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 341, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img_data/xdasd.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(-130, 0, 1181, 611))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("img_data/werwer.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 400, 521, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.radioButton_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.radioButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 120, 521, 192))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 104, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 167, 167, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)

        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 104, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 167, 167, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)

        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 167, 167, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)

        self.listWidget.setPalette(palette)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setObjectName("listWidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 399, 521, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 330, 521, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 58, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 58, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 58, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 58, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frame_2.setPalette(palette)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")

        self.checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox.setGeometry(QtCore.QRect(12, 17, 111, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.checkBox.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.label_6.raise_()
        self.verticalLayoutWidget.raise_()
        self.pushButton_3.raise_()
        self.label.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.listWidget.raise_()
        self.frame_2.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.refresh = QtWidgets.QPushButton(self.frame_2)
        self.refresh.setGeometry(QtCore.QRect(480, 10, 30, 30))
        self.refresh.raise_()

        self.pushButton.clicked.connect(self.add)
        self.radioButton_2.setChecked(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.refresh.clicked.connect(self.update)
        self.pushButton_2.clicked.connect(self.remove)
        self.pushButton_3.clicked.connect(self.confirm)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ADD"))
        self.pushButton_2.setText(_translate("MainWindow", "REMOVE"))
        self.pushButton_3.setText(_translate("MainWindow", "CONFIRM"))
        self.radioButton_2.setText(_translate("MainWindow", "Oragnize by extension"))
        self.radioButton.setText(_translate("MainWindow", "Oragnize by name"))
        self.checkBox.setText(_translate("MainWindow", "Burst Folders"))
        self.refresh.setText(_translate("MainWindow", "R"))

        f = open(r"database\data.csv", 'w')
        f.truncate()
        f.close()

    def add(self):
        self.Mainwindow = QtWidgets.QMainWindow()
        self.ui = Ui_add()
        self.ui.setupUi(self.Mainwindow)
        self.Mainwindow.show()

    def update(self):

        self.listWidget.clear()

        with open(r"database\data.csv", 'r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                self.listWidget.addItem(row[0] + " > " + row[1])

        self.listWidget.update()

    def remove(self):
        rem = self.listWidget.currentRow()
        x = self.listWidget.takeItem(rem)
        x = x.text()
        x = x.split(">")
        items = []
        for index in range(self.listWidget.count()):
            items.append(self.listWidget.item(index).text())
            print(items[index])
        with open(r"database\data.csv", 'w', newline='') as infile:
            writer = csv.writer(infile)
            for item in items:
                a = item.split(">")
                writer.writerow(a)
        self.listWidget.update()
        infile.close()

    def confirm(self):
        global org
        Burst = "- 'Burst Folder' Will not be done"
        if self.checkBox.isChecked():
            Burst = "- 'Burst Folder' Will be done"
        if self.radioButton.isChecked():
            org = "- To be Organized by Name "
        elif self.radioButton_2.isChecked():
            org = "- To be Organized by Extenstion "
        msg = QMessageBox()
        msg.setWindowTitle("Confirm")
        msg.setIcon(QMessageBox.Warning)
        msg.setText(Burst + "\n" + org)
        msg.addButton(QtWidgets.QMessageBox.YesToAll)
        msg.addButton(QtWidgets.QMessageBox.Abort)
        opt = msg.exec_()
        if opt == QtWidgets.QMessageBox.YesToAll:
            self.Organize()
            msg = QMessageBox()
            msg.setWindowTitle("Done")
            msg.setIcon(QMessageBox.Information)
            msg.setText("Folders Sorted")
            msg.addButton(QtWidgets.QMessageBox.Ok)
            msg.exec_()

    def Organize(self):

        # Bursting Folder
        if self.checkBox.isChecked():
            for root, dir, files in os.walk(self.path):
                for file in files:
                    old = root + "\\" + file
                    new = self.path + "\\" + file
                    os.rename(old, new)

            for root, dirs, files in os.walk(self.path):
                for dir in dirs:
                    loc = self.path + "\\" + dir
                    shutil.rmtree(loc)

        # Making Folders
        with open(r"database\data.csv", 'r') as sd:
            reader = csv.reader(sd)
            for row in reader:
                os.mkdir(self.path + "\\" + row[0])

        # Filling Files
        with open(r"database\data.csv", 'r') as sd:
            reader = csv.reader(sd)
            for row in reader:
                x = row[1].split(",")
                for extnam in x:
                    # For Names-Sort
                    if self.radioButton.isChecked():
                        for root, dir, files in os.walk(self.path):
                            if root is self.path:
                                for file in files:
                                    nam = file.split(".")
                                    del nam[-1]
                                    if extnam in nam:
                                        old = self.path + "\\" + file
                                        new = self.path + "\\" + row[0] + "\\" + file
                                        os.rename(old, new)
                    # For Extension-Sort
                    elif self.radioButton_2.isChecked():
                        for root, dir, files in os.walk(self.path):
                            if root is self.path:
                                for file in files:
                                    if extnam in file.split(".")[-1]:
                                        old = self.path + "\\" + file
                                        new = self.path + "\\" + row[0] + "\\" + file
                                        os.rename(old, new)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_custom()
    ui.setupUi(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon(r"img_data/icon.png"))
    MainWindow.setWindowTitle("Organizer")
    MainWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from custom import Ui_custom
import os
import shutil
import webbrowser


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.website = "https://github.com/Pratyush-exe"
        self.path = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(544, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 100, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(411, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 220, 501, 101))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setText("")
        self.label.setObjectName("label")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 149, 501, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(27, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.radioButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color = rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
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
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 350, 501, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(136, 18, 271, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(r"img_data\052d765b-0249-4a2d-bf13-fdgdfgdf.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 410, 221, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(249, 250, 181, 31))
        self.comboBox.setObjectName("comboBox")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(39, 256, 191, 21))
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
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(465, 250, 31, 31))
        self.toolButton.setObjectName("toolButton")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(21, 150, 501, 51))
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 413, 251, 31))
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
        self.label_5.setPalette(palette)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 551, 481))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(r"img_data\werwer.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.label_4.raise_()
        self.textEdit.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.horizontalLayoutWidget.raise_()
        self.pushButton_2.raise_()
        self.label_2.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.comboBox.raise_()
        self.label_3.raise_()
        self.toolButton.raise_()
        self.label_5.raise_()
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QtCore.QRect(20, 220, 101, 16))
        self.label_7.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.radioButton.setChecked(True)
        self.pushButton.clicked.connect(self.file_dialogue)
        self.pushButton_2.clicked.connect(self.next)
        self.pushButton_4.clicked.connect(lambda: webbrowser.open_new(self.website))
        self.pushButton_3.clicked.connect(lambda: print("pratyush21225@gmail.com"))
        self.toolButton.clicked.connect(self.default_details)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def default_details(self):
        print("Default setting:")
        print("-> images contains jpg,png,gif,jpeg,bmp")
        print("-> audios contains mp3,wav,amr,aac,m4a")
        print("-> videos contains mp4,mkv,avi,flv,mpeg,wmv,mov")
        print("-> documents contains doc,docx,ppt,pptx,pdf,txt")
        print("-> fonts contains ttf")
        print("-> zips contains zip,rar,7z")
        print("-> applications contains exe,msi")
        print("-> others contains other remaining extensions")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Choose File"))
        self.radioButton.setText(_translate("MainWindow", "Default"))
        self.radioButton_2.setText(_translate("MainWindow", "Custom"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))
        self.pushButton_4.setText(_translate("MainWindow", "About"))
        self.pushButton_3.setText(_translate("MainWindow", "Contact"))
        self.label_3.setText(_translate("MainWindow", "Organized by extension"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_5.setText(_translate("MainWindow", "                                       Organizer v1.0"))
        self.label_7.setText(_translate("MainWindow", u"Default Settings", None))

        self.comboBox.addItem("Folder Names")
        self.comboBox.addItem("images")
        self.comboBox.addItem("audios")
        self.comboBox.addItem("videos")
        self.comboBox.addItem("documents")
        self.comboBox.addItem("fonts")
        self.comboBox.addItem("zips")
        self.comboBox.addItem("applications")
        self.comboBox.addItem("others")

    def file_dialogue(self):
        self.path = QtWidgets.QFileDialog.getExistingDirectory()
        print(self.path)
        self.textEdit.setText(self.path)
        files = os.listdir(self.path)
        if ".idea" in files:
            files.remove(".idea")

        for file in files:
            print(file)
            if "." in file:
                print(file.split(".")[-1])  # to get extensions of file

    def check_availability(self):
        i = 0
        while os.path.isdir(self.path + r"\images" + str(i)) or os.path.isdir(
                self.path + r"others" + str(i)) or os.path.isdir(
                self.path + r"\audios" + str(i)) or os.path.isdir(self.path + r"\videos" + str(i)) or os.path.isdir(
            self.path + r"\documents" + str(i)) or os.path.isdir(self.path + r"\fonts" + str(i)) or os.path.isdir(
            self.path + r"\zips" + str(i)) or os.path.isdir(self.path + r"\applications" + str(i)):
            i = i + 1

        return i

    def next(self):
        if self.path == "":
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please choose a target folder")
            msg.addButton(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        else:
            if self.radioButton_2.isChecked():
                self.Mainwindow = QtWidgets.QMainWindow()
                self.ui = Ui_custom(self.path)
                self.ui.setupUi(self.Mainwindow)
                self.Mainwindow.show()
                # open a new window with custom settings

            if self.radioButton.isChecked():

                for root, dir, files in os.walk(self.path):
                    for file in files:
                        old = root + "\\" + file
                        new = self.path + "\\" + file
                        os.rename(old, new)

                for root, dirs, files in os.walk(self.path):
                    for dir in dirs:
                        loc = self.path + "\\" + dir
                        shutil.rmtree(loc)

                x = self.check_availability()
                i = str(x)
                os.mkdir(self.path + r"\images" + i)
                os.mkdir(self.path + r"\audios" + i)
                os.mkdir(self.path + r"\videos" + i)
                os.mkdir(self.path + r"\documents" + i)
                os.mkdir(self.path + r"\fonts" + i)
                os.mkdir(self.path + r"\zips" + i)
                os.mkdir(self.path + r"\applications" + i)
                os.mkdir(self.path + r"\others" + i)

                files = os.listdir(self.path)
                if ".idea" in files:
                    files.remove(".idea")

                for file in files:
                    if "." in file:
                        if file.split(".")[-1] == "jpg" or file.split(".")[-1] == "png" or file.split(".")[-1] == "gif" or \
                                file.split(".")[-1] == "jpeg" or file.split(".")[-1] == "bmp":
                            old = self.path + r"/" + file
                            new = self.path + r"/images" + i + r"/" + file
                            os.rename(old, new)

                        elif file.split(".")[-1] == "mp3" or file.split(".")[-1] == "wav" or file.split(".")[-1] == "amr" or \
                                file.split(".")[-1] == "aac" or file.split(".")[-1] == "m4a":
                            old = self.path + r"/" + file
                            new = self.path + r"/audios" + i + r"/" + file
                            os.rename(old, new)

                        elif file.split(".")[-1] == "mp4" or file.split(".")[-1] == "mkv" or file.split(".")[-1] == "avi" or \
                                file.split(".")[-1] == "flv" or file.split(".")[-1] == "mpeg" or file.split(".")[
                            -1] == "wmv" or file.split(".")[-1] == "mov":
                            old = self.path + r"/" + file
                            new = self.path + r"/videos" + i + r"/" + file
                            os.rename(old, new)

                        elif file.split(".")[-1] == "doc" or file.split(".")[-1] == "docx" or file.split(".")[
                            -1] == "ppt" or file.split(".")[-1] == "pptx" or file.split(".")[-1] == "pdf" or \
                                file.split(".")[-1] == "txt":
                            old = self.path + r"/" + file
                            new = self.path + r"/documents" + i + r"/" + file
                            os.rename(old, new)

                        elif file.split(".")[-1] == "ttf":
                            old = self.path + r"/" + file
                            new = self.path + r"/fonts" + i + r"/" + file
                            os.rename(old, new)

                        elif file.split(".")[-1] == "zip" or file.split(".")[-1] == "rar" or file.split(".")[-1] == "7z":
                            old = self.path + r"/" + file
                            new = self.path + r"/zips" + i + r"/" + file
                            os.rename(old, new)

                        elif file.split(".")[-1] == "exe" or file.split(".")[-1] == "msi":
                            old = self.path + r"/" + file
                            new = self.path + r"/applications" + i + r"/" + file
                            os.rename(old, new)

                        else:
                            old = self.path + r"/" + file
                            new = self.path + r"/others" + i + r"/" + file
                            os.rename(old, new)

                msg = QMessageBox()
                msg.setWindowTitle("Done")
                msg.setIcon(QMessageBox.Information)
                msg.setText("Folders Sorted")
                msg.addButton(QtWidgets.QMessageBox.Ok)
                msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon(r"img_data/icon.png"))
    MainWindow.setWindowTitle("Organizer")
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Kelebek/Desktop/DHT22/Arduino_anapen.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_anapencere(object):
    def setupUi(self, anapencere):
        anapencere.setObjectName("anapencere")
        anapencere.resize(542, 407)
        anapencere.setMinimumSize(QtCore.QSize(500, 300))
        anapencere.setMaximumSize(QtCore.QSize(1150, 650))
        self.centralwidget = QtWidgets.QWidget(anapencere)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(15, 70, 191, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setToolTip("")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.portac = QtWidgets.QPushButton(self.frame)
        self.portac.setGeometry(QtCore.QRect(20, 113, 151, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.portac.setFont(font)
        self.portac.setObjectName("portac")
        self.portkapat = QtWidgets.QPushButton(self.frame)
        self.portkapat.setGeometry(QtCore.QRect(20, 145, 151, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.portkapat.setFont(font)
        self.portkapat.setObjectName("portkapat")
        self.baud = QtWidgets.QLabel(self.frame)
        self.baud.setGeometry(QtCore.QRect(15, 79, 80, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.baud.setFont(font)
        self.baud.setObjectName("baud")
        self.portseciniz = QtWidgets.QLabel(self.frame)
        self.portseciniz.setGeometry(QtCore.QRect(15, 51, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.portseciniz.setFont(font)
        self.portseciniz.setObjectName("portseciniz")
        self.port = QtWidgets.QComboBox(self.frame)
        self.port.setGeometry(QtCore.QRect(100, 46, 70, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.port.setFont(font)
        self.port.setObjectName("port")
        self.port.addItem("")
        self.port.addItem("")
        self.port.addItem("")
        self.port.addItem("")
        self.port.addItem("")
        self.port.addItem("")
        self.port.addItem("")
        self.port.addItem("")
        self.port.addItem("")
        self.baudrate = QtWidgets.QComboBox(self.frame)
        self.baudrate.setGeometry(QtCore.QRect(100, 76, 70, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.baudrate.setFont(font)
        self.baudrate.setObjectName("baudrate")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.ayarlar = QtWidgets.QLabel(self.frame)
        self.ayarlar.setGeometry(QtCore.QRect(17, 14, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ayarlar.setFont(font)
        self.ayarlar.setObjectName("ayarlar")
        self.OFF = QtWidgets.QPushButton(self.centralwidget)
        self.OFF.setGeometry(QtCore.QRect(525, 277, 42, 23))
        self.OFF.setMinimumSize(QtCore.QSize(42, 23))
        self.OFF.setMaximumSize(QtCore.QSize(42, 23))
        self.OFF.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.OFF.setText("")
        self.OFF.setAutoDefault(False)
        self.OFF.setDefault(False)
        self.OFF.setFlat(True)
        self.OFF.setObjectName("OFF")
        self.RS232 = QtWidgets.QLabel(self.centralwidget)
        self.RS232.setGeometry(QtCore.QRect(516, 66, 30, 15))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.RS232.setFont(font)
        self.RS232.setText("")
        self.RS232.setObjectName("RS232")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(890, 290, 91, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"  color: rgb(170, 0, 0);\n"
"  text-align: center;\n"
"}\n"
"")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(890, 580, 91, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"  color: rgb(170, 0, 0);\n"
"  text-align: center;\n"
"}\n"
"")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.ruzgarYeksen = QtWidgets.QLabel(self.centralwidget)
        self.ruzgarYeksen.setGeometry(QtCore.QRect(599, 420, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ruzgarYeksen.setFont(font)
        self.ruzgarYeksen.setStyleSheet("QLabel\n"
"{\n"
"  color: rgb(170, 0, 0);\n"
"  text-align: center;\n"
"}\n"
"")
        self.ruzgarYeksen.setText("")
        self.ruzgarYeksen.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ruzgarYeksen.setObjectName("ruzgarYeksen")
        self.pb_cikis = QtWidgets.QPushButton(self.centralwidget)
        self.pb_cikis.setGeometry(QtCore.QRect(40, 300, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_cikis.setFont(font)
        self.pb_cikis.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1,   stop:0 rgba(225,225,225, 255), stop:1 rgba(210,180,140, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: rgb(225,225,225); border: 2px solid rgb(173,173,173);\n"
"     border-radius: 10px;\n"
"     color: rgb(50,50,50);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(225,225,225)\n"
"}")
        self.pb_cikis.setObjectName("pb_cikis")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(260, 20, 261, 341))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.progressBar_1 = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar_1.setGeometry(QtCore.QRect(50, 50, 21, 250))
        self.progressBar_1.setStyleSheet("QProgressBar {\n"
"     border: 2px solid;\n"
"     border-color: gray;\n"
"     border-radius: 5px;\n"
"     background-color: rgb(255, 255, 255);    \n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: rgb(255, 0, 0);   \n"
" }")
        self.progressBar_1.setProperty("value", 1)
        self.progressBar_1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.progressBar_1.setTextVisible(False)
        self.progressBar_1.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_1.setInvertedAppearance(False)
        self.progressBar_1.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_1.setObjectName("progressBar_1")
        self.progressBar_2 = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar_2.setGeometry(QtCore.QRect(182, 50, 21, 250))
        self.progressBar_2.setStyleSheet("QProgressBar {\n"
"     border: 2px solid;\n"
"     border-color: gray;\n"
"     border-radius: 5px;\n"
"     background-color: rgb(255, 255, 255);\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: rgb(85, 255, 255);\n"
" }")
        self.progressBar_2.setProperty("value", 1)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(32, 310, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(154, 310, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel\n"
"\n"
" {\n"
"     border: 2px solid;\n"
"     border-color: gray;\n"
"     border-radius: 5px;\n"
"     background-color: rgb(255, 255, 255);\n"
" }")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(161, 10, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel\n"
"\n"
" {\n"
"     border: 2px solid;\n"
"     border-color: gray;\n"
"     border-radius: 5px;\n"
"     background-color: rgb(255, 255, 255);\n"
" }")
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(95, 43, 60, 275))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("Scale.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 22, 181, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel\n"
"\n"
" {\n"
"     border: 2px solid;\n"
"     border-color: gray;\n"
"     border-radius: 5px;\n"
"     background-color: rgb(255, 255, 255);\n"
" }")
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        anapencere.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(anapencere)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 542, 21))
        self.menubar.setObjectName("menubar")
        anapencere.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(anapencere)
        self.statusbar.setObjectName("statusbar")
        anapencere.setStatusBar(self.statusbar)

        self.retranslateUi(anapencere)
        self.port.setCurrentIndex(2)
        self.baudrate.setCurrentIndex(12)
        self.OFF.clicked.connect(anapencere.close)
        self.portkapat.clicked.connect(self.RS232.clear)
        self.pb_cikis.clicked.connect(anapencere.close)
        QtCore.QMetaObject.connectSlotsByName(anapencere)

    def retranslateUi(self, anapencere):
        _translate = QtCore.QCoreApplication.translate
        anapencere.setWindowTitle(_translate("anapencere", "Arduino Arayüz"))
        self.portac.setText(_translate("anapencere", "Port Aç"))
        self.portkapat.setText(_translate("anapencere", "Port Kapat"))
        self.baud.setText(_translate("anapencere", "Baud Rate"))
        self.portseciniz.setText(_translate("anapencere", "Port"))
        self.port.setCurrentText(_translate("anapencere", "COM3"))
        self.port.setItemText(0, _translate("anapencere", "COM1"))
        self.port.setItemText(1, _translate("anapencere", "COM2"))
        self.port.setItemText(2, _translate("anapencere", "COM3"))
        self.port.setItemText(3, _translate("anapencere", "COM4"))
        self.port.setItemText(4, _translate("anapencere", "COM5"))
        self.port.setItemText(5, _translate("anapencere", "COM6"))
        self.port.setItemText(6, _translate("anapencere", "COM7"))
        self.port.setItemText(7, _translate("anapencere", "COM8"))
        self.port.setItemText(8, _translate("anapencere", "COM9"))
        self.baudrate.setCurrentText(_translate("anapencere", "9600"))
        self.baudrate.setItemText(0, _translate("anapencere", "50"))
        self.baudrate.setItemText(1, _translate("anapencere", "75"))
        self.baudrate.setItemText(2, _translate("anapencere", "110"))
        self.baudrate.setItemText(3, _translate("anapencere", "134"))
        self.baudrate.setItemText(4, _translate("anapencere", "150"))
        self.baudrate.setItemText(5, _translate("anapencere", "200"))
        self.baudrate.setItemText(6, _translate("anapencere", "300"))
        self.baudrate.setItemText(7, _translate("anapencere", "600"))
        self.baudrate.setItemText(8, _translate("anapencere", "1200"))
        self.baudrate.setItemText(9, _translate("anapencere", "1800"))
        self.baudrate.setItemText(10, _translate("anapencere", "2400"))
        self.baudrate.setItemText(11, _translate("anapencere", "4800"))
        self.baudrate.setItemText(12, _translate("anapencere", "9600"))
        self.baudrate.setItemText(13, _translate("anapencere", "19200"))
        self.baudrate.setItemText(14, _translate("anapencere", "38400"))
        self.baudrate.setItemText(15, _translate("anapencere", "57600"))
        self.baudrate.setItemText(16, _translate("anapencere", "115200"))
        self.ayarlar.setText(_translate("anapencere", "AYARLAR"))
        self.pb_cikis.setText(_translate("anapencere", "ÇIKIŞ"))
        self.label.setText(_translate("anapencere", "ISI (C)"))
        self.label_2.setText(_translate("anapencere", "NEM (%)"))

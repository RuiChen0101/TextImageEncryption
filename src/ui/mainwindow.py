# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/ui/mainui.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 470)
        MainWindow.setMinimumSize(QtCore.QSize(390, 470))
        MainWindow.setMaximumSize(QtCore.QSize(390, 470))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self._openEncryptFile = QtWidgets.QPushButton(self.centralwidget)
        self._openEncryptFile.setGeometry(QtCore.QRect(20, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self._openEncryptFile.setFont(font)
        self._openEncryptFile.setObjectName("_openEncryptFile")
        self._fileName = QtWidgets.QLabel(self.centralwidget)
        self._fileName.setGeometry(QtCore.QRect(160, 10, 221, 61))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self._fileName.setFont(font)
        self._fileName.setText("")
        self._fileName.setObjectName("_fileName")
        self._password = QtWidgets.QLineEdit(self.centralwidget)
        self._password.setGeometry(QtCore.QRect(20, 110, 221, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self._password.setFont(font)
        self._password.setInputMask("")
        self._password.setText("")
        self._password.setObjectName("_password")
        self._encrypt = QtWidgets.QPushButton(self.centralwidget)
        self._encrypt.setEnabled(False)
        self._encrypt.setGeometry(QtCore.QRect(270, 90, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        self._encrypt.setFont(font)
        self._encrypt.setObjectName("_encrypt")
        self._decrypt = QtWidgets.QPushButton(self.centralwidget)
        self._decrypt.setEnabled(False)
        self._decrypt.setGeometry(QtCore.QRect(270, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        self._decrypt.setFont(font)
        self._decrypt.setObjectName("_decrypt")
        self._content = QtWidgets.QTextEdit(self.centralwidget)
        self._content.setGeometry(QtCore.QRect(20, 170, 351, 261))
        self._content.setObjectName("_content")
        self._message = QtWidgets.QLabel(self.centralwidget)
        self._message.setGeometry(QtCore.QRect(20, 440, 351, 21))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self._message.setFont(font)
        self._message.setText("")
        self._message.setObjectName("_message")
        self._openDecryptFile = QtWidgets.QPushButton(self.centralwidget)
        self._openDecryptFile.setGeometry(QtCore.QRect(20, 50, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self._openDecryptFile.setFont(font)
        self._openDecryptFile.setObjectName("_openDecryptFile")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "mainWindow"))
        self._openEncryptFile.setText(_translate("MainWindow", "開啟加密檔案"))
        self._password.setPlaceholderText(_translate("MainWindow", "password"))
        self._encrypt.setText(_translate("MainWindow", "加密"))
        self._decrypt.setText(_translate("MainWindow", "解密"))
        self._openDecryptFile.setText(_translate("MainWindow", "開啟解密檔案"))



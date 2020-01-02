import sys
import os
import hashlib
from src.imagefile import ImageFile
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtWidgets, QtCore
from src.ui.mainwindow import Ui_MainWindow

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui._openEncryptFile.clicked.connect(self.SelectEncryptFile)
        self.ui._openDecryptFile.clicked.connect(self.SelectDecryptFile)
        self.ui._encrypt.clicked.connect(self.StartEncrypt)
        self.ui._decrypt.clicked.connect(self.StartDecrypt)

    def SelectEncryptFile(self):
        file = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.jpg *.jpeg)")
        fileName = (file[0].split('/'))[-1]
        self._image = ImageFile(file[0],fileName[0:-4])
        self.ui._fileName.setText(fileName)
        self.ui._decrypt.setEnabled(False)
        self.ui._encrypt.setEnabled(True)
        self.ui._message.setText(str(int(self._image.avalSpace))+"可用字元")

    def SelectDecryptFile(self):
        file = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png)")
        fileName=(file[0].split('/'))[-1]
        self._image = ImageFile(file[0],fileName[0:-4])
        self.ui._fileName.setText(fileName)
        self.ui._encrypt.setEnabled(False)
        self.ui._decrypt.setEnabled(True)
        self.ui._message.setText("")

    def StartEncrypt(self):
        message=self.ui._content.toPlainText()
        key=self.ui._password.text()
        if message!='' and key!='':
            bin = self.string2bin(message)
            print(bin)
            print(len(bin))
            keyX, keyY=self.GetKey(key)
            self._image.BinaryEncrypt(bin, keyX, keyY)
            self.EncryptSuccess()
        else:
            self.ui._message.setText("content or password is empty")

    def StartDecrypt(self):
        key=self.ui._password.text()
        if key!='':
            keyX, keyY=self.GetKey(key)
            stateCode, bin=self._image.BinaryDecrypt(keyX, keyY)
            if(stateCode):
                decodeString=self.bin2string(bin)
                self.ui._content.setText(decodeString)
                self.DecryptSuccess()
            else:
                self.ui._message.setText("decrypt fail")
        else:
            self.ui._message.setText("password is empty")

    def DecryptSuccess(self):
        self.ui._message.setText("decrypt success")
        self.ui._password.setText("")
        del self._image
        self._image=None
        self.ui._encrypt.setEnabled(False)
        self.ui._decrypt.setEnabled(False)

    def EncryptSuccess(self):
        self.ui._message.setText("encrypt success")
        self.ui._password.setText("")
        self.ui._content.setText("")
        self.ui._fileName.setText("")
        del self._image
        self._image=None
        self.ui._encrypt.setEnabled(False)
        self.ui._decrypt.setEnabled(False)

    def string2bin(self, string):
        return ''.join(bin(ord(c))[2:].zfill(8) for c in string)

    def bin2string(self, binary):
        return ''.join([chr(int(x, 2)) for x in binary])

    def GetKey(self, key):
        split = [char for char in key]
        kx=split[0::2]
        ky=split[1::2]
        kx=''.join(i for i in kx)
        ky=''.join(i for i in ky)
        return hashlib.sha1(kx.encode('utf-8')).digest(), hashlib.sha1(ky.encode('utf-8')).digest()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())

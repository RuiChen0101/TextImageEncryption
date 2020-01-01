import sys
import os
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

    def SelectEncryptFile(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.jpg *.jpeg)")
        fileName=(fileName[0].split('/'))[-1]
        self.ui._fileName.setText(fileName);
        self.ui._encrypt.setEnabled(True);
        self.ui._decrypt.setEnabled(False);

    def SelectDecryptFile(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png)")
        fileName=(fileName[0].split('/'))[-1]
        self.ui._fileName.setText(fileName);
        self.ui._encrypt.setEnabled(False);
        self.ui._decrypt.setEnabled(True);

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())

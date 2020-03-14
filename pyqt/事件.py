



import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication,QPushButton,QLineEdit,QInputDialog
class Communicate(QObject):
    closeApp = pyqtSignal() 
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.button=QPushButton('Dialog',self)     
        self.button.move(20,30)
        self.button.clicked[bool].connect(self.showDialog)
        self.le=QLineEdit(self)
        self.le.move(20,10)
    def showDialog(self):
        text,ok=QInputDialog.getText(self,'input dialog','enter your name')

        if ok:
            self.le.setText(str(text))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
    
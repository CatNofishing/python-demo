
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame, 
    QSplitter, QStyleFactory, QApplication,QVBoxLayout,QComboBox,QLabel,QMessageBox)
from PyQt5.QtCore import Qt,pyqtSignal,QObject
from PyQt5.QtGui import QFont
import sys
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):      
        self.label=QLabel('label',self)
        combo=QComboBox(self)
        combo.addItem('a')
        combo.addItem('b')
        combo.addItem('c')
        combo.activated.connect(self.levent)
        self.resize(200,200)
    
    def levent(self,text):
        if text=='a':
            print('sshss')
        elif text=='b':
            print('sdddd')
        else:
            print('ddjdhd')

    def closeEvent(self,event):
        print(event)
        box=QMessageBox()
        reply=box.question(self,'退出','缺认退出!',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else :
            event.ignore()
    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
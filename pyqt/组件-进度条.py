from PyQt5.QtWidgets import  QApplication,QMainWindow,QPushButton,QWidget,QSlider,QProgressBar

from PyQt5.QtGui import QFont,QColor
from PyQt5.QtCore import Qt,QObject,pyqtSignal,QBasicTimer,QObject,QEvent

import sys

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.init()
    
    def init(self):
        self.timer=QBasicTimer()
        self.pbr=QProgressBar(self)
        self.pbr.resize(200,25)
        self.step=0
        self.btn=QPushButton('start',self)
        self.btn.clicked.connect(self.doaction)
        self.btn.move(10,10)
        self.pbr.move(10,50)
        self.setGeometry(100,100,300,300)


    def timerEvent(self,e):

        if self.step>100:
            self.timer.stop()
            self.btn.setText('finshed')
            return
        else:
            self.step+=1
            self.pbr.setValue(self.step)


    def doaction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('start')
        else:
            self.timer.start(100,self)
            self.btn.setText('stop')
            

if __name__ =='__main__':
    app=QApplication(sys.argv)
    window=window()
    window.show()
    sys.exit(app.exec_())
        
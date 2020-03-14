from PyQt5.QtWidgets import QWidget,QApplication,QCalendarWidget,QLabel,QVBoxLayout,QMainWindow

from PyQt5.QtCore import QDate,QEvent
from PyQt5.QtGui import QCloseEvent

import sys

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        vbox=QVBoxLayout(self)
        cal=QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked.connect(self.showdate)
        vbox.addWidget(cal)
        self.lbl=QLabel(self)
        date=cal.selectedDate()
        self.lbl.setText(date.toString())
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)
    def showdate(self,date):
        self.lbl.setText(date.toString())

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=window()
    window.show()
    sys.exit(app.exec_())




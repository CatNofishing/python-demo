from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QSlider
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()
    
    def init(self):

        self.label=QLabel(self)
        self.label.setText('这是标签')
        self.slide=QSlider(Qt.Horizontal,self)
        self.slide.setGeometry(100,100,200,40)
        self.label.setGeometry(350,100,200,200)

        self.slide.valueChanged.connect(self.changevalue)
        self.resize(500,500)

    def changevalue(self,value):
        if value>=0 and value<=30:
            self.label.setPixmap(QPixmap('./图标/1.jpg'))
       
        elif value>30 and value<60:
            self.label.setPixmap(QPixmap('./图标/2.jpg'))
        
        else:
            self.label.setPixmap(QPixmap('./图标.jpg'))



if __name__=='__main__':
    app=QApplication(sys.argv)
    window=window()
    window.show()
    sys.exit(app.exec_())


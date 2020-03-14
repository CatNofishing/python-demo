from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton
from PyQt5.QtCore import QMimeData,Qt,QObject,pyqtSignal
from PyQt5.QtGui import QDrag,QPixmap
import sys
class Button(QPushButton):
    def __init__(self,parent=None):
        super().__init__(parent)
    
    def mouseMoveEvent(self,e):
        if e.buttons() != Qt.RightButton:
            return
        else:
            drag=QDrag(self)
            data=QMimeData()
            drag.setMimeData(data)
            drag.setPixmap(QPixmap('./图标/1.jpg'))
            drag.setHotSpot(e.pos() - self.rect().topLeft())
            print(e.pos())
            print(self.rect())
            drag.exec_(Qt.MoveAction)
        
    def mousePressEvent(self,e):
        if e.buttons()==Qt.LeftButton:
            print('press')

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()
    
    def init(self):
        self.setAcceptDrops(True)
        self.buton=Button(self)
        self.resize(300,300)
        self.move(500,500)
        self.buton.move(100,100)
        self.setMouseTracking(True)
        print(self.rect())

    def dragEnterEvent(self,e):
        e.accept()
       
    
    def dropEvent(self,e):
        self.buton.move(e.pos())
        e.setDropAction(Qt.MoveAction)
        e.accept()

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=window()
    window.show()
    sys.exit(app.exec_())
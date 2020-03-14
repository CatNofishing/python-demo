from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication,QLineEdit,QPushButton

import sys

class Button(QPushButton):
    def __init__(self,parent):
        super().__init__(parent)
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self,e):
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()
            print('没有文本')
        
    def dropEvent(self,e):
        self.setText(e.mimeData().text())




class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()
    
    def init(self):
        edit=QLineEdit(self)
        edit.setDragEnabled(True)
        button=Button(self)
        button.setText('按钮')
        edit.move(30,30)
        button.move(100,100)
        self.resize(300,300)
    

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=window()
    window.show()
    sys.exit(app.exec_())
        
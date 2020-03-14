from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QLabel

import sys
class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()
    
    def init(self):
        self.label=QLabel('文本',self)
        self.input=QLineEdit(self)
        self.label.move(100,100)
        self.input.move(100,150)

        self.input.textChanged.connect(self.change)
        self.resize(500,500)
    
    def change(self,text):
        self.label.setText(text)
        self.label.adjustSize()
    

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=window()
    window.show()
    sys.exit(app.exec_())
        

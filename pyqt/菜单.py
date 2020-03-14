from PyQt5.QtWidgets import QApplication,QMainWindow,QAction
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()
    
    def init(self):
        menubar=self.menuBar()
        menu1=menubar.addMenu('文件')
        menu2=menubar.addMenu('编辑')
        menu3=menubar.addMenu('选择')

        ac11=menu1.addAction('新建文件')
        ac12=menu1.addAction('打开文件')
        ac13=menu1.addAction('退出')
        ac13.triggered.connect(self.closeEvent)
        menubar.setStyleSheet('QMenuBar{background-color:red}')

    def closeEvent(self,event):
        QApplication.instance().quit()



if __name__=='__main__':
    app=QApplication(sys.argv)
    window=window()
    window.show()
    sys.exit(app.exec_())
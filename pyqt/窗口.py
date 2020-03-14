from PyQt5.QtWidgets import QMainWindow,QApplication,QToolTip,QAction,QMessageBox,QDesktopWidget,QMenu,QTextEdit,QStatusBar
from PyQt5.QtGui import QIcon,QFont,QColor,QPixmap
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        QToolTip.setFont(QFont('微软雅黑',18))
        self.setWindowTitle('窗口')
        self.setWindowIcon(QIcon('./图标/cat.svg'))
        self.resize(400,300)
        self.setToolTip('这是文本区')
        self.status=self.statusBar()
        self.status.showMessage('欢迎使用',5000)
        
        textedit=QTextEdit(self)
        self.setCentralWidget(textedit)
        



        menubar=self.menuBar()
        menubar.setFont(QFont('宋体',12))
        menu1=menubar.addMenu('文件')
        menu2=menubar.addMenu('编辑')
        menu3=menubar.addMenu('选择')
        menu4=menubar.addMenu('查看')
        menu5=menubar.addMenu('转到')
        menu6=menubar.addMenu('调试')
        menu7=menubar.addMenu('终端')
        menu8=menubar.addMenu('帮助')
    
        menu1.setStatusTip('文件')

        act11=QAction('新建文件',self)
        act12=QAction('新建窗口',self)
        act13=QAction('关闭文件夹',self)
        act14=QAction('退出',self)
        act14.setStatusTip('退出')
        act14.setShortcut('Ctrl+Q')
        act14.triggered.connect(self.close)
        menu1.addActions([act11,act12,act13,act14])
        
        act21=QAction('撤销',self)
        act22=QAction('恢复',self)
        act23=QAction('剪切',self)
        act24=QAction('查找',self)
        menu2.addActions([act21,act22])
        menu2.addSeparator()
        menu2.addActions([act23,act24])
        menu2.setToolTip('编辑')

        act31=QAction('全选',self)
        act31.setCheckable(True)
        act31.setChecked(True)
        act31.setStatusTip('选中')
        act31.setShortcut('Ctrl+A')
        act31.triggered.connect(self.togglemenu)
        act32=QAction('展开选定内容',self)
        act32.setStatusTip('展开')
        act33=QAction('缩小选定范围',self)
        act34=QAction('向上复制一行',self)
        act35=QAction('向下复制一行',self)
        menu3.addActions([act31,act32,act33,act34,act35])

        toolbar=self.addToolBar('工具栏')
        act=QAction(QIcon('./图标/tigger.jpg'),'退出',self)
        act.triggered.connect(self.close)
        toolbar.addAction(act)
        self.center()

    def togglemenu(self,state):
        if state:
            print(state)
            self.statusBar().show()
        else:
            self.statusBar().hide()


    def contextMenuEvent(self,event):
        print(event)
        menu=QMenu(self)
        act1=QAction('选择',self)
        act2=QAction('编辑',self)
        act3=QAction('退出',self)
        menu.addActions([act1,act2,act3])
        action=menu.exec_(self.mapToGlobal(event.pos()))
        if action is act3:
            print(act3)
            QApplication.instance().quit()


    def center(self):
        dec=QDesktopWidget().geometry()
        win=self.geometry()
        win.moveCenter(dec.center())


    def closeEvent(self,event):
        box=QMessageBox()
        reply=box.question(self,'退出','缺认退出!',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else :
            event.ignore()

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=window()
    window.show()
    sys.exit(app.exec_())

    



        

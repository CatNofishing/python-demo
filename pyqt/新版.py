from PyQt5.QtWidgets import QWidget,QApplication,QSlider,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QPainter,QFont,QColor,QPen
from PyQt5.QtCore import Qt,QObject,pyqtSignal
import sys



class communicate(QObject):
    updateBW=pyqtSignal(int)


class newwidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.init()
    
    def init(self):
        self.setMinimumSize(1,30)
        self.value=75
        self.num=[75*x for x in range(1,10)]

    def setvalue(self,value):
        self.value=value
        print(self.value)
    
    def paintEvent(self,event):
        painter=QPainter()
        painter.begin(self)
        self.drowwidget(painter)
        painter.end()
    
    def drowwidget(self,painter):
        max_capacity=700
        over_capacity=750
        font=QFont('微软雅黑',7,QFont.Light)
        painter.setFont(font)
        w=self.size().width()
        h=self.size().height()
        till=int((w/over_capacity)*self.value)
        full=int((w/over_capacity)*max_capacity)
        step=int(w/10)
        if self.value>=max_capacity:
            painter.setPen(QColor('black'))
            painter.setBrush(QColor('LightPink'))
            painter.drawRect(0,0,full,h)
            painter.setPen(QColor('black'))
            painter.setBrush(QColor('red'))
            painter.drawRect(full,0,till-full,h)
        else:
            painter.setPen(QColor('black'))
            painter.setBrush(QColor('LightPink'))
            painter.drawRect(0,0,till,h)
        
        pen=QPen(QColor('green'))
        painter.setBrush(Qt.NoBrush)
        painter.setPen(pen)
        painter.drawRect(0,0,w-1,h-1)
        j=0
        for i in range(step,step*10,step):
            painter.drawLine(i,0,i,5)
            metrics=painter.fontMetrics()
            fw=metrics.width(str(self.num[j]))
            painter.drawText(i-fw/2,h/2,str(self.num[j]))
            j+=1


class window(QWidget):

    def __init__(self):
        super().__init__()
        self.init()
    
    def init(self):
        slider=QSlider(Qt.Horizontal,self)
        slider.setRange(1,750)
        slider.setValue(75)
        slider.setGeometry(30, 40, 150, 30)


        self.wid=newwidget()
        self.c=communicate()
        self.c.updateBW[int].connect(self.wid.setvalue)
        slider.valueChanged[int].connect(self.changevalue)
        vbox=QVBoxLayout(self)
        hbox=QHBoxLayout()
        hbox.addWidget(self.wid)
        
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle('Burning widget')
        self.show()

    def changevalue(self,value):
        self.c.updateBW.emit(value)
        self.wid.repaint()
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=window()
    sys.exit(app.exec_())
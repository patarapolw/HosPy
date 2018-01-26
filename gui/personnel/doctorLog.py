import sys, os
if __name__ == '__main__':
    os.chdir('../')
    sys.path.insert(0,'.')

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def main(param={'type':'admin'}):
    global window
    window = MainWindow()
    window.param = param
    window.showUI()

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('Preferences')

    def showUI(self):
        overall = Layout()
        overall.param = self.param
        overall.setWidget()

        self.setLayout(overall)
        self.show()

class SubWindow(QMdiSubWindow):
    def __init__(self, *args, **kwargs):
        super(SubWindow, self).__init__(*args, **kwargs)

    def showUI(self):
        overall = Layout()
        overall.param = self.param
        overall.setWidget()

        widget = QWidget()
        widget.setLayout(overall) 
        
        self.setWidget(widget)
        self.show()

class Layout(QVBoxLayout):
    def __init__(self, *args, **kwargs):
        super(Layout, self).__init__(*args, **kwargs)

    def setWidget(self):
        center = QLabel(repr(self.param))
        self.addWidget(center)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main()
    sys.exit(app.exec_())
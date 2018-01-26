import sys, os
if os.getcwd() == os.path.dirname(os.path.abspath(__file__)):
    os.chdir('../')
    sys.path.insert(0,'.')

from gui import preferences, personnel, patient, login

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

MENU = {
    'pref' : 'Preferences',
    'newPatient' : 'New patient',
    'newPersonnel' : 'New personnel',
    'doctorWork' : "Doctor workstation", 
    'nurseWork' : "Nurse workstation", 
    'doctorLog' : "Doctor's log", 
    'wardLog' : "Ward's log", 
    'emr' : 'Patient EMR',
    'logout' :"Logout"
}

def main(param={'type':'admin'}):
    global window
    window = MainWindow()
    window.param = param
    window.showUI()

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('HosPy')

    def showUI(self):
        menubar = self.menuBar()

        settings = menubar.addMenu('&Settings')
        self.createMenu( (MENU['pref'], ),
            settings, self.menuBarAction)

        workStation = menubar.addMenu('&File')
        self.createMenu( (MENU['newPatient'], MENU['newPersonnel'], 'sep', 
            MENU['doctorWork'], MENU['nurseWork'], 'sep', MENU['logout']) ,
            workStation, self.menuBarAction)

        view = menubar.addMenu('&View')
        self.createMenu( (MENU['doctorLog'], MENU['wardLog'],'sep', MENU['emr']),
            view, self.menuBarAction)

        resolution = QDesktopWidget().screenGeometry()
        self.setGeometry(0,0,resolution.width(),resolution.height())
        
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.show()

    def menuBarAction(self, qaction):
        text = qaction.text()
        if text == MENU['pref']:
            sub = preferences.SubWindow()
        elif text == MENU['doctorWork']:
            sub = personnel.doctorWork.SubWindow()
        elif text == MENU['nurseWork']:
            sub = personnel.nurseWork.SubWindow()
        elif text == MENU['logout']:
            login.main()
            self.close()
            return
        elif text == MENU['doctorLog']:
            sub = personnel.doctorLog.SubWindow()
        elif text == MENU['wardLog']:
            sub = personnel.wardLog.SubWindow()
        elif text == MENU['emr']:
            sub = patient.emr.SubWindow()

        sub.param = self.param
        self.mdi.addSubWindow(sub)
        sub.showUI()

    def createMenu(self, wordList, menu, action):
        for text in wordList:
            if text == 'sep':
                menu.addSeparator()
            else:
                menu.addAction(QAction(text,self))
        menu.triggered[QAction].connect(action)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main()
    sys.exit(app.exec_())
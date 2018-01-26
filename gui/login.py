import sys, os
if __name__ == '__main__':
	os.chdir('../')
	sys.path.insert(0,'.')

from gui import mainWindow

from passlib.hash import bcrypt
import sqlite3, os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def main():
	global window
	window = MainWindow()
	window.showUI()

class MainWindow(QWidget):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle('Please login')

	def showUI(self):
		userText = QLabel('Username')
		self.userInput = QLineEdit()

		passText = QLabel('Password')
		self.passInput = QLineEdit()
		self.passInput.setEchoMode(QLineEdit.Password)

		self.userInput.returnPressed.connect(self.passInput.setFocus)
		self.passInput.returnPressed.connect(self.login)

		top = QGridLayout()
		top.addWidget(userText, 1,1)
		top.addWidget(self.userInput, 1,2)
		top.addWidget(passText, 2,1)
		top.addWidget(self.passInput, 2,2)

		login = QPushButton('Login')
		login.clicked.connect(self.login)
		quitApp = QPushButton('Quit')
		quitApp.clicked.connect(self.close)

		bottom = QHBoxLayout()
		bottom.addWidget(login)
		bottom.addWidget(quitApp)

		overall = QVBoxLayout()
		overall.addLayout(top)
		overall.addLayout(bottom)
		self.setLayout(overall)

		frame = self.size()
		screen = QDesktopWidget().screenGeometry()
		self.move(screen.width()/2 - frame.width()/2, screen.height()/2 - frame.height()/2)
		self.show()

	def login(self):
		d = QDialog()

		resultText = self.checkLogin(self.userInput.text(), self.passInput.text())
		result = QLabel(resultText)

		ok = QPushButton('OK')
		ok.clicked.connect(d.close)

		layout = QVBoxLayout(d)
		layout.addWidget(result)
		layout.addWidget(ok)

		d.exec_()

	def checkLogin(self, username, password):
		db_path = os.path.join('database','login.db')
		with sqlite3.connect(db_path) as con:
			query = 'SELECT h,type FROM login WHERE username=?'
			cursor = con.execute(query, (username, ))
			try:
				h, typeOfUser = list(cursor)[0]
			except IndexError:
				return 'No such username.'

		verify = bcrypt.verify(password, h)
		param = {'username':username, 'type':typeOfUser }

		if verify:
			mainWindow.main(param)
			self.close()
			return 'Login successful.'
		else:
			return 'Wrong password, please try again.'

if __name__ == '__main__':
	app = QApplication(sys.argv)
	main()
	sys.exit(app.exec_())
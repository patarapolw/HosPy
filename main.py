from gui import login
import common

from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
login.main()
sys.exit(app.exec_())
from PyQt5.QtWidgets import *
from myapp_ui import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.clicks = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_plus.clicked.connect(self.inc)
        self.ui.btn_minus.clicked.connect(self.dec)


    def inc(self):
        self.clicks += 1
        self.ui.l1.setText(f"You clicked {self.clicks} times")

    def dec(self):
        self.clicks -= 1
        self.ui.l1.setText(f"You clicked {self.clicks} times")


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

from PySide2.QtWidgets import *
import sys

class MyGuiApp:
    def __init__(self):
        self.w = QWidget()
        self.w.show()

        self.layout = QVBoxLayout(self.w)
        self.clicks = 0

        # 1. Draw stuff on screen
        self.l1 = QLabel(self.get_text_for_label(), parent=self.w)
        self.layout.addWidget(self.l1)

        btn_plus = QPushButton("Click me", parent=self.w)
        self.layout.addWidget(btn_plus)

        # 2. Bind event handlers
        btn_plus.clicked.connect(self.increase_value_in_label)

    def increase_value_in_label(self):
        self.clicks += 1
        self.l1.setText(self.get_text_for_label())

    def get_text_for_label(self):
        return f"Ouch! you clicked {self.clicks} times"

app = QApplication(sys.argv)
myapp = MyGuiApp()

# 3. Start Main Loop
app.exec_()

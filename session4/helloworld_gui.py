from PySide2.QtWidgets import *
import sys

# Lab:
# 1. Add a new button "Minus"
# 2. Clicking on that new button will DECREASE the value
#
# 3. Bonus: put the buttons one next to the other,
#           leaving the label above both
#
# 10 Minutes - until 13:06



class MyGuiApp:
    def __init__(self):
        self.w = QWidget()
        self.w.show()

        self.layout = QVBoxLayout(self.w)
        self.buttons_layout = QHBoxLayout()


        self.clicks = 0

        # 1. Draw stuff on screen
        self.l1 = QLabel(self.get_text_for_label(), parent=self.w)
        self.layout.addWidget(self.l1)

        btn_plus = QPushButton("+", parent=self.w)
        self.buttons_layout.addWidget(btn_plus)

        btn_minus = QPushButton("-", parent=self.w)
        self.buttons_layout.addWidget(btn_minus)


        # 2. Bind event handlers
        btn_plus.clicked.connect(self.increase_value_in_label)
        btn_minus.clicked.connect(self.decrease_value_in_label)

        self.layout.addLayout(self.buttons_layout)


    def increase_value_in_label(self):
        self.clicks += 1
        self.l1.setText(self.get_text_for_label())

    def decrease_value_in_label(self):
        self.clicks -= 1
        self.l1.setText(self.get_text_for_label())

    def get_text_for_label(self):
        return f"Ouch! you clicked {self.clicks} times"

app = QApplication(sys.argv)
myapp = MyGuiApp()

# 3. Start Main Loop
app.exec_()

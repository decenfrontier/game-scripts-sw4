from PySide2.QtWidgets import QMessageBox, QPushButton
from PySide2.QtCore import QTimer

class TimeMsgBox(QMessageBox):
    def __init__(self, title: str, text: str, timeout=5):
        super().__init__()
        self.timeout = timeout
        self.setWindowTitle(title)
        self.setText(text)

        self.btn_accept = QPushButton(f"确 定 ({self.timeout})")
        self.btn_reject = QPushButton("取 消")
        self.addButton(self.btn_accept, QMessageBox.ButtonRole.AcceptRole)
        self.addButton(self.btn_reject, QMessageBox.ButtonRole.RejectRole)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer_timeout)
        self.timer.start(1000)

    def on_timer_timeout(self):
        self.timeout -= 1
        self.btn_accept.setText(f"确 定 ({self.timeout})")
        if self.timeout <= 0:
            self.btn_accept.click()


class MyMsgBox(QMessageBox):
    def __init__(self, title: str, text: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setText(text)
        self.btn_accept = QPushButton("确 定")
        self.btn_reject = QPushButton("取 消")
        self.addButton(self.btn_accept, QMessageBox.ButtonRole.AcceptRole)
        self.addButton(self.btn_reject, QMessageBox.ButtonRole.RejectRole)

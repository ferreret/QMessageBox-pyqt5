import sys
from PyQt5.QtWidgets import *


def evt_btn_clicked() -> None:
    msg_disk_full = QMessageBox()
    msg_disk_full.setText("Your hard drive is almost full")
    msg_disk_full.setDetailedText("Please, make some room on your disk")
    msg_disk_full.setIcon(QMessageBox.Information)
    msg_disk_full.setWindowTitle("Full drive")
    msg_disk_full.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg_disk_full.exec_()


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200, 200)

        self.btn = QPushButton("ShowMessage", self)
        self.btn.move(40, 40)
        self.btn.clicked.connect(evt_btn_clicked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())

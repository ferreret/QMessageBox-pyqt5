import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.resize(200, 200)

        self.btn = QPushButton("ShowMessage", self)
        self.btn.move(40, 40)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        res = QMessageBox.question(self, "Disk full", "Your disk drive is almost full")
        if res == QMessageBox.Yes:
            QMessageBox.information(self, "", "You clicked yes")
        else:
            QMessageBox.information(self, "", "You clicked no")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())

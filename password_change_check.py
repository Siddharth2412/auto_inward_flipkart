import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
status = True

class App(QWidget):

    def __init__(self,app):
        super().__init__()
        self.title = 'Confirmation'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.app = app
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        buttonReply = QMessageBox.question(self, 'Password Change Check', "Did You Change your password?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            global status
            status = False
            self.app.quit()


def confirmation():
    app = QApplication(sys.argv)
    ex = App(app)
    app.quit()
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        QMessageBox.about(self, "Information", "Success Fully Inward")


class ErrorMessage(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        QMessageBox.about(self, "Error", "All Listing IDs Are Not Converted Properly")


def finish():
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    app.quit()


def error():
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ErrorMessage()
    mainWin.show()
    app.quit()

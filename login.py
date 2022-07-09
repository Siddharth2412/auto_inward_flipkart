import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
# import time

id, pwd = '', ''
class LoginForm(QWidget):
	def __init__(self,app):
		super().__init__()
		self.setWindowTitle('Login Form')
		self.resize(300, 80)
		self.app = app
		layout = QGridLayout()

		label_name = QLabel('<font size="4"> Username </font>')
		self.lineEdit_username = QLineEdit()
		self.lineEdit_username.setPlaceholderText('Please enter your username')
		layout.addWidget(label_name, 0, 0)
		layout.addWidget(self.lineEdit_username, 0, 1)

		label_password = QLabel('<font size="4"> Password </font>')
		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setPlaceholderText('Please enter your password')
		layout.addWidget(label_password, 1, 0)
		layout.addWidget(self.lineEdit_password, 1, 1)

		button_login = QPushButton('Save Data', self)
		button_login.clicked.connect(self.check_password)
		layout.addWidget(button_login, 2, 0, 1, 2)
		layout.setRowMinimumHeight(2, 60)
		self.setLayout(layout)


	def check_password(self):
		msg = QMessageBox()
		if len(self.lineEdit_username.text()) > 0 and len(self.lineEdit_password.text()) > 0:
			global id
			id = self.lineEdit_username.text()
			global pwd
			pwd = self.lineEdit_password.text()
			msg.setText('Success')
			msg.exec_()
			self.app.quit()
		else:
			msg.setText('Incorrect Password')
			msg.exec_()
def Show_pass():
	app = QApplication(sys.argv)
	form = LoginForm(app)
	form.show()
	app.exec_()
	app.quit()


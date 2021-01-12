"""
    CRM Login Window
    Authors: Gabriel Tomuta, Rares Horju
"""

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import time
import threading
import data.config as config


class LoginWindow(QWidget, config.Config):
    loginSuccessSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        uic.loadUi(r"..\ui\LoginInterface.ui", self)
        self.setWindowTitle("Login into CRM")

        # Widgets
        self.Qmain_login = self.findChild(QWidget, "Qmain_login")
        self.Qbutton_login = self.findChild(QPushButton, "Qbutton_login")
        self.Qbutton_login.setCheckable(True)
        self.Qtext_email = self.findChild(QLineEdit, "Qtext_email")
        self.Qtext_password = self.findChild(QLineEdit, "Qtext_password")

        self.Qtext_email.setPlaceholderText('Introduceti e-mail')
        self.Qtext_password.setPlaceholderText('Introduceti parola')
        self.Qtext_password.setEchoMode(QLineEdit.Password)

        # Signals
        self.Qbutton_login.clicked.connect(self.on_check_password)

        # Init
        self.Qtext_email.setFocus()

    # Methods ----------------------------------------------------------------------------------------------------------
    def redirect_to_main(self):
        self.MainWindow.show()
        self.hide()

    # Events -----------------------------------------------------------------------------------------------------------
    def keyPressEvent(self, event):
        if event.key() == 16777220:  # Enter
            if not self.Qtext_password.text():
                self.Qtext_password.setFocus()
            else:
                self.Qbutton_login.clicked.emit()
        elif event.key() == 16777235:  # Up_arrow
            self.Qtext_email.setFocus()
        elif event.key() == 16777237:  # Down_arrow
            self.Qtext_password.setFocus()

    # Slots ------------------------------------------------------------------------------------------------------------
    def on_check_password(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)

        if self.check_in_csv(self.Qtext_email.text(), self.Qtext_password.text()) is True:
            self.loginSuccessSignal.emit()
        else:
            self.Qtext_email.setText('')
            self.Qtext_password.setText('')
            msg.setWindowTitle("Eroare")
            msg.setText('E-mail sau parola incorecta')
            msg.exec_()

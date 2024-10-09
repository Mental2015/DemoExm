from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QDialog)
from PyQt5.uic import loadUi
import sys 
from PyQt5.QtGui import QPixmap, QIcon
import sqlite3


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi ('/home/kabinet303/DemExm/dialog.ui', self)
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton.clicked.connect(self.Vxod)
        
    def Vxod (self):
        print ("Прошло")
        user = self.LoginField.text()
        pwd = self.PasswordField.text()
        userinfo = [user, pwd]
        
        if user == "" or pwd == "":
            self.ErrorField.setText("Заполните поля")
        else:
            print (user, pwd)
            conn = sqlite3.connect("uchet.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM users where login = ? and password = ?", (user,pwd))
            #cur.execute("SELECT * from users where login = 'login1' and password = 'pass1'")
            typeuser = cur.fetchone()
            print(typeuser)
            conn.commit()
            conn.close()

app = QApplication(sys.argv)

welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)

icon = QIcon()
icon.addPixmap(QPixmap("nyam-nyam.png"),
QIcon.Normal, QIcon.Off)
widget.setWindowIcon(icon)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("You close application")    
#  widget - это имя, присваиваемое компоненту пользовательского интерфейса,
#  с которым пользователь может взаимодействовать 
from PyQt5 import QtWidgets
import sqlite3
from PyQt5.QtWidgets import (    
    QDialog # это базовый класс диалогового окна
)

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

# Окно приветствия
class WelcomeScreen(QDialog):
    """
    Это класс окна приветствия.
    """
    def __init__(self):
        """
        Это конструктор класса
        """
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui",self) # загружаем интерфейс
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.SignInButton.clicked.connect(self.signupfunction)
        self.SignOutButton.clicked.connect(self.sign_out)
        self.SignOutButton.hide()
        self.stackedWidget.currentChanged.connect(self.on_page_changed)

    def signupfunction(self):

        user = self.LoginField.text()
        password = self.PasswordField.text()
        print(user, password)

        if len(user)==0 or len(password)==0:
            self.ErrorField.setText("Заполните все поля")
        else:
            self.ErrorField.setText("Все ок")

        conn = sqlite3.connect("uchet.db")
        cur = conn.cursor()

        cur.execute('SELECT typeID FROM users WHERE login=(?) and password=(?)', [user, password]) # получаем тип пользователя, логин и пароль которого был введен
        typeUser = cur.fetchone() # получает только один тип пользователя
        if typeUser:
            print(typeUser[0]) # выводит тип пользователя без скобок       
            if typeUser[0] == 1:
                self.stackedWidget.setCurrentWidget(self.Manager)
                self.lybaya = Manager()
            elif typeUser[0] == 2:
                self.stackedWidget.setCurrentWidget(self.Master)
                self.lybaya = Master()
            elif typeUser[0] == 3:
                self.stackedWidget.setCurrentWidget(self.Operator)
                self.lybaya = Operator()
            elif typeUser[0] == 4:
                self.stackedWidget.setCurrentWidget(self.Zakazchik)
                self.lybaya = Zakazchik()

        else:
            self.ErrorField.setText("Неверный логин или пароль")                    

        conn.commit()

    def on_page_changed(self, index):
        if index == self.stackedWidget.indexOf(self.Avtorisation):
            self.SignOutButton.hide()
        else:
            self.SignOutButton.show()
    def sign_out(self):
        self.stackedWidget.setCurrentWidget(self.Avtorisation)

class Manager(QDialog):
    def __init__(self):        
        super(Manager, self).__init__()
        print("Manager")

class Master(QDialog):
    def __init__(self):        
        super(Master, self).__init__()
        print("Master")

class Operator(QDialog):
    def __init__(self):        
        super(Operator, self).__init__()
        print("Operator")

class Zakazchik(QDialog):
    def __init__(self):        
        super(Zakazchik, self).__init__()
        print("Zakazchik")
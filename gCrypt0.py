#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
import random
from PyQt5.QtWidgets import (QWidget, QLineEdit, QTextEdit, QGridLayout,  QDesktopWidget, QMainWindow, QLabel, QToolTip, QPushButton, QMessageBox, QApplication)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import (QFont, QIcon)
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('Times New Roman', 11))
        self.setToolTip('Это моя гениальная программа')
        grid = QGridLayout()
        grid.setSpacing(5)
        self.setLayout(grid)
        lbl1 = QLabel('Для зашифровки введите encr, для дешифровки - decr', self)
        lbl2 = QLabel('Не стирайте "1)" если хотите корректной работы программы', self)
        lne = QLineEdit('1) ', self)
        x = ''
        self.lbl3 = QLabel(x, self)
        lbl11 = QLabel('Введите пароль(если вы зашифровываете файл - для генерации случайного пароля введите random)', self)
        lbl21 = QLabel('Не стирайте "2)" если хотите корректной работы программы', self)
        lne1 = QLineEdit('2) ', self)
        x1 = ''
        self.lbl31 = QLineEdit(x1, self)
        lbl12 = QLabel('Введите файл для зашифровки/дешифровки', self)
        lbl22 = QLabel('Не стирайте "3)" если хотите корректной работы программы', self)
        lne2 = QLineEdit('3) ', self)
        x2 = ''
        self.lbl32 = QLabel(x2, self)
        lbl13 = QLabel('Введите файл назначения. Для значения по умолчанию введите def', self)
        lbl23 = QLabel('Не стирайте "4)" если хотите корректной работы программы', self)
        lne3 = QLineEdit('4) ', self)
        x3 = ''
        self.lbl33 = QLabel(x3, self)
        lbl14 = QLabel('Удалить исходный файл?(да/нет)', self)
        lbl24 = QLabel('Не стирайте "5)" если хотите корректной работы программы', self)
        lne4 = QLineEdit('5) ', self)
        x4 = ''
        self.lbl34 = QLabel(x4, self)
        defin = QLabel('Данная программа является графическим интерфейсом к моей программе Crypt0.', self)
        defin1 = QLabel('Если у Вас возникли какие-то вопросы, пишите на электронный адрес artur.bigulov@yandex.ru', self)
        btn = QPushButton("Шифровать!", self)
        btn.clicked.connect(self.buttonClicked)
        lne.textChanged[str].connect(self.onChanged)
        lne1.textChanged[str].connect(self.onChanged)
        lne2.textChanged[str].connect(self.onChanged)
        lne3.textChanged[str].connect(self.onChanged)
        lne4.textChanged[str].connect(self.onChanged)
        grid.addWidget(lbl1, 1, 1)
        grid.addWidget(lbl2, 2, 1)
        grid.addWidget(lne, 3, 1)
        grid.addWidget(self.lbl3, 4, 1)
        grid.addWidget(lbl11, 5, 1)
        grid.addWidget(lbl21, 6, 1)
        grid.addWidget(lne1, 7, 1)
        grid.addWidget(self.lbl31, 8, 1)
        grid.addWidget(lbl12, 9, 1)
        grid.addWidget(lbl22, 10, 1)
        grid.addWidget(lne2, 11, 1)
        grid.addWidget(self.lbl32, 12, 1)
        grid.addWidget(lbl13, 13, 1)
        grid.addWidget(lbl23, 14, 1)
        grid.addWidget(lne3, 15, 1)
        grid.addWidget(self.lbl33, 16, 1)
        grid.addWidget(lbl14, 17, 1)
        grid.addWidget(lbl24, 18, 1)
        grid.addWidget(lne4, 19, 1)
        grid.addWidget(self.lbl34, 20, 1)
        grid.addWidget(defin, 21, 1)
        grid.addWidget(defin1, 22, 1)
        grid.addWidget(btn, 23, 1)
        self.resize(500, 500)
        self.center()
        self.setWindowTitle('gCrypt0 0.9.9 alpha')
        self.setWindowIcon(QIcon('zamok.jpg'))
        self.show()
        self.en = ['q','w','e','r','t','y','u','i','o','p','[',']',
          'a','s','d','f','g','h','j','k','l',';',
          'z','x','c','v','b','n','m',',','.','/',  
          '1','2','3','4','5','6','7','8','9','0','=',
          '~','!','(',')','+',
          'Q','W','E','R','T','Y','U','I','O','P',
          'A','S','D','F','G','H','J','K','L',':',
          'Z','X','C','V','B','N','M',]
        self.de = ''
        self.password = ''
        self.infile = ''
        self.outfile = ''
        self.df = ''
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def buttonClicked(self):
        reply = QMessageBox.question(self, 'Encryption', "Вы уверены, что ввели все правильно?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if 'en' in self.de:
                if 'def' in self.outfile:
                    c = self.df
                    if 'Y' in c or 'y' in c or 'YES' in c or 'yes' in c or 'Д' in c or 'д' in c or 'ДА' in c or 'да' in c:
                        os.system('crypt0 -e -p '+self.password+' -if '+self.infile+' -df '+'-dd')
                    else:
                        os.system('crypt0 -e -p '+self.password+' -if '+self.infile+' -df')
                else:
                    c = self.df
                    if 'Y' in c or 'y' in c or 'YES' in c or 'yes' in c or 'Д' in c or 'д' in c or 'ДА' in c or 'да' in c:
                        os.system('crypt0 -e -p '+self.password+' -if '+self.infile+' -of '+self.outfile+' -dd')
                    else:
                        os.system('crypt0 -e -p '+self.password+' -if '+self.infile+' -of '+self.outfile)
            else:
                if 'def' in self.outfile:
                    c = self.df
                    if 'Y' in c or 'y' in c or 'YES' in c or 'yes' in c or 'Д' in c or 'д' in c or 'ДА' in c or 'да' in c:
                        os.system('crypt0 -d -p '+self.password+' -if '+self.infile+' -df '+'-dd')
                    else:
                        os.system('crypt0 -d -p '+self.password+' -if '+self.infile+' -df')
                else:
                    c = self.df
                    if 'Y' in c or 'y' in c or 'YES' in c or 'yes' in c or 'Д' in c or 'д' in c or 'ДА' in c or 'да' in c:
                        os.system('crypt0 -d -p '+self.password+' -if '+self.infile+' -of '+self.outfile+' -dd')
                    else:
                        os.system('crypt0 -d -p '+self.password+' -if '+self.infile+' -of '+self.outfile)
        else:
            pass
    def onChanged(self, text):
        sender = self.sender().text()[:2]
        if sender == '1)':
            self.lbl3.setText('Вы решили: '+text[2:])
            self.de = text[2:]
            if self.de != '':
                if self.de[0] == ' ':
                    self.de = self.de[1:]
        if sender == '2)':
            self.password = text[2:]
            if self.password != '':
                if self.password[0] == ' ':
                    self.password = self.password[1:]
                    self.lbl31.setText('Ваш пароль: '+text[2:])
                else:
                    self.lbl31.setText('Ваш пароль: '+text[2:])
                if self.password == 'random':
                    self.password = ''.join(random.sample(self.en, 12))
                    self.lbl31.setText('Ваш пароль(не забудьте скопировать!): '+self.password)
        if sender == '3)':
            self.lbl32.setText('Исходный файл: '+text[2:])
            self.infile = text[2:]
            if self.infile != '':
                if self.infile[0] == ' ':
                    self.infile = self.infile[1:]
        if sender == '4)':
            self.lbl33.setText('Итоговый файл: '+text[2:])
            self.outfile = text[2:]
            if self.outfile != '':
                if self.outfile[0] == ' ':
                    self.outfile = self.outfile[1:]
        if sender == '5)':
            self.lbl34.setText('Вы решили: '+text[2:])
            self.df = text[2:]
            if self.df != '':
                if self.df[0] == ' ':
                    self.df = self.df[1:]
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', "Вы точно хотите выйти?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

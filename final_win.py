from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *

class FinalWin(QWidget):
    def __init__(self):
        '''окно, в котором проводится опрос '''
        super().__init__()
        self.set_appear()# Устанавливает, как будет выглядить окно
        self.initUI()# Создаём и настраеваем графические элементы
        self.show()#Делает окно видимым
    def initUI(self):
        '''Создаёт графические элементы'''
        self.workh_text = QLabel(txt_workheart + self.results())
        self.index_text = QLable(txt_index + str(self.index))

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)

    ''' устанавливает, как будет выглядеть окно (надптсь, размер, место)'''
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def resuts(self):
        self.index=(4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index<15 and self.index>=11:
                return txt_res2
            elif self.index    

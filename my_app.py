from PyQt5.QtCore import Qt, QTime, QTimer, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont #проверка типов вводимых значений
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *


class MainWin(QWidget):
    def __init__(self):
        '''окно, в котором распологается приветствие'''
        super().__init__()
        self.set_appear()# Устанавливает, как будет выглядить окно
        self.initUI()# Создаём и настраеваем графические элементы
        self.connects()# Устанавливает связи между элементами
        self.show()#Делает окно видимым

    def initUI(self):
        # Описание элементов интерфейса
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.btn_next = QPushButton(txt_next, self)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def next_click(self):
        self.tw = TestWin()
        self.hide()
                
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    
    '''Устанавливает, как будет выглядеть окно (надпись, размер, место) '''    
    def set_appear(self):
        self.stWindowTitle(txt_title) 
        self.resize(win_whidth, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw = MainWin()
app.exec_() 
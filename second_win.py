from PyQt5.QtCore import Qt,, QTimer, QTime
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from final_win import *

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3  


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def timer_test(self):
        global time 
        time = QTime(0, 1, 0)
        self.time = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toSting("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Blod))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toSting("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer_sits(self):
        time = QTime(0, 0, 30)
        self.time = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
    def timer_final(self):
        time = QTime(0, 1, 0)
        self.timer.timout.connect(self.timer3Event)
    def timer3Event(self):
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8])  <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.line_age.text(),self.line_test1.text(),self.line_test2.text(),self.line_test3.text())
        self.tw = TestWin(self.exp)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)
        self.btn_test3.clicked.connect(self.timer_final)
    def set_appear(self):
        # Описание элементов интерфейса
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        '''Создаёт графические элементы'''
        #self.questionnary = AllQueshions()
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)    
        self.btn_test3 = QPushButton(txt_starttest3, self)
           
        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)

        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)

        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QVBoxLayout()
        self.r_line.addWidget(self.text_timer, aligment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, aligment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, aligment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_age, aligment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, aligment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1, aligment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, aligment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, aligment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2, aligment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, aligment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, aligment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3, aligment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, aligment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, aligment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next, aligment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
    
    def next_click(self):
        self.hide()
        self.fw = FinalWin()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def resuts(self):
        self.index=(4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10

    ''''''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    






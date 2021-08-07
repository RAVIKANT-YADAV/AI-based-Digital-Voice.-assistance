from datetime import time
from ANAS import Ui_ANAS 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QDateTime,Qt
from PyQt5.uic import loadUi
import wish as WS
import myquery 
import sys


class MainThread(QThread):
    def __init__(self): 
        super(MainThread,self).__init__()

    def run(self):
        WS.wish()
        myquery.myquery()

startFun = MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui =Ui_ANAS()
        self.gui.setupUi(self)

        self.gui.pushButtonStart.clicked.connect(self.startask)
       # self.gui.pushButtonStop_2.clicked.connect(self.exit)

    def startask(self):
        self.gui.l1=QtGui.QMovie("G.U.I Material-20210522T162824Z-001//G.U.I Material/B.G//Iron_Template_1.gif")
        self.gui.gfi_1.setMovie(self.gui.l1)
        self.gui.l1.start()

        self.gui.l2=QtGui.QMovie("G.U.I Material-20210522T162824Z-001//G.U.I Material/ExtraGui//live.gif")
        self.gui.gfi2.setMovie(self.gui.l2)
        self.gui.l2.start()

        self.gui.l3=QtGui.QMovie("G.U.I Material-20210522T162824Z-001/G.U.I Material/VoiceReg/__1.gif")
        self.gui.gif3.setMovie(self.gui.l3)
        self.gui.l3.start()

        self.gui.l4=QtGui.QMovie("G.U.I Material-20210522T162824Z-001/G.U.I Material/ExtraGui/Earth.gif")
        self.gui.gif4_2.setMovie(self.gui.l4)
        self.gui.l4.start()

        self.gui.l5=QtGui.QMovie("G.U.I Material-20210522T162824Z-001/G.U.I Material/ExtraGui/initial.gif")
        self.gui.gif5.setMovie(self.gui.l5)
        self.gui.l5.start()

        timer=QTimer(self)
        timer.timeout.connect(self.ShowTimelive)
        timer.start(990)

        
        startFun.start()

    def ShowTimelive(self):
       Time_ver=QTime.currentTime()
       time=Time_ver.toString()
       level_time="Time :"+str(time)
       date_ver=QDate.currentDate()
       date=date_ver.toString()
       level_date="date : "+str(date)

       self.gui.text_time.setText(level_time)
       self.gui.text_Date.setText(level_date)

guiApp = QApplication(sys.argv)
Anas_gui = Gui_Start()
Anas_gui.show()
exit(guiApp.exec_())




from PyQt5 import QtCore, QtGui, QtWidgets
import minimax

board = [
    [ '_', '_', '_' ], 
    [ '_', '_', '_' ], 
    [ '_', '_', '_' ] 
]    

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Noughts and Crosses")
        MainWindow.resize(829, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 80, 171, 141))
        self.pushButton.setText("")
        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(self.toggle1)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 80, 171, 141))
        self.pushButton_2.setText("")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.clicked.connect(self.toggle2)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 80, 171, 141))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.clicked.connect(self.toggle3)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 220, 171, 141))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.clicked.connect(self.toggle4)


        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 220, 171, 141))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.clicked.connect(self.toggle5)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 220, 171, 141))
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.clicked.connect(self.toggle6)

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(160, 360, 171, 141))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.clicked.connect(self.toggle7)

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(330, 360, 171, 141))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.clicked.connect(self.toggle8)

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 360, 171, 141))
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.clicked.connect(self.toggle9)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(55, 10, 721, 61))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def eval(self,b):
        if minimax.evaluate(b) == 10 or minimax.evaluate(b) == -10:
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(False)
            self.pushButton_4.setEnabled(False)
            self.pushButton_5.setEnabled(False)
            self.pushButton_6.setEnabled(False)
            self.pushButton_7.setEnabled(False)
            self.pushButton_8.setEnabled(False)
            self.pushButton_9.setEnabled(False)
            if minimax.evaluate(b) == -10:
                _translate = QtCore.QCoreApplication.translate
                self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:30pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:280px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">you win!</p></body></html>"))
            if minimax.evaluate(b) == 10:
                _translate = QtCore.QCoreApplication.translate
                self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:30pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:280px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">you lose!</p></body></html>"))
        counter = 0
        for i in range(3): 
            for j in range(3):
               if b[i][j] != "_":
                   counter += 1
        if counter == 9:
            _translate = QtCore.QCoreApplication.translate
            self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:30pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:305px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Draw!</p></body></html>"))
            

        else:
            pass
        
    

    def makeaturn(self,a):
        bestMove = minimax.findBestMove(a) 

        i = int(bestMove[0])
        j = int(bestMove[1])

        if i == 0 and j == 0:
            self.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap("nought.png")))
            self.pushButton.setIconSize(QtCore.QSize(160,160))
            self.pushButton.setEnabled(False)
        
        if i == 0 and j == 1:
            self.pushButton_2.setIcon(QtGui.QIcon(QtGui.QPixmap("nought.png")))
            self.pushButton_2.setIconSize(QtCore.QSize(160,160))
            self.pushButton_2.setEnabled(False)
        
        if i == 0 and j == 2:
            self.pushButton_3.setIcon(QtGui.QIcon(QtGui.QPixmap("nought.png")))
            self.pushButton_3.setIconSize(QtCore.QSize(160,160))
            self.pushButton_3.setEnabled(False)
        
        if i == 1 and j == 0:
            self.pushButton_4.setIcon(QtGui.QIcon(QtGui.QPixmap("nought.png")))
            self.pushButton_4.setIconSize(QtCore.QSize(160,160))
            self.pushButton_4.setEnabled(False)

        if i == 1 and j == 1:
            self.pushButton_5.setIcon(QtGui.QIcon(QtGui.QPixmap("nought.png")))
            self.pushButton_5.setIconSize(QtCore.QSize(160,160))
            self.pushButton_5.setEnabled(False)
        
        if i == 1 and j == 2:
            self.pushButton_6.setIcon(QtGui.QIcon(QtGui.QPixmap("nought.png")))
            self.pushButton_6.setIconSize(QtCore.QSize(160,160))
            self.pushButton_6.setEnabled(False)
        
        if i == 2 and j == 0:
            self.pushButton_7.setIcon(QtGui.QIcon(QtGui.QPixmap("nought.png")))
            self.pushButton_7.setIconSize(QtCore.QSize(160,160))
            self.pushButton_7.setEnabled(False)
        
        if i == 2 and j == 1:
            self.pushButton_8.setIcon(QtGui.QIcon(QtGui.QPixmap("nought.png")))
            self.pushButton_8.setIconSize(QtCore.QSize(160,160))
            self.pushButton_8.setEnabled(False)
        
        if i == 2 and j == 2:
            self.pushButton_9.setIcon(QtGui.QIcon(QtGui.QPixmap("nought.png")))
            self.pushButton_9.setIconSize(QtCore.QSize(160,160))
            self.pushButton_9.setEnabled(False)

        board[i][j] = "o"

       

    
    def toggle1(self):
        if self.pushButton.isChecked():
            self.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap("cross.png")))
            self.pushButton.setIconSize(QtCore.QSize(130,130))
            board[0][0] = "x"
            self.pushButton.setEnabled(False)

            self.makeaturn(board)
            self.eval(board)

       
        else:
            self.pushButton.setText("")

    def toggle2(self):
        if self.pushButton_2.isChecked():
            self.pushButton_2.setIcon(QtGui.QIcon(QtGui.QPixmap("cross.png")))
            self.pushButton_2.setIconSize(QtCore.QSize(130,130))
            board[0][1] = "x"
            self.pushButton_2.setEnabled(False)

            self.makeaturn(board)
            self.eval(board)

       
        else:
            self.pushButton_2.setText("")
    
    def toggle3(self):
        if self.pushButton_3.isChecked():
            self.pushButton_3.setIcon(QtGui.QIcon(QtGui.QPixmap("cross.png")))
            self.pushButton_3.setIconSize(QtCore.QSize(130,130))
            board[0][2] = "x"
            self.pushButton_3.setEnabled(False)

            self.makeaturn(board)
            self.eval(board)

       
        else:
            self.pushButton_3.setText("")
    
    def toggle4(self):
        if self.pushButton_4.isChecked():
            self.pushButton_4.setIcon(QtGui.QIcon(QtGui.QPixmap("cross.png")))
            self.pushButton_4.setIconSize(QtCore.QSize(130,130))
            board[1][0] = "x"
            self.pushButton_4.setEnabled(False)

            self.makeaturn(board)
            self.eval(board)

       
        else:
            self.pushButton_4.setText("")
    
    def toggle5(self):
        if self.pushButton_5.isChecked():
            self.pushButton_5.setIcon(QtGui.QIcon(QtGui.QPixmap("cross.png")))
            self.pushButton_5.setIconSize(QtCore.QSize(130,130))
            board[1][1] = "x"
            self.pushButton_5.setEnabled(False)

            self.makeaturn(board)
            self.eval(board)

       
        else:
            self.pushButton_5.setText("")
    
    def toggle6(self):
        if self.pushButton_6.isChecked():
            self.pushButton_6.setIcon(QtGui.QIcon(QtGui.QPixmap("cross.png")))
            self.pushButton_6.setIconSize(QtCore.QSize(130,130))
            board[1][2] = "x"
            self.pushButton_6.setEnabled(False)

            self.makeaturn(board)
            self.eval(board)

       
        else:
            self.pushButton_6.setText("")
    
    def toggle7(self):
        if self.pushButton_7.isChecked():
            self.pushButton_7.setIcon(QtGui.QIcon(QtGui.QPixmap("cross.png")))
            self.pushButton_7.setIconSize(QtCore.QSize(130,130))
            board[2][0] = "x"
            self.pushButton_7.setEnabled(False)

            self.makeaturn(board)
            self.eval(board)

       
        else:
            self.pushButton_7.setText("")
    
    def toggle8(self):
        if self.pushButton_8.isChecked():
            self.pushButton_8.setIcon(QtGui.QIcon(QtGui.QPixmap("cross.png")))
            self.pushButton_8.setIconSize(QtCore.QSize(130,130))
            board[2][1] = "x"
            self.pushButton_8.setEnabled(False)

            self.makeaturn(board)
            self.eval(board)

       
        else:
            self.pushButton_8.setText("")
    
    def toggle9(self):
        if self.pushButton_9.isChecked():
            self.pushButton_9.setIcon(QtGui.QIcon(QtGui.QPixmap("cross.png")))
            self.pushButton_9.setIconSize(QtCore.QSize(130,130))
            board[2][2] = "x"
            self.pushButton_9.setEnabled(False)

            self.makeaturn(board)
            self.eval(board)

       
        else:
            self.pushButton_9.setText("")
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Noughts and Crosses", "Noughts and Crosses"))
        self.textBrowser.setHtml(_translate("Noughts and Crosses", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:30pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:305px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PLAY!</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# +------------+--------------+-----------------------------------------------------------+
# |   Author   |     Date     |                         Changed                           |
# +------------+--------------+-----------------------------------------------------------+
# | Qt5 UI gen |  2022/09/29  | Auto-generated (from resources/dbmgr_pathselect.ui)       |
# +------------+--------------+-----------------------------------------------------------+


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 57)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.baseHori = QtWidgets.QHBoxLayout()
        self.baseHori.setObjectName("baseHori")
        self.pathEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.pathEdit.setFont(font)
        self.pathEdit.setObjectName("pathEdit")
        self.baseHori.addWidget(self.pathEdit)
        self.loadBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.loadBtn.setFont(font)
        self.loadBtn.setObjectName("loadBtn")
        self.baseHori.addWidget(self.loadBtn)
        self.horizontalLayout_2.addLayout(self.baseHori)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "온도미쁨 - 데이터베이스 관리 도구"))
        self.loadBtn.setText(_translate("MainWindow", "불러오기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

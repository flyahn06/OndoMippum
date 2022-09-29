# +------------+--------------+-----------------------------------------------------------+
# |   Author   |     Date     |                         Changed                           |
# +------------+--------------+-----------------------------------------------------------+
# |  Andrew A. |  2022/09/29  | Merged dbmgr_mainwindow.py and dbmgr_pathselect.py        |
# +------------+--------------+-----------------------------------------------------------+


from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, Qt
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import sys


class PathSelectWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")

        self.setWindowTitle("온도미쁨 - 데이터베이스 관리 도구")
        self.resize(821, 57)

        self.centralwidget = QWidget(self)
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)

        self.baseHori = QHBoxLayout()

        self.pathEdit = QLineEdit("/Users/flyahn06/code/OndoMippum/resources/main.db", self.centralwidget)
        self.pathEdit.setFont(font)
        self.baseHori.addWidget(self.pathEdit)

        self.loadBtn = QPushButton("불러오기", self.centralwidget)
        self.loadBtn.setFont(font)
        self.loadBtn.clicked.connect(self.loadDB)

        self.baseHori.addWidget(self.loadBtn)
        self.horizontalLayout_2.addLayout(self.baseHori)
        self.setCentralWidget(self.centralwidget)

        self.show()
        # TODO: For debugging
        self.loadDB()

    def loadDB(self):
        path = self.pathEdit.text()

        try:
            open(path, 'rb')
        except FileNotFoundError:
            return

        self.next = MainWindow()
        self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")

        self.resize(898, 578)
        self.centralwidget = QWidget(self)
        self.setWindowTitle("온도미쁨 - 데이터베이스 관리 도구")

        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.baseVert = QVBoxLayout()
        self.upperTimeSearchHori = QHBoxLayout()

        self.timeSearchEnableChkBox = QCheckBox("시간 검색", self.centralwidget)
        self.timeSearchEnableChkBox.setFont(font)
        self.timeSearchEnableChkBox.clicked.connect(self.enableTimeSearch)
        self.upperTimeSearchHori.addWidget(self.timeSearchEnableChkBox)

        self.timeSearchFromEdit = QDateTimeEdit(self.centralwidget)
        self.timeSearchFromEdit.setFont(font)
        self.timeSearchFromEdit.setEnabled(False)
        self.upperTimeSearchHori.addWidget(self.timeSearchFromEdit)

        self.timeSearchFromLbl = QLabel("부터", self.centralwidget)
        self.timeSearchFromLbl.setFont(font)
        self.timeSearchFromLbl.setEnabled(False)
        self.upperTimeSearchHori.addWidget(self.timeSearchFromLbl)

        self.timeSearchToEdit = QDateTimeEdit(self.centralwidget)
        self.timeSearchToEdit.setFont(font)
        self.timeSearchToEdit.setEnabled(False)
        self.upperTimeSearchHori.addWidget(self.timeSearchToEdit)

        self.timeSearchToLbl = QLabel("까지", self.centralwidget)
        self.timeSearchToLbl.setFont(font)
        self.timeSearchToLbl.setEnabled((False))
        self.upperTimeSearchHori.addWidget(self.timeSearchToLbl)
        self.baseVert.addLayout(self.upperTimeSearchHori)

        self.upperNameSearchHori = QHBoxLayout()

        self.nameSearchEdit = QLineEdit(self.centralwidget)
        self.nameSearchEdit.setFont(font)
        self.nameSearchEdit.setPlaceholderText("검색할 대상의 이름을 입력하세요. 입력하지 않으면 모두(*) 가져옵니다.")
        self.upperNameSearchHori.addWidget(self.nameSearchEdit)

        self.searchBtn = QPushButton("검색", self.centralwidget)
        self.searchBtn.setFont(font)
        self.upperNameSearchHori.addWidget(self.searchBtn)

        self.baseVert.addLayout(self.upperNameSearchHori)

        self.tableView = QTableView(self.centralwidget)
        self.baseVert.addWidget(self.tableView)

        self.lowerExportGraphHori = QHBoxLayout()

        self.graphBtn = QPushButton("그래프 보기", self.centralwidget)
        self.graphBtn.setFont(font)
        self.lowerExportGraphHori.addWidget(self.graphBtn)

        self.exportBtn = QPushButton("액셀 파일로 내보내기", self.centralwidget)
        self.exportBtn.setFont(font)
        self.lowerExportGraphHori.addWidget(self.exportBtn)

        self.baseVert.addLayout(self.lowerExportGraphHori)
        self.verticalLayout_2.addLayout(self.baseVert)
        self.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)

        self.show()

    def enableTimeSearch(self):
        if self.timeSearchEnableChkBox.isChecked():
            self.timeSearchFromLbl.setEnabled(True)
            self.timeSearchToLbl.setEnabled(True)
            self.timeSearchFromEdit.setEnabled(True)
            self.timeSearchToEdit.setEnabled(True)
        else:
            self.timeSearchFromLbl.setEnabled(False)
            self.timeSearchToLbl.setEnabled(False)
            self.timeSearchFromEdit.setEnabled(False)
            self.timeSearchToEdit.setEnabled(False)

app = QApplication(sys.argv)
pathselect = PathSelectWindow()
sys.exit(app.exec_())

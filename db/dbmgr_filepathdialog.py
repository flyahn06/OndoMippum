# +------------+--------------+-----------------------------------------------------------+
# |   Author   |     Date     |                         Changed                           |
# +------------+--------------+-----------------------------------------------------------+
# | Qt5 UI gen |  2022/09/29  | Auto-generated (from resources/dbmgr_mainwindow.ui)       |
# +------------+--------------+-----------------------------------------------------------+

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_filePathDialog(object):
    def setupUi(self, filePathDialog):
        filePathDialog.setObjectName("filePathDialog")
        filePathDialog.resize(635, 89)
        filePathDialog.setMinimumSize(QtCore.QSize(635, 89))
        filePathDialog.setMaximumSize(QtCore.QSize(10000, 89))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(filePathDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.base = QtWidgets.QVBoxLayout()
        self.base.setObjectName("base")
        self.base_in = QtWidgets.QHBoxLayout()
        self.base_in.setObjectName("base_in")
        self.filePathLbl = QtWidgets.QLabel(filePathDialog)
        font = QtGui.QFont()
        font.setFamily("Apple SD Gothic Neo")
        self.filePathLbl.setFont(font)
        self.filePathLbl.setObjectName("filePathLbl")
        self.base_in.addWidget(self.filePathLbl)
        self.filePathEdit = QtWidgets.QLineEdit(filePathDialog)
        self.filePathEdit.setObjectName("filePathEdit")
        self.base_in.addWidget(self.filePathEdit)
        self.base.addLayout(self.base_in)
        self.verticalLayout_2.addLayout(self.base)
        self.buttonBox = QtWidgets.QDialogButtonBox(filePathDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(filePathDialog)
        self.buttonBox.accepted.connect(filePathDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(filePathDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(filePathDialog)

    def retranslateUi(self, filePathDialog):
        _translate = QtCore.QCoreApplication.translate
        filePathDialog.setWindowTitle(_translate("filePathDialog", "온도미쁨 - 데이터베이스 관리 도구"))
        self.filePathLbl.setText(_translate("filePathDialog", "파일 경로"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    filePathDialog = QtWidgets.QDialog()
    ui = Ui_filePathDialog()
    ui.setupUi(filePathDialog)
    filePathDialog.show()
    sys.exit(app.exec_())

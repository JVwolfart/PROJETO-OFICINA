# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joao-vitor/Dropbox/JP 2021/PROJETO OFICINA/manutencao_usuarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(814, 615)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(62, 132, 238);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BtnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.BtnVoltar.setGeometry(QtCore.QRect(20, 20, 231, 51))
        self.BtnVoltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnVoltar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(245, 121, 0);\n"
"border-radius: 10px;")
        self.BtnVoltar.setObjectName("BtnVoltar")
        self.TabelaUsuarios = QtWidgets.QTableWidget(self.centralwidget)
        self.TabelaUsuarios.setEnabled(True)
        self.TabelaUsuarios.setGeometry(QtCore.QRect(10, 140, 781, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabelaUsuarios.sizePolicy().hasHeightForWidth())
        self.TabelaUsuarios.setSizePolicy(sizePolicy)
        self.TabelaUsuarios.setMinimumSize(QtCore.QSize(465, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TabelaUsuarios.setFont(font)
        self.TabelaUsuarios.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(138, 226, 52);")
        self.TabelaUsuarios.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.TabelaUsuarios.setObjectName("TabelaUsuarios")
        self.TabelaUsuarios.setColumnCount(5)
        self.TabelaUsuarios.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(17)
        item.setFont(font)
        self.TabelaUsuarios.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(17)
        item.setFont(font)
        self.TabelaUsuarios.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(17)
        item.setFont(font)
        self.TabelaUsuarios.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(17)
        item.setFont(font)
        self.TabelaUsuarios.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(17)
        item.setFont(font)
        self.TabelaUsuarios.setHorizontalHeaderItem(4, item)
        self.TabelaUsuarios.horizontalHeader().setDefaultSectionSize(150)
        self.TabelaUsuarios.horizontalHeader().setSortIndicatorShown(True)
        self.TabelaUsuarios.horizontalHeader().setStretchLastSection(True)
        self.lbl_status_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_status_2.setGeometry(QtCore.QRect(10, 90, 811, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lbl_status_2.setFont(font)
        self.lbl_status_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_status_2.setObjectName("lbl_status_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.TabelaUsuarios, self.BtnVoltar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Permiss??es a usu??rios"))
        self.BtnVoltar.setText(_translate("MainWindow", "Fechar"))
        item = self.TabelaUsuarios.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.TabelaUsuarios.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Criar"))
        item = self.TabelaUsuarios.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Editar"))
        item = self.TabelaUsuarios.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Excluir"))
        item = self.TabelaUsuarios.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Root"))
        self.lbl_status_2.setText(_translate("MainWindow", "D?? um duplo clique para editar as permiss??es."))

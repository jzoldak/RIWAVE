# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 1, 7, 17, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 2, 17, 1)
        self.actualValueComboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.actualValueComboBox.setFont(font)
        self.actualValueComboBox.setMaxVisibleItems(6)
        self.actualValueComboBox.setMaxCount(20)
        self.actualValueComboBox.setMinimumContentsLength(1)
        self.actualValueComboBox.setObjectName("actualValueComboBox")
        self.actualValueComboBox.addItem("")
        self.actualValueComboBox.addItem("")
        self.actualValueComboBox.addItem("")
        self.actualValueComboBox.addItem("")
        self.actualValueComboBox.addItem("")
        self.gridLayout_2.addWidget(self.actualValueComboBox, 15, 5, 1, 1)
        self.actualValueLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.actualValueLabel.setFont(font)
        self.actualValueLabel.setObjectName("actualValueLabel")
        self.gridLayout_2.addWidget(self.actualValueLabel, 13, 5, 1, 1)
        self.justSaveButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.justSaveButton.setFont(font)
        self.justSaveButton.setObjectName("justSaveButton")
        self.gridLayout_2.addWidget(self.justSaveButton, 16, 4, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.candidate0Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.candidate0Label.setFont(font)
        self.candidate0Label.setObjectName("candidate0Label")
        self.gridLayout.addWidget(self.candidate0Label, 0, 0, 1, 1)
        self.candidate3Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.candidate3Label.setFont(font)
        self.candidate3Label.setObjectName("candidate3Label")
        self.gridLayout.addWidget(self.candidate3Label, 2, 1, 1, 1)
        self.candidate1Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.candidate1Label.setFont(font)
        self.candidate1Label.setObjectName("candidate1Label")
        self.gridLayout.addWidget(self.candidate1Label, 0, 1, 1, 1)
        self.candidate2Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.candidate2Label.setFont(font)
        self.candidate2Label.setObjectName("candidate2Label")
        self.gridLayout.addWidget(self.candidate2Label, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 5, 4, 2, 3)
        self.saveAndNextButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.saveAndNextButton.setFont(font)
        self.saveAndNextButton.setObjectName("saveAndNextButton")
        self.gridLayout_2.addWidget(self.saveAndNextButton, 16, 5, 1, 1)
        self.contestantsSubSectionLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contestantsSubSectionLabel.sizePolicy().hasHeightForWidth())
        self.contestantsSubSectionLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.contestantsSubSectionLabel.setFont(font)
        self.contestantsSubSectionLabel.setAutoFillBackground(False)
        self.contestantsSubSectionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.contestantsSubSectionLabel.setObjectName("contestantsSubSectionLabel")
        self.gridLayout_2.addWidget(self.contestantsSubSectionLabel, 3, 4, 2, 2)
        self.auditTable = QtWidgets.QTableWidget(self.centralwidget)
        self.auditTable.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.auditTable.sizePolicy().hasHeightForWidth())
        self.auditTable.setSizePolicy(sizePolicy)
        self.auditTable.setMinimumSize(QtCore.QSize(80, 251))
        self.auditTable.setMaximumSize(QtCore.QSize(1000, 1000))
        self.auditTable.setBaseSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.auditTable.setFont(font)
        self.auditTable.setAutoFillBackground(False)
        self.auditTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.auditTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.auditTable.setAlternatingRowColors(True)
        self.auditTable.setIconSize(QtCore.QSize(0, 0))
        self.auditTable.setGridStyle(QtCore.Qt.SolidLine)
        self.auditTable.setWordWrap(True)
        self.auditTable.setRowCount(100)
        self.auditTable.setColumnCount(4)
        self.auditTable.setObjectName("auditTable")
        item = QtWidgets.QTableWidgetItem()
        self.auditTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.auditTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.auditTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.auditTable.setHorizontalHeaderItem(3, item)
        self.auditTable.horizontalHeader().setVisible(True)
        self.auditTable.horizontalHeader().setDefaultSectionSize(53)
        self.auditTable.verticalHeader().setVisible(False)
        self.auditTable.verticalHeader().setDefaultSectionSize(22)
        self.auditTable.verticalHeader().setMinimumSectionSize(11)
        self.gridLayout_2.addWidget(self.auditTable, 1, 1, 16, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 0, 0, 2, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 7, 4, 2, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.candidate0NameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.candidate0NameLabel.setFont(font)
        self.candidate0NameLabel.setObjectName("candidate0NameLabel")
        self.verticalLayout.addWidget(self.candidate0NameLabel)
        self.candidate1NameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.candidate1NameLabel.setFont(font)
        self.candidate1NameLabel.setObjectName("candidate1NameLabel")
        self.verticalLayout.addWidget(self.candidate1NameLabel)
        self.candidate2NameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.candidate2NameLabel.setFont(font)
        self.candidate2NameLabel.setObjectName("candidate2NameLabel")
        self.verticalLayout.addWidget(self.candidate2NameLabel)
        self.candidate3NameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.candidate3NameLabel.setFont(font)
        self.candidate3NameLabel.setObjectName("candidate3NameLabel")
        self.verticalLayout.addWidget(self.candidate3NameLabel)
        self.gridLayout_2.addLayout(self.verticalLayout, 9, 4, 2, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.candidate0Percentage = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.candidate0Percentage.setFont(font)
        self.candidate0Percentage.setObjectName("candidate0Percentage")
        self.verticalLayout_2.addWidget(self.candidate0Percentage)
        self.candidate1Percentage = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.candidate1Percentage.setFont(font)
        self.candidate1Percentage.setObjectName("candidate1Percentage")
        self.verticalLayout_2.addWidget(self.candidate1Percentage)
        self.candidate2Percentage = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.candidate2Percentage.setFont(font)
        self.candidate2Percentage.setObjectName("candidate2Percentage")
        self.verticalLayout_2.addWidget(self.candidate2Percentage)
        self.candidate3Percentage = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.candidate3Percentage.setFont(font)
        self.candidate3Percentage.setObjectName("candidate3Percentage")
        self.verticalLayout_2.addWidget(self.candidate3Percentage)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 9, 5, 2, 1)
        self.reportedValueLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.reportedValueLabel.setFont(font)
        self.reportedValueLabel.setObjectName("reportedValueLabel")
        self.gridLayout_2.addWidget(self.reportedValueLabel, 13, 4, 1, 1)
        self.auditedBallotLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.auditedBallotLabel.setFont(font)
        self.auditedBallotLabel.setObjectName("auditedBallotLabel")
        self.gridLayout_2.addWidget(self.auditedBallotLabel, 12, 4, 1, 1)
        self.auditedBallotValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.auditedBallotValue.setFont(font)
        self.auditedBallotValue.setObjectName("auditedBallotValue")
        self.gridLayout_2.addWidget(self.auditedBallotValue, 12, 5, 1, 1)
        self.currentBallotLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.currentBallotLabel.setFont(font)
        self.currentBallotLabel.setAutoFillBackground(True)
        self.currentBallotLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentBallotLabel.setObjectName("currentBallotLabel")
        self.gridLayout_2.addWidget(self.currentBallotLabel, 11, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 17, 1, 1, 1)
        self.exportButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.exportButton.setFont(font)
        self.exportButton.setObjectName("exportButton")
        self.gridLayout_2.addWidget(self.exportButton, 16, 10, 1, 2)
        self.mainPageSectionLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageSectionLabel.sizePolicy().hasHeightForWidth())
        self.mainPageSectionLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.mainPageSectionLabel.setFont(font)
        self.mainPageSectionLabel.setAutoFillBackground(True)
        self.mainPageSectionLabel.setIndent(20)
        self.mainPageSectionLabel.setObjectName("mainPageSectionLabel")
        self.gridLayout_2.addWidget(self.mainPageSectionLabel, 0, 1, 1, 12)
        self.electionDetailsSectionLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.electionDetailsSectionLabel.setFont(font)
        self.electionDetailsSectionLabel.setAutoFillBackground(True)
        self.electionDetailsSectionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.electionDetailsSectionLabel.setIndent(0)
        self.electionDetailsSectionLabel.setObjectName("electionDetailsSectionLabel")
        self.gridLayout_2.addWidget(self.electionDetailsSectionLabel, 1, 3, 2, 4)
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.statusLabel.setFont(font)
        self.statusLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.statusLabel.setIndent(0)
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout_2.addWidget(self.statusLabel, 5, 10, 1, 2)
        self.auditDetailsLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.auditDetailsLabel.setFont(font)
        self.auditDetailsLabel.setAutoFillBackground(True)
        self.auditDetailsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.auditDetailsLabel.setObjectName("auditDetailsLabel")
        self.gridLayout_2.addWidget(self.auditDetailsLabel, 9, 10, 1, 1)
        self.toleranceValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.toleranceValue.setFont(font)
        self.toleranceValue.setObjectName("toleranceValue")
        self.gridLayout_2.addWidget(self.toleranceValue, 11, 11, 1, 1)
        self.specialValueValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.specialValueValue.setFont(font)
        self.specialValueValue.setObjectName("specialValueValue")
        self.gridLayout_2.addWidget(self.specialValueValue, 12, 11, 1, 1)
        self.recomputeButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.recomputeButton.setFont(font)
        self.recomputeButton.setObjectName("recomputeButton")
        self.gridLayout_2.addWidget(self.recomputeButton, 15, 10, 1, 2)
        self.toleranceLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.toleranceLabel.setFont(font)
        self.toleranceLabel.setObjectName("toleranceLabel")
        self.gridLayout_2.addWidget(self.toleranceLabel, 11, 10, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 10, 10, 1, 1)
        self.actualValueComboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.actualValueComboBox_2.setFont(font)
        self.actualValueComboBox_2.setMaxVisibleItems(6)
        self.actualValueComboBox_2.setMaxCount(20)
        self.actualValueComboBox_2.setMinimumContentsLength(1)
        self.actualValueComboBox_2.setObjectName("actualValueComboBox_2")
        self.actualValueComboBox_2.addItem("")
        self.actualValueComboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.actualValueComboBox_2, 10, 11, 1, 1)
        self.specialValueLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.specialValueLabel.setFont(font)
        self.specialValueLabel.setObjectName("specialValueLabel")
        self.gridLayout_2.addWidget(self.specialValueLabel, 12, 10, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 7, 10, 1, 2)
        self.tLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.tLabel.setFont(font)
        self.tLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tLabel.setIndent(0)
        self.tLabel.setObjectName("tLabel")
        self.gridLayout_2.addWidget(self.tLabel, 3, 10, 1, 1)
        self.tValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.tValue.setFont(font)
        self.tValue.setIndent(0)
        self.tValue.setObjectName("tValue")
        self.gridLayout_2.addWidget(self.tValue, 3, 11, 1, 1)
        self.reportedValueComboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.reportedValueComboBox.setFont(font)
        self.reportedValueComboBox.setObjectName("reportedValueComboBox")
        self.reportedValueComboBox.addItem("")
        self.reportedValueComboBox.addItem("")
        self.reportedValueComboBox.addItem("")
        self.reportedValueComboBox.addItem("")
        self.reportedValueComboBox.addItem("")
        self.gridLayout_2.addWidget(self.reportedValueComboBox, 15, 4, 1, 1)
        self.auditTable.raise_()
        self.mainPageSectionLabel.raise_()
        self.electionDetailsSectionLabel.raise_()
        self.contestantsSubSectionLabel.raise_()
        self.label_4.raise_()
        self.line_5.raise_()
        self.pushButton.raise_()
        self.currentBallotLabel.raise_()
        self.auditedBallotLabel.raise_()
        self.auditedBallotValue.raise_()
        self.reportedValueLabel.raise_()
        self.actualValueLabel.raise_()
        self.justSaveButton.raise_()
        self.actualValueComboBox.raise_()
        self.saveAndNextButton.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.exportButton.raise_()
        self.recomputeButton.raise_()
        self.specialValueLabel.raise_()
        self.specialValueValue.raise_()
        self.toleranceValue.raise_()
        self.toleranceLabel.raise_()
        self.label_5.raise_()
        self.actualValueComboBox_2.raise_()
        self.auditDetailsLabel.raise_()
        self.line_3.raise_()
        self.tLabel.raise_()
        self.tValue.raise_()
        self.statusLabel.raise_()
        self.reportedValueComboBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.actualValueComboBox.setCurrentIndex(0)
        self.actualValueComboBox_2.setCurrentIndex(0)
        self.reportedValueComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.actualValueComboBox.setCurrentText(_translate("MainWindow", "Select Candidate"))
        self.actualValueComboBox.setItemText(0, _translate("MainWindow", "Select Candidate"))
        self.actualValueComboBox.setItemText(1, _translate("MainWindow", "Trump"))
        self.actualValueComboBox.setItemText(2, _translate("MainWindow", "Clinton"))
        self.actualValueComboBox.setItemText(3, _translate("MainWindow", "Johnson"))
        self.actualValueComboBox.setItemText(4, _translate("MainWindow", "Stein"))
        self.actualValueLabel.setText(_translate("MainWindow", "Actual Value"))
        self.justSaveButton.setText(_translate("MainWindow", "Save Changes"))
        self.candidate0Label.setText(_translate("MainWindow", "0 - Trump"))
        self.candidate3Label.setText(_translate("MainWindow", "3 - Stein"))
        self.candidate1Label.setText(_translate("MainWindow", "1 - Clinton"))
        self.candidate2Label.setText(_translate("MainWindow", "2 - Johnson"))
        self.saveAndNextButton.setText(_translate("MainWindow", "Save and Continue"))
        self.contestantsSubSectionLabel.setText(_translate("MainWindow", "Contestants:"))
        item = self.auditTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Audit #"))
        item = self.auditTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Actual Ballot #"))
        item = self.auditTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Reported Value"))
        item = self.auditTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Actual Value"))
        self.label_4.setText(_translate("MainWindow", "Reported Results"))
        self.candidate0NameLabel.setText(_translate("MainWindow", "Trump"))
        self.candidate1NameLabel.setText(_translate("MainWindow", "Clinton "))
        self.candidate2NameLabel.setText(_translate("MainWindow", "Johnson"))
        self.candidate3NameLabel.setText(_translate("MainWindow", "Stein"))
        self.candidate0Percentage.setText(_translate("MainWindow", "25%"))
        self.candidate1Percentage.setText(_translate("MainWindow", "25%"))
        self.candidate2Percentage.setText(_translate("MainWindow", "25%"))
        self.candidate3Percentage.setText(_translate("MainWindow", "25%"))
        self.reportedValueLabel.setText(_translate("MainWindow", "Reported Value"))
        self.auditedBallotLabel.setText(_translate("MainWindow", "Audited Ballot #"))
        self.auditedBallotValue.setText(_translate("MainWindow", "1"))
        self.currentBallotLabel.setText(_translate("MainWindow", "Current Ballot"))
        self.pushButton.setText(_translate("MainWindow", "Edit Election"))
        self.exportButton.setText(_translate("MainWindow", "Export Results"))
        self.mainPageSectionLabel.setText(_translate("MainWindow", "RI WAVE - AUDIT"))
        self.electionDetailsSectionLabel.setText(_translate("MainWindow", "Election Details"))
        self.statusLabel.setText(_translate("MainWindow", "Status: OK"))
        self.auditDetailsLabel.setText(_translate("MainWindow", "Audit Details"))
        self.toleranceValue.setText(_translate("MainWindow", "10%"))
        self.specialValueValue.setText(_translate("MainWindow", "0.1"))
        self.recomputeButton.setText(_translate("MainWindow", "Recompute"))
        self.toleranceLabel.setText(_translate("MainWindow", "Tolerance:"))
        self.label_5.setText(_translate("MainWindow", "Type:"))
        self.actualValueComboBox_2.setCurrentText(_translate("MainWindow", "Risk-limiting"))
        self.actualValueComboBox_2.setItemText(0, _translate("MainWindow", "Risk-limiting"))
        self.actualValueComboBox_2.setItemText(1, _translate("MainWindow", "Bayesian"))
        self.specialValueLabel.setText(_translate("MainWindow", "Risk-limit:"))
        self.tLabel.setText(_translate("MainWindow", "T= "))
        self.tValue.setText(_translate("MainWindow", "8.99"))
        self.reportedValueComboBox.setCurrentText(_translate("MainWindow", "Select Candidate"))
        self.reportedValueComboBox.setItemText(0, _translate("MainWindow", "Select Candidate"))
        self.reportedValueComboBox.setItemText(1, _translate("MainWindow", "Trump"))
        self.reportedValueComboBox.setItemText(2, _translate("MainWindow", "Clinton"))
        self.reportedValueComboBox.setItemText(3, _translate("MainWindow", "Johnson"))
        self.reportedValueComboBox.setItemText(4, _translate("MainWindow", "Stein"))

    def getSpecialValueLabel(self):
        return self.specialValueLabel;

    def getAuditTable(self):
        return self.auditTable;

    def getCandidateGridLayout(self):
        return self.gridLayout;

    def getCandidateNameReportedResultsVeriticalLayout(self):
        return self.verticalLayout;

    def getCandidateValueReportedResultsVerticalLayout(self):
        return self.gridLayout_2;

    def getAuditedBallotValue(self):
        return self.auditedBallotValue;

    def getBallotReportedValueName(self):
        return self.reportedValueName;

    def getBallotActualValueComboBox(self):
        return self.actualValueComboBox;

    def getBallotActualValueComboBoxIndex(self):
        return self.actualValueComboBox.currentIndex();

    def getEditElectionButton(self):
        return self.pushButton;

    def getJustSaveChangesButton(self):
        return self.justSaveButton;

    def getSaveChangesAndContinueButton(self):
        return self.saveAndNextButton;

    def getRecomputeButton(self):
        return self.recomputeButton;

    def getExportResultsButton(self):
        return self.exportButton;

    def getToleranceLabel(self):
        return self.toleranceLabel;

    def getToleranceValueLabel(self):
        return self.toleranceValue;

    def getSpecialValueLabel(self):
        return self.specialValueLabel;

    def getSpecialValueValue(self):
        return self.specialValueValue;

    def getAuditTypeComboBox(self):
        return self.actualValueComboBox_2;

    def getAuditTypeComboBoxSelectedIndex(self):
        return str(self.actualValueComboBox_2.currentIndex());

    def getStatusLabel(self):
        return self.statusLabel;

    def getTValueValueLabel(self):
        return self.tValue;

    def getTLabelLabel(self):
        return self.tLabel;

    def setTableCell(self,row,col,value):
        self.auditTable.setItem(row, col, QtWidgets.QTableWidgetItem(value))







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    sys.exit(app.exec_())




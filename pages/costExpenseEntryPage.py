# Form implementation generated from reading ui file 'pages/costExpenseEntryPage.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_costExpenseMain(object):
    def setupUi(self, costExpenseMain):
        costExpenseMain.setObjectName("costExpenseMain")
        costExpenseMain.resize(944, 650)
        costExpenseMain.setStyleSheet("*{\n"
"  text-align: left;\n"
"}\n"
"QLineEdit, QComboBox{\n"
"border-radius:10px;\n"
"border:1px solid #B8B8B8;\n"
"padding:2px;\n"
"}\n"
"QPushButton{\n"
"background-color:#150E0A;\n"
"color:white;\n"
"padding:3px 12px 0px 8px;\n"
"border-radius:9px;\n"
"text-align:center;\n"
"}\n"
"QDateEdit{\n"
"border:1px solid #B8B8B8;\n"
"border-radius:5px;\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(costExpenseMain)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.costExpenseHeader = QtWidgets.QWidget(parent=costExpenseMain)
        self.costExpenseHeader.setMinimumSize(QtCore.QSize(0, 60))
        self.costExpenseHeader.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.costExpenseHeader.setFont(font)
        self.costExpenseHeader.setObjectName("costExpenseHeader")
        self.costExpenseHeader_Layout = QtWidgets.QHBoxLayout(self.costExpenseHeader)
        self.costExpenseHeader_Layout.setContentsMargins(0, 0, 0, 0)
        self.costExpenseHeader_Layout.setSpacing(0)
        self.costExpenseHeader_Layout.setObjectName("costExpenseHeader_Layout")
        self.accountNameFrame = QtWidgets.QFrame(parent=self.costExpenseHeader)
        self.accountNameFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.accountNameFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.accountNameFrame.setFont(font)
        self.accountNameFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.accountNameFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.accountNameFrame.setObjectName("accountNameFrame")
        self.accountNameFrame_layout = QtWidgets.QVBoxLayout(self.accountNameFrame)
        self.accountNameFrame_layout.setContentsMargins(0, 0, 10, 0)
        self.accountNameFrame_layout.setSpacing(0)
        self.accountNameFrame_layout.setObjectName("accountNameFrame_layout")
        self.accountNameLabel = QtWidgets.QLabel(parent=self.accountNameFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.accountNameLabel.setFont(font)
        self.accountNameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.accountNameLabel.setObjectName("accountNameLabel")
        self.accountNameFrame_layout.addWidget(self.accountNameLabel)
        self.accountNameSelect = QtWidgets.QComboBox(parent=self.accountNameFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.accountNameSelect.setFont(font)
        self.accountNameSelect.setObjectName("accountNameSelect")
        self.accountNameSelect.addItem("")
        self.accountNameSelect.addItem("")
        self.accountNameSelect.addItem("")
        self.accountNameSelect.addItem("")
        self.accountNameFrame_layout.addWidget(self.accountNameSelect)
        self.costExpenseHeader_Layout.addWidget(self.accountNameFrame)
        self.startDateFrame = QtWidgets.QFrame(parent=self.costExpenseHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startDateFrame.sizePolicy().hasHeightForWidth())
        self.startDateFrame.setSizePolicy(sizePolicy)
        self.startDateFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.startDateFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.startDateFrame.setFont(font)
        self.startDateFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.startDateFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.startDateFrame.setObjectName("startDateFrame")
        self.startDateFrame_Layout = QtWidgets.QVBoxLayout(self.startDateFrame)
        self.startDateFrame_Layout.setContentsMargins(10, 0, 10, 0)
        self.startDateFrame_Layout.setSpacing(0)
        self.startDateFrame_Layout.setObjectName("startDateFrame_Layout")
        self.startDateLabel = QtWidgets.QLabel(parent=self.startDateFrame)
        self.startDateLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.startDateLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.startDateLabel.setFont(font)
        self.startDateLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.startDateLabel.setObjectName("startDateLabel")
        self.startDateFrame_Layout.addWidget(self.startDateLabel)
        self.startDateInput = QtWidgets.QDateEdit(parent=self.startDateFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.startDateInput.setFont(font)
        self.startDateInput.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.startDateInput.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.startDateInput.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.startDateInput.setCalendarPopup(True)
        self.startDateInput.setDate(QtCore.QDate(2025, 1, 1))
        self.startDateInput.setObjectName("startDateInput")
        self.startDateFrame_Layout.addWidget(self.startDateInput)
        self.costExpenseHeader_Layout.addWidget(self.startDateFrame)
        self.endDateFrame = QtWidgets.QFrame(parent=self.costExpenseHeader)
        self.endDateFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.endDateFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.endDateFrame.setFont(font)
        self.endDateFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.endDateFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.endDateFrame.setObjectName("endDateFrame")
        self.endDateFrame_Layout = QtWidgets.QVBoxLayout(self.endDateFrame)
        self.endDateFrame_Layout.setContentsMargins(10, 0, 10, 0)
        self.endDateFrame_Layout.setSpacing(0)
        self.endDateFrame_Layout.setObjectName("endDateFrame_Layout")
        self.endDateLabel = QtWidgets.QLabel(parent=self.endDateFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.endDateLabel.setFont(font)
        self.endDateLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.endDateLabel.setObjectName("endDateLabel")
        self.endDateFrame_Layout.addWidget(self.endDateLabel)
        self.endDateInput = QtWidgets.QDateEdit(parent=self.endDateFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.endDateInput.setFont(font)
        self.endDateInput.setCalendarPopup(True)
        self.endDateInput.setDate(QtCore.QDate(2025, 1, 1))
        self.endDateInput.setObjectName("endDateInput")
        self.endDateFrame_Layout.addWidget(self.endDateInput)
        self.costExpenseHeader_Layout.addWidget(self.endDateFrame)
        self.filterActionFrame = QtWidgets.QFrame(parent=self.costExpenseHeader)
        self.filterActionFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.filterActionFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.filterActionFrame.setFont(font)
        self.filterActionFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.filterActionFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.filterActionFrame.setObjectName("filterActionFrame")
        self.filterActionFrame_Layout = QtWidgets.QVBoxLayout(self.filterActionFrame)
        self.filterActionFrame_Layout.setContentsMargins(10, 0, 10, 0)
        self.filterActionFrame_Layout.setSpacing(0)
        self.filterActionFrame_Layout.setObjectName("filterActionFrame_Layout")
        self.filterLabel = QtWidgets.QLabel(parent=self.filterActionFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.filterLabel.setFont(font)
        self.filterLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.filterLabel.setObjectName("filterLabel")
        self.filterActionFrame_Layout.addWidget(self.filterLabel)
        self.filterBtn = QtWidgets.QPushButton(parent=self.filterActionFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.filterBtn.setFont(font)
        self.filterBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.filterBtn.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/filter.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.filterBtn.setIcon(icon)
        self.filterBtn.setObjectName("filterBtn")
        self.filterActionFrame_Layout.addWidget(self.filterBtn)
        self.costExpenseHeader_Layout.addWidget(self.filterActionFrame)
        self.costExpenseEntryframe = QtWidgets.QFrame(parent=self.costExpenseHeader)
        self.costExpenseEntryframe.setMinimumSize(QtCore.QSize(0, 0))
        self.costExpenseEntryframe.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.costExpenseEntryframe.setFont(font)
        self.costExpenseEntryframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.costExpenseEntryframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.costExpenseEntryframe.setObjectName("costExpenseEntryframe")
        self.costExpenseEntryframe_Layout = QtWidgets.QVBoxLayout(self.costExpenseEntryframe)
        self.costExpenseEntryframe_Layout.setContentsMargins(10, 0, 0, 0)
        self.costExpenseEntryframe_Layout.setSpacing(0)
        self.costExpenseEntryframe_Layout.setObjectName("costExpenseEntryframe_Layout")
        self.costExpenseEntryLabel = QtWidgets.QLabel(parent=self.costExpenseEntryframe)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.costExpenseEntryLabel.setFont(font)
        self.costExpenseEntryLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.costExpenseEntryLabel.setObjectName("costExpenseEntryLabel")
        self.costExpenseEntryframe_Layout.addWidget(self.costExpenseEntryLabel)
        self.costExpenseEntryBtn = QtWidgets.QPushButton(parent=self.costExpenseEntryframe)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.costExpenseEntryBtn.setFont(font)
        self.costExpenseEntryBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.costExpenseEntryBtn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/edit-3.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.costExpenseEntryBtn.setIcon(icon1)
        self.costExpenseEntryBtn.setObjectName("costExpenseEntryBtn")
        self.costExpenseEntryframe_Layout.addWidget(self.costExpenseEntryBtn)
        self.costExpenseHeader_Layout.addWidget(self.costExpenseEntryframe)
        self.verticalLayout.addWidget(self.costExpenseHeader)
        self.costExpenseBody = QtWidgets.QWidget(parent=costExpenseMain)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.costExpenseBody.setFont(font)
        self.costExpenseBody.setObjectName("costExpenseBody")
        self.cashReportBody_Layout = QtWidgets.QHBoxLayout(self.costExpenseBody)
        self.cashReportBody_Layout.setContentsMargins(0, 10, 0, 0)
        self.cashReportBody_Layout.setSpacing(0)
        self.cashReportBody_Layout.setObjectName("cashReportBody_Layout")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.costExpenseBody)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QHeaderView::section, QHeaderView{\n"
"    background-color: #2D221B;\n"
"    color: white;   \n"
"    font-size: 12pt;  \n"
"    text-align: center; \n"
"}\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(160)
        self.cashReportBody_Layout.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.costExpenseBody)
        self.costExpenseBottom = QtWidgets.QWidget(parent=costExpenseMain)
        self.costExpenseBottom.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.costExpenseBottom.setFont(font)
        self.costExpenseBottom.setStyleSheet("#creditAmount, #debitAmount, #revenueAmount{\n"
"background:white;\n"
"color:black;\n"
"border-radius:10px;\n"
"border:1px solid #828282;\n"
"}")
        self.costExpenseBottom.setObjectName("costExpenseBottom")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.costExpenseBottom)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.debitLabel = QtWidgets.QLabel(parent=self.costExpenseBottom)
        self.debitLabel.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.debitLabel.setFont(font)
        self.debitLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.debitLabel.setObjectName("debitLabel")
        self.horizontalLayout.addWidget(self.debitLabel)
        self.debitAmount = QtWidgets.QLabel(parent=self.costExpenseBottom)
        self.debitAmount.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.debitAmount.setFont(font)
        self.debitAmount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.debitAmount.setObjectName("debitAmount")
        self.horizontalLayout.addWidget(self.debitAmount)
        self.creditLabel = QtWidgets.QLabel(parent=self.costExpenseBottom)
        self.creditLabel.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.creditLabel.setFont(font)
        self.creditLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.creditLabel.setObjectName("creditLabel")
        self.horizontalLayout.addWidget(self.creditLabel)
        self.creditAmount = QtWidgets.QLabel(parent=self.costExpenseBottom)
        self.creditAmount.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.creditAmount.setFont(font)
        self.creditAmount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.creditAmount.setObjectName("creditAmount")
        self.horizontalLayout.addWidget(self.creditAmount)
        self.revenueLabel = QtWidgets.QLabel(parent=self.costExpenseBottom)
        self.revenueLabel.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.revenueLabel.setFont(font)
        self.revenueLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.revenueLabel.setObjectName("revenueLabel")
        self.horizontalLayout.addWidget(self.revenueLabel)
        self.revenueAmount = QtWidgets.QLabel(parent=self.costExpenseBottom)
        self.revenueAmount.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.revenueAmount.setFont(font)
        self.revenueAmount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.revenueAmount.setObjectName("revenueAmount")
        self.horizontalLayout.addWidget(self.revenueAmount)
        self.verticalLayout.addWidget(self.costExpenseBottom)
        self.costExpenseFooter = QtWidgets.QWidget(parent=costExpenseMain)
        self.costExpenseFooter.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.costExpenseFooter.setFont(font)
        self.costExpenseFooter.setObjectName("costExpenseFooter")
        self.cashReportFooter_Layout = QtWidgets.QHBoxLayout(self.costExpenseFooter)
        self.cashReportFooter_Layout.setContentsMargins(0, 20, 0, 25)
        self.cashReportFooter_Layout.setSpacing(0)
        self.cashReportFooter_Layout.setObjectName("cashReportFooter_Layout")
        self.saveBtn = QtWidgets.QPushButton(parent=self.costExpenseFooter)
        self.saveBtn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.saveBtn.setFont(font)
        self.saveBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.saveBtn.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/save.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.saveBtn.setIcon(icon2)
        self.saveBtn.setIconSize(QtCore.QSize(22, 22))
        self.saveBtn.setCheckable(True)
        self.saveBtn.setAutoExclusive(True)
        self.saveBtn.setObjectName("saveBtn")
        self.cashReportFooter_Layout.addWidget(self.saveBtn, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.printBtn = QtWidgets.QPushButton(parent=self.costExpenseFooter)
        self.printBtn.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.printBtn.setFont(font)
        self.printBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.printBtn.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./icons/printer.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.printBtn.setIcon(icon3)
        self.printBtn.setIconSize(QtCore.QSize(22, 22))
        self.printBtn.setCheckable(True)
        self.printBtn.setAutoExclusive(True)
        self.printBtn.setObjectName("printBtn")
        self.cashReportFooter_Layout.addWidget(self.printBtn, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout.addWidget(self.costExpenseFooter)

        self.retranslateUi(costExpenseMain)
        QtCore.QMetaObject.connectSlotsByName(costExpenseMain)

    def retranslateUi(self, costExpenseMain):
        _translate = QtCore.QCoreApplication.translate
        costExpenseMain.setWindowTitle(_translate("costExpenseMain", "Form"))
        self.accountNameLabel.setText(_translate("costExpenseMain", "হিসাবের নাম"))
        self.accountNameSelect.setItemText(0, _translate("costExpenseMain", "সব হিসাব"))
        self.accountNameSelect.setItemText(1, _translate("costExpenseMain", "বিক্রেতা কে প্রদান"))
        self.accountNameSelect.setItemText(2, _translate("costExpenseMain", "ক্রেতা থেকে গ্রহণ"))
        self.accountNameSelect.setItemText(3, _translate("costExpenseMain", "অন্যান্য খরচ"))
        self.startDateLabel.setText(_translate("costExpenseMain", "তারিখ"))
        self.startDateInput.setDisplayFormat(_translate("costExpenseMain", "dd/mm/yyyy"))
        self.endDateLabel.setText(_translate("costExpenseMain", "শেষ তারিখ"))
        self.endDateInput.setDisplayFormat(_translate("costExpenseMain", "dd/mm/yyyy"))
        self.filterLabel.setText(_translate("costExpenseMain", "অ্যাকশন"))
        self.filterBtn.setText(_translate("costExpenseMain", "ফিল্টার"))
        self.costExpenseEntryLabel.setText(_translate("costExpenseMain", "আয় ব্যয় এন্ট্রি"))
        self.costExpenseEntryBtn.setText(_translate("costExpenseMain", "এন্ট্রি করুন"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("costExpenseMain", "তারিখ "))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("costExpenseMain", "হিসাবের নাম"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("costExpenseMain", "ক্রেতা - বিক্রেতার নাম"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("costExpenseMain", "খরচের নাম"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("costExpenseMain", "পরিমান "))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("costExpenseMain", "এন্ট্রি বাই"))
        self.debitLabel.setText(_translate("costExpenseMain", "মোট আয় :"))
        self.debitAmount.setText(_translate("costExpenseMain", "500000"))
        self.creditLabel.setText(_translate("costExpenseMain", "মোট ব্যয় :"))
        self.creditAmount.setText(_translate("costExpenseMain", "100000"))
        self.revenueLabel.setText(_translate("costExpenseMain", "মোট  আয়  :"))
        self.revenueAmount.setText(_translate("costExpenseMain", "100000"))
        self.saveBtn.setText(_translate("costExpenseMain", "সেভ এক্সেল"))
        self.printBtn.setText(_translate("costExpenseMain", "প্রিন্ট"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    costExpenseMain = QtWidgets.QWidget()
    ui = Ui_costExpenseMain()
    ui.setupUi(costExpenseMain)
    costExpenseMain.show()
    sys.exit(app.exec())
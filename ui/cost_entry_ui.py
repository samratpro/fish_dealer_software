# Form implementation generated from reading ui file 'ui_files/cost_entry.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CostEntry(object):
    def setupUi(self, CostEntry):
        CostEntry.setObjectName("CostEntry")
        CostEntry.resize(487, 577)
        CostEntry.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        CostEntry.setStyleSheet("QLineEdit, QDateEdit{ border-radius:10px;\n"
"border:1px solid #B8B8B8;\n"
" padding:3px;}\n"
"QPushButton{background-color:#2D221B;\n"
"                                        color:white;\n"
"                                        padding:5px 12px;\n"
"                                        border-radius:9px;}\n"
" QComboBox{border-radius:10px;background:#E1E1E1;border:1px solid #B8B8B8; padding:3px;}")
        self.layoutWidget = QtWidgets.QWidget(parent=CostEntry)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 470, 271, 68))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cancelBtn = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName("cancelBtn")
        self.gridLayout_2.addWidget(self.cancelBtn, 0, 1, 1, 1)
        self.addBtn = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.addBtn.setFont(font)
        self.addBtn.setObjectName("addBtn")
        self.gridLayout_2.addWidget(self.addBtn, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(parent=CostEntry)
        self.widget.setGeometry(QtCore.QRect(60, 59, 361, 381))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.entryName = QtWidgets.QComboBox(parent=self.widget)
        self.entryName.setEnabled(True)
        self.entryName.setMinimumSize(QtCore.QSize(210, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.entryName.setFont(font)
        self.entryName.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.entryName.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.entryName.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.entryName.setAutoFillBackground(False)
        self.entryName.setStyleSheet("")
        self.entryName.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.entryName.setIconSize(QtCore.QSize(24, 24))
        self.entryName.setFrame(True)
        self.entryName.setObjectName("entryName")
        self.entryName.addItem("")
        self.entryName.addItem("")
        self.entryName.addItem("")
        self.entryName.addItem("")
        self.entryName.addItem("")
        self.entryName.addItem("")
        self.entryName.addItem("")
        self.entryName.addItem("")
        self.entryName.addItem("")
        self.entryName.addItem("")
        self.entryName.addItem("")
        self.entryName.addItem("")
        self.entryName.addItem("")
        self.gridLayout.addWidget(self.entryName, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.payerName = QtWidgets.QLineEdit(parent=self.widget)
        self.payerName.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.payerName.setFont(font)
        self.payerName.setObjectName("payerName")
        self.gridLayout.addWidget(self.payerName, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.receiverName = QtWidgets.QLineEdit(parent=self.widget)
        self.receiverName.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.receiverName.setFont(font)
        self.receiverName.setObjectName("receiverName")
        self.gridLayout.addWidget(self.receiverName, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.entryDate = QtWidgets.QDateEdit(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.entryDate.setFont(font)
        self.entryDate.setCalendarPopup(True)
        self.entryDate.setObjectName("entryDate")
        self.gridLayout.addWidget(self.entryDate, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.widget)
        self.label_8.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.amount = QtWidgets.QLineEdit(parent=self.widget)
        self.amount.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.amount.setFont(font)
        self.amount.setObjectName("amount")
        self.gridLayout.addWidget(self.amount, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.widget)
        self.label_9.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.description = QtWidgets.QLineEdit(parent=self.widget)
        self.description.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.description.setFont(font)
        self.description.setObjectName("description")
        self.gridLayout.addWidget(self.description, 5, 1, 1, 1)

        self.retranslateUi(CostEntry)
        QtCore.QMetaObject.connectSlotsByName(CostEntry)

    def retranslateUi(self, CostEntry):
        _translate = QtCore.QCoreApplication.translate
        CostEntry.setWindowTitle(_translate("CostEntry", "Dialog"))
        self.cancelBtn.setText(_translate("CostEntry", " বাতিল"))
        self.addBtn.setText(_translate("CostEntry", "ঠিক আছে"))
        self.label_3.setText(_translate("CostEntry", " এন্ট্রি নাম"))
        self.entryName.setItemText(0, _translate("CostEntry", "বিক্রেতা কে প্রদান"))
        self.entryName.setItemText(1, _translate("CostEntry", "ক্রেতা থেকে গ্রহণ"))
        self.entryName.setItemText(2, _translate("CostEntry", "মূলধন ফেরৎ"))
        self.entryName.setItemText(3, _translate("CostEntry", "মূলধন জমা"))
        self.entryName.setItemText(4, _translate("CostEntry", "ঋণ গ্রহণ"))
        self.entryName.setItemText(5, _translate("CostEntry", "ঋণ পরিশোধ"))
        self.entryName.setItemText(6, _translate("CostEntry", "বেতন / মজুরি প্রদান"))
        self.entryName.setItemText(7, _translate("CostEntry", "অফিস খরচ"))
        self.entryName.setItemText(8, _translate("CostEntry", "মসজিদ/মাদ্রাসা"))
        self.entryName.setItemText(9, _translate("CostEntry", "সমিতি"))
        self.entryName.setItemText(10, _translate("CostEntry", "অন্যান্য খরচ(ভাউচার)"))
        self.entryName.setItemText(11, _translate("CostEntry", "ঋণ প্রদান"))
        self.entryName.setItemText(12, _translate("CostEntry", "প্রদেয় ঋণ গ্রহণ"))
        self.label_4.setText(_translate("CostEntry", "প্রদানকারী নাম :"))
        self.label_5.setText(_translate("CostEntry", "গ্রহণকারীর নাম :"))
        self.label_7.setText(_translate("CostEntry", "তারিখ :"))
        self.label_8.setText(_translate("CostEntry", "পরিমাণ :"))
        self.label_9.setText(_translate("CostEntry", "বিবরণ :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CostEntry = QtWidgets.QDialog()
    ui = Ui_CostEntry()
    ui.setupUi(CostEntry)
    CostEntry.show()
    sys.exit(app.exec())

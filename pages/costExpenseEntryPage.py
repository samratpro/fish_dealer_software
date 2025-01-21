from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
from PyQt6.QtCore import QDate
from forms.cost_entry import Ui_CostEntry
from models import *
from features.data_save_signals import data_save_signals


class Ui_costExpenseMain(object):
    def setupUi(self, costExpenseMain):

        # ****************** Declear database ************************
        self.Base = declarative_base()
        self.engine = create_engine('sqlite:///business.db')    # change db url
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        # ******************* end db ***************************

        costExpenseMain.setObjectName("costExpenseMain")
        costExpenseMain.resize(944, 650)
        costExpenseMain.setStyleSheet("""*{text-align: left;}
                                      QLineEdit, QComboBox{border-radius:10px;
                                                           border:1px solid #B8B8B8;
                                                           padding:2px;}
                                      QPushButton{background-color:#150E0A;
                                                  color:white;
                                                  padding:3px 12px 0px 8px;
                                                  border-radius:9px;
                                                  text-align:center;}
                                      QDateEdit{border:1px solid #B8B8B8;border-radius:5px;}
                                      QDateEdit::drop-down {
                                            image: url('./images/down-arrow.png');
                                            margin:3px 4px 0 0;
                                            border:1px solid #DEDEDE;
                                           }
                                      """)
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
        self.accountNameSelect.addItem("")
        self.accountNameSelect.addItem("")
        self.accountNameSelect.addItem("")
        self.accountNameSelect.addItem("")
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
        self.tableWidget.setStyleSheet("""QHeaderView::section, QHeaderView{background-color: #2D221B;
                                                                            color: white;
                                                                            font-size: 12pt;
                                                                            text-align: center;
                                                                            }""")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(165)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(165)

        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tableWidget.setFont(font)
        font.setPointSize(12)  # Set the font size to 12 points
        self.tableWidget.setFont(font)
        self.cashReportBody_Layout.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.costExpenseBody)
        self.costExpenseBottom = QtWidgets.QWidget(parent=costExpenseMain)
        self.costExpenseBottom.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.costExpenseBottom.setFont(font)
        self.costExpenseBottom.setStyleSheet("""#paidAmount, #receivedAmount, #revenueAmount{background:white;
                                                                                            color:black;
                                                                                            border-radius:10px;
                                                                                            border:1px solid #828282;
                                                                                            }
                                                                                            """)
        self.costExpenseBottom.setObjectName("costExpenseBottom")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.costExpenseBottom)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.receivedLabel = QtWidgets.QLabel(parent=self.costExpenseBottom)
        self.receivedLabel.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.receivedLabel.setFont(font)
        self.receivedLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.receivedLabel.setObjectName("receivedLabel")
        self.horizontalLayout.addWidget(self.receivedLabel)
        self.receivedAmount = QtWidgets.QLabel(parent=self.costExpenseBottom)
        self.receivedAmount.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.receivedAmount.setFont(font)
        self.receivedAmount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.receivedAmount.setObjectName("receivedAmount")
        self.horizontalLayout.addWidget(self.receivedAmount)
        self.paidLable = QtWidgets.QLabel(parent=self.costExpenseBottom)
        self.paidLable.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.paidLable.setFont(font)
        self.paidLable.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.paidLable.setObjectName("paidLable")
        self.horizontalLayout.addWidget(self.paidLable)
        self.paidAmount = QtWidgets.QLabel(parent=self.costExpenseBottom)
        self.paidAmount.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.paidAmount.setFont(font)
        self.paidAmount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.paidAmount.setObjectName("paidAmount")
        self.horizontalLayout.addWidget(self.paidAmount)
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
        costExpenseMain.setWindowTitle(_translate("costExpenseMain", "আড়ৎ এর হিসাব"))
        self.accountNameLabel.setText(_translate("costExpenseMain", "হিসাবের নাম"))
        self.accountNameSelect.setItemText(0, _translate("costExpenseMain", "সব হিসাব"))
        self.accountNameSelect.setItemText(1, _translate("costExpenseMain", "বিক্রেতা কে প্রদান"))
        self.accountNameSelect.setItemText(2, _translate("costExpenseMain", "ক্রেতা থেকে গ্রহণ"))
        self.accountNameSelect.setItemText(3, _translate("costExpenseMain", "মুনাফা উত্তোলন"))
        self.accountNameSelect.setItemText(4, _translate("costExpenseMain", "মূলধন জমা"))
        self.accountNameSelect.setItemText(5, _translate("costExpenseMain", "ঋণ গ্রহণ"))
        self.accountNameSelect.setItemText(6, _translate("costExpenseMain", "ঋণ পরিশোধ"))
        self.accountNameSelect.setItemText(7, _translate("costExpenseMain", "বেতন/মজুরি প্রদান"))
        self.accountNameSelect.setItemText(8, _translate("costExpenseMain", "অন্যান্য খরচ"))
        self.accountNameSelect.setItemText(9, _translate("costExpenseMain", "মসজিদ/মাদ্রাসা"))
        self.accountNameSelect.setItemText(10, _translate("costExpenseMain", "সমিতি"))
        self.accountNameSelect.setItemText(11, _translate("costExpenseMain", "অন্যান্য(ভাউচার)"))
        self.startDateLabel.setText(_translate("costExpenseMain", "তারিখ"))
        self.startDateInput.setDisplayFormat(_translate("costExpenseMain", "dd/mm/yyyy"))
        self.endDateLabel.setText(_translate("costExpenseMain", "শেষ তারিখ"))
        self.endDateInput.setDisplayFormat(_translate("costExpenseMain", "dd/mm/yyyy"))
        self.filterLabel.setText(_translate("costExpenseMain", "অ্যাকশন"))
        self.filterBtn.setText(_translate("costExpenseMain", "ফিল্টার"))
        self.costExpenseEntryLabel.setText(_translate("costExpenseMain", "আয় ব্যয় এন্ট্রি"))
        self.costExpenseEntryBtn.setText(_translate("costExpenseMain", "এন্ট্রি করুন"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("costExpenseMain", "এন্ট্রি আইডি"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("costExpenseMain", "তারিখ "))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("costExpenseMain", "হিসাবের নাম"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("costExpenseMain", "প্রদান/গ্রহণ কারীর নাম"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("costExpenseMain", "গ্রহণের পরিমান"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("costExpenseMain", "প্রদানের পরিমান"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("costExpenseMain", "এন্ট্রি বাই"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("costExpenseMain", "অ্যাকশন"))
        self.receivedLabel.setText(_translate("costExpenseMain", "মোট গ্রহণ:"))
        self.receivedAmount.setText(_translate("costExpenseMain", "0"))
        self.paidLable.setText(_translate("costExpenseMain", "মোট প্রদান:"))
        self.paidAmount.setText(_translate("costExpenseMain", "0"))
        self.saveBtn.setText(_translate("costExpenseMain", "সেভ এক্সেল"))
        self.printBtn.setText(_translate("costExpenseMain", "প্রিন্ট"))

        # Set current date ****************
        self.startDateInput.setDisplayFormat("dd/MM/yyyy")
        self.endDateInput.setDisplayFormat("dd/MM/yyyy")
        self.today_date_raw = datetime.now()
        self.today_date = self.today_date_raw.strftime("%d/%m/%Y").lstrip('0').replace('/0', '/')
        self.qdate_today = QDate.fromString(self.today_date, "d/M/yyyy")
        self.startDateInput.setDate(self.qdate_today)
        self.endDateInput.setDate(self.qdate_today)

        data_save_signals.data_saved.connect(self.filter_data)
        self.costExpenseEntryBtn.clicked.connect(self.open_entry_form)  # Open Entry and entry data
        self.filter_data()
        self.filterBtn.clicked.connect(self.filter_data)

        self.entry_by = ''
        self.entry_by_username()
        data_save_signals.data_saved.connect(self.entry_by_username)


    def entry_by_username(self):
        session = self.Session()
        setting = session.query(SettingModel).first()
        
        self.entry_by = setting.username
        session.close()

    def filter_data(self):
        try:
            entry_index = self.accountNameSelect.currentIndex()
            entry_name = {0:'all_accounting',1: 'paid_to_seller',
                          2: 'get_paid_from_buyer',3: 'capital_withdrawal',
                          4: 'capital_deposit',5: 'borrowing',
                          6: 'loan_repayment',7: 'salary',
                          8: 'other_cost', 9:'mosque', 10:'somiti', 11: 'other_cost_voucher'
                          }.get(entry_index, 'all_accounting')
            start_date = self.startDateInput.date().toPyDate()
            end_date = self.endDateInput.date().toPyDate()

            # Retrieve data from the database
            session = self.Session()
            query = session.query(DealerModel).filter(DealerModel.date.between(start_date, end_date))
            if entry_name != 'all_accounting':
                query = query.filter(DealerModel.entry_name.ilike(f"%{entry_name}%"))
            all_entries = query.all()

            # Clear existing table data
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

            # Populate the table with queried data
            self.receivedAmount.setText(str(0))
            self.paidAmount.setText(str(0))
            row = 0
            for entry in all_entries:
                entry_name = {'paid_to_seller': "বিক্রেতা কে প্রদান", 'get_paid_from_buyer': "ক্রেতা থেকে গ্রহণ",
                              'capital_withdrawal': "মুনাফা উত্তোলন", 'capital_deposit': "মূলধন জমা",
                              'borrowing': "ঋণ গ্রহণ", 'loan_repayment': "ঋণ পরিশোধ",
                              'salary': "বেতন / মজুরি প্রদান", 'other_cost': "অন্যান্য খরচ", 'mosque':'মসজিদ/মাদ্রাসা',
                              'somiti':'সমিতি','other_cost_voucher':'অন্যান্য(ভাউচার)'
                              }.get(entry.entry_name.strip(), "অন্যান্য খরচ")
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(entry.id)))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(entry.date)))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(entry_name)))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(entry.name)))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(entry.receiving_amount)))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(entry.paying_amount)))
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(entry.entry_by)))

                delete_button = QtWidgets.QPushButton("")
                delete_icon = QtGui.QIcon("./images/delete.png")  # Path to your delete icon
                delete_button.setIcon(delete_icon)
                delete_button.setIconSize(QtCore.QSize(24, 24))  # Set icon size if needed
                delete_button.setStyleSheet("background-color: white; border: none;margin-left:50px;")  # Set wh
                delete_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                delete_button.clicked.connect(lambda _, r=row: self.delete_row(r))
                self.tableWidget.setCellWidget(row, 7, delete_button)

                old_receivedAmount = int(self.receivedAmount.text())
                self.receivedAmount.setText(str(old_receivedAmount+int(entry.receiving_amount)))
                old_paidAmount = int(self.paidAmount.text())
                self.paidAmount.setText(str(old_paidAmount+int(entry.paying_amount)))
                row += 1
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "seller Profile Error", f"An error occurred while filtering data: {e}")

    def delete_row(self, row):
        try:
            reply = QtWidgets.QMessageBox.question(
                None,
                'মুছে ফেলা নিশ্চিত করুন',
                'আপনি কি নিশ্চিত যে আপনি এই এন্ট্রিটি মুছে ফেলতে চান?',
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                QtWidgets.QMessageBox.StandardButton.No
            )

            # If the user confirms, proceed with deletion
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                entry_id = self.tableWidget.item(row, 0).text()
                session = self.Session()
                entry = session.query(DealerModel).filter(DealerModel.id==entry_id).one()
                self.update_capital(entry.paying_amount, entry.receiving_amount)
                if entry.entry_name == "paid_to_seller":
                    seller = session.query(SellerProfileModel).filter_by(seller_name=entry.name).first()
                    seller.total_get_paid_amount -= entry.paying_amount
                    seller.total_receivable += entry.paying_amount
                elif entry.entry_name == "get_paid_from_buyer":  # get_paid_from_buyer
                    buyer = session.query(BuyerProfileModel).filter_by(buyer_name=entry.name).first()
                    buyer.total_payable += entry.receiving_amount
                    buyer.total_paid -= entry.receiving_amount
                elif entry.entry_name == "borrowing":  # borrowing
                    self.update_loan_model(entry.name, entry.receiving_amount, 'sub')
                elif entry.entry_name == "loan_repayment":  # loan_repayment
                    self.update_loan_model(entry.name, entry.paying_amount, 'add')
                elif entry.entry_name == "mosque":  # mosque
                    cost = session.query(CostModel).first()
                    cost.mosque += entry.paying_amount
                    cost.mosque_get_paid -= entry.paying_amount
                elif entry.entry_name == "somiti":  # somiti
                    cost = session.query(CostModel).first()
                    cost.somiti += entry.paying_amount
                    cost.somiti_get_paid -= entry.paying_amount
                elif entry.entry_name == "other_cost_voucher":  # other_cost_voucher
                    cost = session.query(CostModel).first()
                    cost.other_cost += entry.paying_amount
                    cost.other_cost_paid -= entry.paying_amount
                session.query(DealerModel).filter(DealerModel.id == entry_id).delete()
                session.commit()
                self.tableWidget.removeRow(row)
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Delete Error", f"An error occurred while deleting the row: {e}")
        data_save_signals.data_saved.emit()

    def update_capital(self,paying_amount,receiving_amount):
        session = self.Session()
        capital = session.query(FinalAccounting).first()
        capital.capital += paying_amount
        capital.capital -= receiving_amount
        session.commit()

    def update_loan_model(self, name, amount, param):
        session = self.Session()
        payer_name = session.query(LoanModel).filter_by(loan_payer_name=name).first()
        if param == 'sub':
            payer_name.amount -= amount
        else:
            payer_name.amount += amount
        session.commit()

    def cell_edited(self, row, column):
        # Reconnect the delete button after a cell is edited
        if column < 6:  # Only do this for data columns, not the button column
            delete_button = self.tableWidget.cellWidget(row, 6)
            if delete_button is not None:
                delete_button.clicked.disconnect()
                delete_button.clicked.connect(lambda _, r=row: self.delete_row(r))
    def reconnect_delete_buttons(self):
        # Reconnect all delete buttons after a row is deleted
        row_count = self.tableWidget.rowCount()
        for row in range(row_count):
            delete_button = self.tableWidget.cellWidget(row, 6)
            if delete_button is not None:
                delete_button.clicked.disconnect()
                delete_button.clicked.connect(lambda _, r=row: self.delete_row(r))




    def open_entry_form(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_CostEntry()
        self.ui.setupUi(self.dialog)
        self.ui.addBtn.clicked.connect(self.accept_information)
        self.ui.cancelBtn.clicked.connect(self.dialog.close)
        self.dialog.exec()

    def accept_information(self):
        try:
            session = self.Session()
            entry_index = self.ui.entryName.currentIndex()
            entry_name = {
                0: 'paid_to_seller', 1: 'get_paid_from_buyer',
                2: 'capital_withdrawal', 3: 'capital_deposit',
                4: 'borrowing', 5: 'loan_repayment',
                6: 'salary', 7: 'other_cost',8:'mosque', 9:'somiti', 10: 'other_cost_voucher'
            }.get(entry_index, 'other_cost')

            payerName = self.ui.payerName.text().strip()
            receiverName = self.ui.receiverName.text().strip()
            entry_date = self.ui.entryDate.date().toPyDate()
            amount = self.ui.amount.text().strip()
            entry_by = self.entry_by  # Replace with dynamic user input if necessary

            # Define a mapping for required fields per entry_name
            required_fields = {
                'paid_to_seller': {'must_fill': 'receiverName', 'must_be_empty': 'payerName'},
                'capital_withdrawal': {'must_fill': 'receiverName', 'must_be_empty': 'payerName'},
                'loan_repayment': {'must_fill': 'receiverName', 'must_be_empty': 'payerName'},
                'salary': {'must_fill': 'receiverName', 'must_be_empty': 'payerName'},
                'other_cost': {'must_fill': 'receiverName', 'must_be_empty': 'payerName'},
                'get_paid_from_buyer': {'must_fill': 'payerName', 'must_be_empty': 'receiverName'},
                'capital_deposit': {'must_fill': 'payerName', 'must_be_empty': 'receiverName'},
                'borrowing': {'must_fill': 'payerName', 'must_be_empty': 'receiverName'},
                'mosque': {'must_fill': 'receiverName', 'must_be_empty': 'payerName'},
                'somiti': {'must_fill': 'receiverName', 'must_be_empty': 'payerName'},
                'other_cost_voucher': {'must_fill': 'receiverName', 'must_be_empty': 'payerName'},
            }

            # Validate mandatory fields
            if not (entry_name and entry_date and amount):
                self.show_error_message("অবশ্যই সব তথ্য পূরণ করতে হবে..")
                return

            # Validate numeric amount
            try:
                amount = int(float(amount))
            except ValueError:
                self.show_error_message("পরিমান সংখ্যা হতে হবে..")
                return

            # Check if entry_name has specific requirements
            if entry_name in required_fields:
                rules = required_fields[entry_name]
                must_fill = rules['must_fill']
                must_be_empty = rules['must_be_empty']

                # Validate 'must_fill' field
                if must_fill == 'receiverName' and not receiverName:
                    self.show_error_message(f"এই এন্ট্রির জন্য শুধুমাত্র গ্রহণকারী পূরণ করতে হবে।")
                    return
                if must_fill == 'payerName' and not payerName:
                    self.show_error_message(f"এই এন্ট্রির জন্য শুধুমাত্র প্রদানকারী পূরণ করতে হবে।")
                    return

                # Validate 'must_be_empty' field
                if must_be_empty == 'payerName' and payerName:
                    self.show_error_message(f"এই এন্ট্রির জন্য প্রদানকারী পূরণ করা যাবে না।")
                    return
                if must_be_empty == 'receiverName' and receiverName:
                    self.show_error_message(f"এই এন্ট্রির জন্য গ্রহণকারী পূরণ করা যাবে না।")
                    return

            # Handle entry logic
            if entry_name == 'paid_to_seller':
                # seller
                seller = session.query(SellerProfileModel).filter_by(seller_name=receiverName).first()
                if not seller:
                    self.show_error_message("বিক্রেতার প্রোফাইল পাওয়া যায়নি।")
                    return
                seller.total_receivable -= amount
                seller.total_get_paid_amount += amount
                #DealerModel
                dealer_entry = DealerModel(
                    entry_name=entry_name,
                    name=receiverName,
                    date=entry_date,
                    paying_amount=amount,
                    entry_by=entry_by
                )
                session.add(dealer_entry)
                # Capital
                accounting = session.query(FinalAccounting).first()
                accounting.capital -= amount
                session.commit()

            elif entry_name == 'get_paid_from_buyer':
                # buyer
                buyer = session.query(BuyerProfileModel).filter_by(buyer_name=payerName).first()
                if not buyer:
                    self.show_error_message("ক্রেতার প্রোফাইল পাওয়া যায়নি।")
                    return
                buyer.total_payable -= amount
                buyer.total_paid += amount
                # Save to DealerModel
                dealer_entry = DealerModel(
                    entry_name=entry_name,
                    name=payerName,
                    date=entry_date,
                    receiving_amount=amount,
                    entry_by=entry_by
                )
                session.add(dealer_entry)
                # capital
                accounting = session.query(FinalAccounting).first()
                accounting.capital += amount
                session.commit()
            elif entry_name == 'capital_withdrawal':
                # Dealer
                dealer_entry = DealerModel(
                    entry_name=entry_name,
                    name=receiverName,
                    date=entry_date,
                    paying_amount=amount,
                    entry_by=entry_by
                )
                session.add(dealer_entry)
                # capital
                accounting = session.query(FinalAccounting).first()
                accounting.capital -= amount
                session.commit()

            elif entry_name == 'capital_deposit':
                # dealer
                dealer_entry = DealerModel(
                    entry_name=entry_name,
                    name=payerName,
                    date=entry_date,
                    receiving_amount=amount,
                    entry_by=entry_by
                )
                session.add(dealer_entry)
                # capital
                accounting = session.query(FinalAccounting).first()
                accounting.capital += amount
                session.commit()

            elif entry_name == 'borrowing':
                dealer_entry = DealerModel(
                    entry_name=entry_name,
                    name=payerName,
                    date=entry_date,
                    receiving_amount=amount,
                    entry_by=entry_by
                )
                session.add(dealer_entry)
                accounting = session.query(FinalAccounting).first()
                accounting.capital += amount
                loan_entry = LoanModel(
                    loan_payer_name=payerName,
                    date=entry_date,
                    amount=amount,
                    entry_by=entry_by
                )
                session.add(loan_entry)
                session.commit()

            elif entry_name == 'loan_repayment':
                loan_receiver = session.query(LoanModel).filter_by(loan_payer_name=receiverName).first()
                if not loan_receiver:
                    self.show_error_message("ঋণ গ্রহণকারী কে পাওয়া যায়নি")
                    return
                dealer_entry = DealerModel(
                    entry_name=entry_name,
                    name=receiverName,
                    date=entry_date,
                    paying_amount=amount,
                    entry_by=entry_by
                )
                session.add(dealer_entry)
                accounting = session.query(FinalAccounting).first()
                accounting.capital -= amount
                loan_receiver.amount -= amount
                session.commit()

            elif entry_name=='salary' or entry_name=='other_cost' or entry_name=='mosque' or entry_name=='somiti' or entry_name=='other_cost_voucher':
                dealer_entry = DealerModel(
                    entry_name=entry_name,
                    name=receiverName,
                    date=entry_date,
                    paying_amount=amount,
                    entry_by=entry_by
                )
                session.add(dealer_entry)
                accounting = session.query(FinalAccounting).first()
                accounting.capital -= amount
                session.commit()

                cost = session.query(CostModel).first()
                if entry_name == 'mosque':
                    cost.mosque -= amount
                    cost.mosque_get_paid += amount
                if entry_name == 'somiti':
                    cost.somiti -= amount
                    cost.somiti_get_paid += amount
                if entry_name == 'other_cost_voucher':
                    cost.other_cost -= amount
                    cost.other_cost_paid += amount
                session.commit()
            else:
                self.show_error_message("অবৈধ এন্ট্রি নাম।")
                return
            session.commit()
            self.dialog.close()
        except Exception as e:
            print(f"Error in seller info: {e}")
            self.show_error_message("ডাটা প্রক্রিয়াকরণের সময় সমস্যা হয়েছে।")
        self.filter_data()
        data_save_signals.data_saved.emit()  # send signal after save data


    def show_error_message(self, message):
        """Helper method to show error message."""
        error_dialog = QtWidgets.QMessageBox(self.dialog)
        error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        error_dialog.setWindowTitle("Input Error")
        error_dialog.setText(message)
        error_dialog.exec()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    costExpenseMain = QtWidgets.QWidget()
    ui = Ui_costExpenseMain()
    ui.setupUi(costExpenseMain)
    costExpenseMain.show()
    sys.exit(app.exec())

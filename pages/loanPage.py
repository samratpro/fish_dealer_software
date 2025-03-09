from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QHeaderView
from models import *
from features.data_save_signals import data_save_signals
from PyQt6.QtGui import QFont, QFontDatabase  # for font file load
import os

class Ui_LoanPage(object):
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
        self.tableWidget.setColumnCount(5)
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
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
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
        self.retranslateUi(costExpenseMain)
        QtCore.QMetaObject.connectSlotsByName(costExpenseMain)



    def retranslateUi(self, costExpenseMain):
        _translate = QtCore.QCoreApplication.translate
        costExpenseMain.setWindowTitle(_translate("costExpenseMain", "ঋণ এর হিসাব"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("costExpenseMain", "তারিখ "))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("costExpenseMain", "হিসাবের নাম"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("costExpenseMain", "প্রদান কারীর নাম"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("costExpenseMain", "পরিমান"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("costExpenseMain", "এন্ট্রি বাই"))

        self.tableWidget.horizontalHeader().setDefaultSectionSize(240)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(240)
        self.tableWidget.verticalHeader().setVisible(False)
        self.filter_data()
        data_save_signals.data_saved.connect(self.filter_data)

        self.apply_bangla_font()

    def apply_bangla_font(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        bangla_font_path = os.path.join(base_dir, "font", "nato.ttf")
        font_id = QFontDatabase.addApplicationFont(bangla_font_path)
        if font_id == -1:
            print(f"❌ Failed to load font: {bangla_font_path}")
            return
        font_id = QFontDatabase.addApplicationFont(bangla_font_path)
        custom_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font = QFont(custom_font_family, 13)  # Font size 14
        # Apply font to table headers
        self.tableWidget.horizontalHeader().setFont(custom_font)
        self.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.tableWidget.horizontalHeader().setFont(custom_font)
        self.tableWidget.setFont(custom_font)
        self.tableWidget.verticalHeader().setFont(custom_font)
        self.tableWidget.viewport().update()

    def filter_data(self):
        try:
            # Retrieve data from the database
            session = self.Session()
            query = session.query(LoanModel).filter(LoanModel.amount > 0)
            all_entries = query.all()
            # Clear existing table data
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            # Populate the table with queried data
            row = 0
            for entry in all_entries:
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(entry.date)))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem("ঋণ গ্রহণ"))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(entry.loan_payer_name)))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(entry.amount)))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(entry.entry_by)))

                row += 1
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "seller Profile Error", f"An error occurred while filtering data: {e}")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    costExpenseMain = QtWidgets.QWidget()
    ui = Ui_LoanPage()
    ui.setupUi(costExpenseMain)
    costExpenseMain.show()
    sys.exit(exec())

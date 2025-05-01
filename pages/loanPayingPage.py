from PyQt6 import QtCore, QtGui, QtWidgets
from models import *
from features.data_save_signals import data_save_signals
from PyQt6.QtGui import QFont, QFontDatabase  # for font file load
from forms.loan_receiver_profile_edit import Profile_Edit_Form
from pages.loanPayingView import LoanProfileView
from PyQt6.QtWidgets import QHeaderView
import os


class Ui_LoanPayingPage(object):
    def setupUi(self, costExpenseMain):

        # ****************** Declear database ************************
        self.Base = declarative_base()
        self.engine = create_engine('sqlite:///business.db')  # change db url
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
        item.setText(_translate("costExpenseMain", "গ্রহণ কারীর নাম"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("costExpenseMain", "ফোন"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("costExpenseMain", "পরিমান"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("costExpenseMain", "ভিউ"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("costExpenseMain", "এন্ট্রি বাই"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("costExpenseMain", "এডিট"))

        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(170)
        self.tableWidget.verticalHeader().setVisible(False)
        self.filter_data()
        data_save_signals.data_saved.connect(self.filter_data)

        self.apply_bangla_font()

    def apply_bangla_font(self):
        bangla_font_path = "font/nato.ttf"
        font_id = QFontDatabase.addApplicationFont(bangla_font_path)
        if font_id == -1:
            print(f"❌ Failed to load font: {bangla_font_path}")
            return
        font_id = QFontDatabase.addApplicationFont(bangla_font_path)
        custom_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font = QFont(custom_font_family, 13)  # Font size 14
        self.tableWidget.horizontalHeader().setFont(custom_font)
        self.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget.setFont(custom_font)
        self.tableWidget.viewport().update()

    def filter_data(self):
        try:
            # Retrieve data from the database
            session = self.Session()
            all_entries = session.query(PayingLoanProfileModel).all()
            # Clear existing table data
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            # Populate the table with queried data
            row = 0
            for entry in all_entries:
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(entry.date)))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem("ঋণ প্রদান"))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(entry.loan_receiver_name)))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(entry.phone)))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(entry.amount)))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(entry.entry_by)))

                # Add a delete button in the last column
                view_button = QtWidgets.QPushButton("")
                view_icon = QtGui.QIcon("./images/view.png")  # Path to your delete icon
                view_button.setIcon(view_icon)
                view_button.setIconSize(QtCore.QSize(24, 24))  # Set icon size if needed
                view_button.setStyleSheet("background-color: white; border: none;margin-left:50px;")  # Set wh
                view_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

                view_button.clicked.connect(lambda _, name=entry.loan_receiver_name, phone=entry.phone: self.view_profile(name, phone))
                self.tableWidget.setCellWidget(row, 6, view_button)

                # Add a edit button
                edit_button = QtWidgets.QPushButton("")
                edit_icon = QtGui.QIcon("./images/edit.png")  # Path to your delete icon
                edit_button.setIcon(edit_icon)
                edit_button.setIconSize(QtCore.QSize(24, 24))  # Set icon size if needed
                edit_button.setStyleSheet("background-color: white; border: none;margin-left:50px;")  # Set wh
                edit_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                edit_button.clicked.connect(
                    lambda _, receiver_name=entry.loan_receiver_name: self.profile_edit(
                        receiver_name))
                self.tableWidget.setCellWidget(row, 7, edit_button)

                row += 1
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Loan Paying Profile Error", f"An error occurred while filtering data: {e}")

    def view_profile(self, payer_name, phone):
        try:
            session = self.Session()
            self.transactions_window = LoanProfileView(payer_name, phone, session)
            self.transactions_window.show()
        except Exception as e:
            print(f' err o : {str(e)}')


    def profile_edit(self, receiver_name):
        try:
            # Create and show the SellerInformation dialog
            self.profile_edit_form_ui = Profile_Edit_Form(receiver_name)
            self.profile_edit_form_ui.setWindowTitle("Profile Edit")

            # Connect buttons with proper lambda or partial
            self.profile_edit_form_ui.ui.update.clicked.connect(
                lambda: self.handle_profile_edit_information(receiver_name))
            self.profile_edit_form_ui.ui.cancel.clicked.connect(self.profile_edit_form_ui.close)

            # Show the dialog
            self.profile_edit_form_ui.exec()
        except Exception as e:
            import traceback
            print(f"Error in profile_edit: {traceback.format_exc()}")
            QtWidgets.QMessageBox.critical(None, "Error", f"An unexpected error occurred: {e}")

    def handle_profile_edit_information(self, receiver_name):
        try:
            success, error_message = self.profile_edit_form_ui.handle_entry()
            if success:
                self.accept_profile_edit_information(receiver_name)
            else:
                error_dialog = QtWidgets.QMessageBox(self.profile_edit_form_ui)
                error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                error_dialog.setWindowTitle("Input Error")
                error_dialog.setText(error_message)
                error_dialog.exec()
        except Exception as e:
            import traceback
            print(f"Error in handle_profile_edit_information: {traceback.format_exc()}")
            QtWidgets.QMessageBox.critical(self.profile_edit_form_ui, "Error", f"An unexpected error occurred: {e}")

    def accept_profile_edit_information(self, receiver_name):
        try:
            name = self.profile_edit_form_ui.ui.name.text().strip()
            phone = self.profile_edit_form_ui.ui.phone.text().strip()
            if name:
                with self.Session() as session:
                    profile = session.query(PayingLoanProfileModel).filter(PayingLoanProfileModel.loan_receiver_name == receiver_name).first()
                    if profile:
                        profile.loan_receiver_name = name
                        profile.phone = phone
                        session.commit()
                        self.filter_data()
                        self.profile_edit_form_ui.close()
                    else:
                        error_dialog = QtWidgets.QMessageBox(self.profile_edit_form_ui)
                        error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                        error_dialog.setWindowTitle("Not Found")
                        error_dialog.setText("Profile not found.")
                        error_dialog.exec()
            else:
                error_dialog = QtWidgets.QMessageBox(self.profile_edit_form_ui)
                error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                error_dialog.setWindowTitle("Input Error")
                error_dialog.setText("All fields must be filled.")
                error_dialog.exec()
        except Exception as e:
            import traceback
            print(f"Error in accept_information: {traceback.format_exc()}")
            error_dialog = QtWidgets.QMessageBox(self.profile_edit_form_ui)
            error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("Invalid input.")
            error_dialog.exec()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    costExpenseMain = QtWidgets.QWidget()
    ui = Ui_LoanPayingPage()
    ui.setupUi(costExpenseMain)
    costExpenseMain.show()
    sys.exit(exec())

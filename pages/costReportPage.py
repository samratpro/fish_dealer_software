from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from datetime import datetime
from PyQt6.QtCore import QDate
from forms.cost_entry import Ui_CostEntry
from models import *
from features.data_save_signals import data_save_signals
from ui.costReportPage_ui import costReport_ui


class costReport(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_database()  # First setup database
        self.ui = costReport_ui()
        self.ui.setupUi(self)
        self.setup_ui()



    def setup_database(self):
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker, declarative_base

        self.Base = declarative_base()
        self.engine = create_engine('sqlite:///business.db')
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def setup_ui(self):

        self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(165)
        self.ui.tableWidget.horizontalHeader().setMinimumSectionSize(165)

        # Set current date ****************
        self.ui.startDateInput.setDisplayFormat("dd/MM/yyyy")
        self.ui.endDateInput.setDisplayFormat("dd/MM/yyyy")
        self.today_date_raw = datetime.now()
        self.today_date = self.today_date_raw.strftime("%d/%m/%Y").lstrip('0').replace('/0', '/')
        self.qdate_today = QDate.fromString(self.today_date, "d/M/yyyy")
        self.ui.startDateInput.setDate(self.qdate_today)
        self.ui.endDateInput.setDate(self.qdate_today)

        data_save_signals.data_saved.connect(self.filter_data)
        self.filter_data()
        self.ui.filterBtn.clicked.connect(self.filter_data)

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
            entry_index = self.ui.accountNameSelect.currentIndex()
            entry_name = {0:'all_accounting',1: 'salary',
                          2: 'other_cost',3: 'mosque',
                          4: 'somiti',5: 'other_cost_voucher'}.get(entry_index, 'all_accounting')
            start_date = self.ui.startDateInput.date().toPyDate()
            end_date = self.ui.endDateInput.date().toPyDate()

            # Retrieve data from the database
            session = self.Session()
            query = session.query(DealerModel).filter(DealerModel.date.between(start_date, end_date))
            if entry_name != 'all_accounting':
                query = query.filter(DealerModel.entry_name.ilike(f"%{entry_name}%"))
            all_entries = query.all()


            # Clear existing table data
            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.setRowCount(0)

            # Populate the table with queried data
            self.ui.receivedAmount.setText(str(0))
            self.ui.paidAmount.setText(str(0))
            row = 0
            for entry in all_entries:
                entry_name = {
                              'salary': "বেতন / মজুরি প্রদান", 'other_cost': "অন্যান্য খরচ", 'mosque':'মসজিদ/মাদ্রাসা',
                              'somiti':'সমিতি','other_cost_voucher':'অন্যান্য(ভাউচার)'
                              }.get(entry.entry_name.strip(), "অন্যান্য খরচ")
                self.ui.tableWidget.insertRow(row)
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(entry.id)))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(entry.date)))
                self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(entry_name)))
                self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(entry.name)))
                self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(entry.paying_amount)))
                self.ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(entry.entry_by)))

                old_paidAmount = int(self.ui.paidAmount.text())
                self.ui.paidAmount.setText(str(old_paidAmount+int(entry.paying_amount)))
                row += 1
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "seller Profile Error", f"An error occurred while filtering data: {e}")


    def show_error_message(self, message):
        """Helper method to show error message."""
        error_dialog = QtWidgets.QMessageBox(self.dialog)
        error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        error_dialog.setWindowTitle("Input Error")
        error_dialog.setText(message)
        error_dialog.exec()

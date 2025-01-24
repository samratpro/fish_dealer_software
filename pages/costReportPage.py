from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from datetime import datetime
from PyQt6.QtCore import QDate
from sqlalchemy.orm import sessionmaker, declarative_base
from models import *
from sqlalchemy import or_
from features.data_save_signals import data_save_signals
from ui.costReportPage_ui import costReport_ui
from features.printmemo import Ui_Form
from PyQt6 import QtWidgets, QtGui, QtPrintSupport
from PyQt6.QtWidgets import QFileDialog
import xlsxwriter


class CostReport(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_database()  # First setup database
        self.ui = costReport_ui()
        self.ui.setupUi(self)
        self.setup_ui()

    def setup_database(self):
        self.Base = declarative_base()
        self.engine = create_engine('sqlite:///business.db')
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def setup_ui(self):

        self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(165)
        self.ui.tableWidget.horizontalHeader().setMinimumSectionSize(165)
        self.ui.tableWidget.verticalHeader().setVisible(False)

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

        self.ui.filterNameInput.textChanged.connect(lambda: self.make_capital(self.ui.filterNameInput))
        self.auto_completer()

        self.ui.printBtn.clicked.connect(self.openPrintMemo)
        self.ui.saveBtn.clicked.connect(self.save_xlsx)

    def auto_completer(self):
        """Refresh the QCompleter with the latest seller names."""
        self.all_name = self.get_all_names()
        self.completer = QtWidgets.QCompleter(self.all_name, self)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ui.filterNameInput.setCompleter(self.completer)

    def get_all_names(self):
        """Fetch all seller names from the database for autocomplete."""
        session = self.Session()
        name_entries = session.query(DealerModel).all()     # change Model name
        session.close()
        return [entry_name.name for entry_name in name_entries]

    def make_capital(self, element):
        element.textChanged.disconnect()
        element.setText(element.text().title())
        element.textChanged.connect(lambda: self.make_capital(element))

    def filter_data(self):
        try:
            entry_index = self.ui.accountNameSelect.currentIndex()
            entry_name = {0: 'all_accounting', 1: 'salary',
                          2: 'other_cost', 3: 'mosque',
                          4: 'somiti', 5: 'other_cost_voucher'}.get(entry_index, 'all_accounting')
            start_date = self.ui.startDateInput.date().toPyDate()
            end_date = self.ui.endDateInput.date().toPyDate()

            # Retrieve data from the database
            with self.Session() as session:
                query = session.query(DealerModel).filter(DealerModel.date.between(start_date, end_date))

                if entry_name == 'all_accounting':
                    # Use or_ to combine multiple conditions
                    conditions = [
                        DealerModel.entry_name.ilike(f"%salary%"),
                        DealerModel.entry_name.ilike(f"%other_cost%"),
                        DealerModel.entry_name.ilike(f"%mosque%"),
                        DealerModel.entry_name.ilike(f"%somiti%"),
                        DealerModel.entry_name.ilike(f"%other_cost_voucher%")
                    ]
                    query = query.filter(or_(*conditions))
                else:
                    query = query.filter(DealerModel.entry_name.ilike(f"%{entry_name}%"))
                all_entries = query.all()


            # Clear existing table data
            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.setRowCount(0)

            # Populate the table with queried data
            self.ui.amount.setText(str(0))
            row = 0
            for entry in all_entries:
                entry_name = {
                              'salary': "বেতন / মজুরি প্রদান", 'other_cost': "অন্যান্য খরচ", 'mosque': 'মসজিদ/মাদ্রাসা',
                              'somiti': 'সমিতি', 'other_cost_voucher': 'অন্যান্য(ভাউচার)'
                              }.get(entry.entry_name.strip(), "অন্যান্য খরচ")
                self.ui.tableWidget.insertRow(row)
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(entry.id)))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(entry.date)))
                self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(entry_name)))
                self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(entry.name)))
                self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(entry.paying_amount)))
                self.ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(entry.entry_by)))

                old_amount = int(self.ui.amount.text())
                self.ui.amount.setText(str(old_amount+int(entry.paying_amount)))
                row += 1
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "seller Profile Error", f"An error occurred while filtering data: {e}")


    def openPrintMemo(self):
        try:
            self.print_window = QtWidgets.QWidget()
            self.ui_form = Ui_Form()
            self.ui_form.setupUi(self.print_window)

            # Table Update
            column_count = self.ui.tableWidget.columnCount()
            column_count -= 1
            row_count = self.ui.tableWidget.rowCount()
            headers = [self.ui.tableWidget.horizontalHeaderItem(i).text() for i in range(column_count)]

            # Set up the table headers in the print window
            self.ui_form.tableWidget.verticalHeader().setVisible(False)
            self.ui_form.tableWidget.setColumnCount(column_count)
            self.ui_form.tableWidget.setHorizontalHeaderLabels(headers)

            # Insert rows and data into the print window's table
            self.ui_form.tableWidget.setRowCount(row_count)
            for row_idx in range(row_count):
                for col_idx in range(column_count):
                    item = self.ui.tableWidget.item(row_idx, col_idx)
                    if item:
                        self.ui_form.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(item.text()))

            self.print_window.show()
            # Set up the printer
            printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterMode.ScreenResolution)
            printer.setPageSize(QtGui.QPageSize(QtGui.QPageSize.PageSizeId.A4))  # Set paper size to A4
            # printer.setFullPage(True)  # Use the full page
            # Open print dialog
            print_dialog = QtPrintSupport.QPrintDialog(printer)
            if print_dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                painter = QtGui.QPainter(printer)
                # Render the print window content to the printer
                painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)  # Improve rendering quality
                self.print_window.render(painter)
                painter.end()
            else:
                print("Print dialog canceled")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_xlsx(self):
        try:
            # Open a file dialog to select the location to save the Excel file
            file_path, _ = QFileDialog.getSaveFileName(
                None,  # Use the actual QWidget as the parent
                "Save Excel File",
                "",
                "Excel Files (*.xlsx);;All Files (*)"
            )

            # If no file is selected, return early
            if not file_path:
                return

            # Ensure the file has the correct extension
            if not file_path.endswith(".xlsx"):
                file_path += ".xlsx"

            # Create an Excel file using xlsxwriter
            workbook = xlsxwriter.Workbook(file_path)
            worksheet = workbook.add_worksheet("Table Data")

            # Retrieve data from the tableWidget
            row_count = self.ui.tableWidget.rowCount()
            column_count = self.ui.tableWidget.columnCount()

            # Write headers to the first row
            headers = [self.ui.tableWidget.horizontalHeaderItem(i).text() for i in range(column_count)]
            for col_idx, header in enumerate(headers):
                worksheet.write(0, col_idx, header)

            # Write table data to the worksheet
            for row_idx in range(row_count):
                for col_idx in range(column_count):
                    item = self.ui.tableWidget.item(row_idx, col_idx)
                    worksheet.write(row_idx + 1, col_idx, item.text() if item else "")

            # Close and save the workbook
            workbook.close()
            print(f"Excel file saved successfully at {file_path}")

        except Exception as e:
            print(f"An error occurred while saving Excel file: {e}")
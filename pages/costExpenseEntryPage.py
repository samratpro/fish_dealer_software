from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from features.data_save_signals import data_save_signals
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from ui.costExpenseEntryPage_ui import Ui_costExpenseMain
from models import *
from forms.cost_entry import Ui_CostEntry
from datetime import datetime
from PyQt6.QtCore import QDate
from features.printmemo import Ui_Form
from PyQt6 import QtWidgets, QtGui, QtPrintSupport
from PyQt6.QtWidgets import QFileDialog
import xlsxwriter

class costExpensePage(QWidget):
    def __init__(self, username):
        super().__init__()
        self.entry_by = username
        self.setup_database()  # First setup database
        self.ui = Ui_costExpenseMain()
        self.ui.setupUi(self)
        self.setup_ui()
        self.username = username
        session = self.Session()
        user = session.query(UserModel).filter(UserModel.username==self.username).one()
        self.user_role = user.role


    def setup_database(self):
        self.Base = declarative_base()
        self.engine = create_engine('sqlite:///business.db')  # change db url
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def setup_ui(self):
        # Set current date ****************
        self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(165)
        self.ui.tableWidget.horizontalHeader().setMinimumSectionSize(165)
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.startDateInput.setDisplayFormat("dd/MM/yyyy")
        self.ui.endDateInput.setDisplayFormat("dd/MM/yyyy")
        self.today_date_raw = datetime.now()
        self.today_date = self.today_date_raw.strftime("%d/%m/%Y").lstrip('0').replace('/0', '/')
        self.qdate_today = QDate.fromString(self.today_date, "d/M/yyyy")
        self.ui.startDateInput.setDate(self.qdate_today)
        self.ui.endDateInput.setDate(self.qdate_today)

        data_save_signals.data_saved.connect(self.filter_data)
        self.ui.costExpenseEntryBtn.clicked.connect(self.open_entry_form)  # Open Entry and entry data
        self.filter_data()
        self.ui.filterBtn.clicked.connect(self.filter_data)
        self.ui.filterNameInput.textChanged.connect(lambda: self.make_capital(self.ui.filterNameInput))

        self.ui.printBtn.clicked.connect(self.openPrintMemo)
        self.ui.saveBtn.clicked.connect(self.save_xlsx)

        self.auto_completer()

        self.update_setting_font()
        data_save_signals.data_saved.connect(self.update_setting_font)

    def update_setting_font(self):
        session = self.Session()
        setting = session.query(SettingModel).first()
        setting_font = QtGui.QFont()
        setting_font.setFamily(setting.font)
        setting_font.setPointSize(12)
        self.ui.filterNameInput.setFont(setting_font)

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
            search_name = self.ui.filterNameInput.text()
            entry_index = self.ui.accountNameSelect.currentIndex()
            entry_name = {0: 'all_accounting', 1: 'paid_to_seller',
                          2: 'get_paid_from_buyer', 3: 'capital_withdrawal',
                          4: 'capital_deposit', 5: 'borrowing',
                          6: 'loan_repayment', 7: 'salary',
                          8: 'other_cost', 9: 'mosque', 10: 'somiti', 11: 'other_cost_voucher'
                          }.get(entry_index, 'all_accounting')
            start_date = self.ui.startDateInput.date().toPyDate()
            end_date = self.ui.endDateInput.date().toPyDate()

            # Retrieve data from the database
            session = self.Session()
            query = session.query(DealerModel).filter(DealerModel.date.between(start_date, end_date))
            if entry_name != 'all_accounting':
                query = query.filter(DealerModel.entry_name.ilike(f"%{entry_name}%"))
            if entry_name:
                query = query.filter(DealerModel.name.ilike(f"%{search_name}%"))
            all_entries = query.all()

            # Clear existing table data
            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.setRowCount(0)

            # Populate the table with queried data
            self.ui.receivedAmount.setText(str(0))
            self.ui.paidAmount.setText(str(0))
            row = 0
            for entry in all_entries:
                entry_name = {'paid_to_seller': "বিক্রেতা কে প্রদান", 'get_paid_from_buyer': "ক্রেতা থেকে গ্রহণ",
                              'capital_withdrawal': "মুনাফা উত্তোলন", 'capital_deposit': "মূলধন জমা",
                              'borrowing': "ঋণ গ্রহণ", 'loan_repayment': "ঋণ পরিশোধ",
                              'salary': "বেতন / মজুরি প্রদান", 'other_cost': "অন্যান্য খরচ", 'mosque': 'মসজিদ/মাদ্রাসা',
                              'somiti': 'সমিতি', 'other_cost_voucher': 'অন্যান্য(ভাউচার)'
                              }.get(entry.entry_name.strip(), "অন্যান্য খরচ")
                self.ui.tableWidget.insertRow(row)
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(entry.id)))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(entry.date)))
                self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(entry_name)))
                self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(entry.name)))
                self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(entry.receiving_amount)))
                self.ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(entry.paying_amount)))
                self.ui.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(entry.entry_by)))

                delete_button = QtWidgets.QPushButton("")
                delete_icon = QtGui.QIcon("./images/delete.png")  # Path to your delete icon
                delete_button.setIcon(delete_icon)
                delete_button.setIconSize(QtCore.QSize(24, 24))  # Set icon size if needed
                delete_button.setStyleSheet("background-color: white; border: none;margin-left:50px;")  # Set wh
                delete_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                delete_button.clicked.connect(lambda _, r=row: self.delete_row(r))
                self.ui.tableWidget.setCellWidget(row, 7, delete_button)

                old_receivedAmount = int(self.ui.receivedAmount.text())
                self.ui.receivedAmount.setText(str(old_receivedAmount + int(entry.receiving_amount)))
                old_paidAmount = int(self.ui.paidAmount.text())
                self.ui.paidAmount.setText(str(old_paidAmount + int(entry.paying_amount)))
                row += 1
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "seller Profile Error", f"An error occurred while filtering data: {e}")

    def delete_row(self, row):
        if self.user_role == "editor":
            QtWidgets.QMessageBox.warning(None, "Delete Error", f"ডিলিট করার একসেস নেই..")
            return
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
                entry_id = self.ui.tableWidget.item(row, 0).text()
                session = self.Session()
                entry = session.query(DealerModel).filter(DealerModel.id == entry_id).one()
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
                self.ui.tableWidget.removeRow(row)
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Delete Error", f"An error occurred while deleting the row: {e}")
        data_save_signals.data_saved.emit()

    def update_capital(self, paying_amount, receiving_amount):
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
            delete_button = self.ui.tableWidget.cellWidget(row, 6)
            if delete_button is not None:
                delete_button.clicked.disconnect()
                delete_button.clicked.connect(lambda _, r=row: self.delete_row(r))

    def reconnect_delete_buttons(self):
        # Reconnect all delete buttons after a row is deleted
        row_count = self.ui.tableWidget.rowCount()
        for row in range(row_count):
            delete_button = self.ui.tableWidget.cellWidget(row, 6)
            if delete_button is not None:
                delete_button.clicked.disconnect()
                delete_button.clicked.connect(lambda _, r=row: self.delete_row(r))

    def open_entry_form(self):
        self.dialog = QtWidgets.QDialog()
        self.ui_form = Ui_CostEntry()
        self.ui_form.setupUi(self.dialog)
        self.ui_form.addBtn.clicked.connect(self.accept_information)
        self.ui_form.cancelBtn.clicked.connect(self.dialog.close)
        self.dialog.exec()

    def accept_information(self):
        try:
            session = self.Session()
            entry_index = self.ui_form.entryName.currentIndex()
            entry_name = {
                0: 'paid_to_seller', 1: 'get_paid_from_buyer',
                2: 'capital_withdrawal', 3: 'capital_deposit',
                4: 'borrowing', 5: 'loan_repayment',
                6: 'salary', 7: 'other_cost', 8: 'mosque', 9: 'somiti', 10: 'other_cost_voucher'
            }.get(entry_index, 'other_cost')

            payerName = self.ui_form.payerName.text().strip()
            receiverName = self.ui_form.receiverName.text().strip()
            entry_date = self.ui_form.entryDate.date().toPyDate()
            amount = self.ui_form.amount.text().strip()
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
                # DealerModel
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

            elif entry_name == 'salary' or entry_name == 'other_cost' or entry_name == 'mosque' or entry_name == 'somiti' or entry_name == 'other_cost_voucher':
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


    def openPrintMemo(self):
        try:
            self.print_window = QtWidgets.QWidget()
            self.ui_form = Ui_Form()
            self.ui_form.setupUi(self.print_window)

            # Table Update
            column_count = self.ui.tableWidget.columnCount()
            column_count -= 2
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
            printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterMode.HighResolution)
            printer.setPageSize(QtGui.QPageSize(QtGui.QPageSize.PageSizeId.A4))  # Set paper size to A4
            # Open print dialog
            print_dialog = QtPrintSupport.QPrintDialog(printer)
            if print_dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                painter = QtGui.QPainter(printer)
                # Render the print window content to the printer
                painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)  # Improve rendering quality
                # Calculate the scaling factor
                dpi_x = printer.logicalDpiX()  # Printer DPI in X direction
                dpi_y = printer.logicalDpiY()  # Printer DPI in Y direction
                scale_x = dpi_x / 96.0  # Assume screen DPI is 96
                scale_y = dpi_y / 96.0
                # Apply scaling to the painter
                painter.scale(scale_x, scale_y)
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

    def show_error_message(self, message):
        """Helper method to show error message."""
        error_dialog = QtWidgets.QMessageBox(self.dialog)
        error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        error_dialog.setWindowTitle("Input Error")
        error_dialog.setText(message)
        error_dialog.exec()
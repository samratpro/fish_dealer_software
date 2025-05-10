import math
from PyQt6 import QtCore
from models import *
from datetime import datetime
from PyQt6.QtCore import QDate
from features.data_save_signals import data_save_signals
from PyQt6.QtGui import QIcon
from features.printmemo import Print_Form
from PyQt6 import QtWidgets, QtGui, QtPrintSupport
from PyQt6.QtWidgets import QFileDialog, QHeaderView
import xlsxwriter
from PyQt6.QtGui import QFont, QFontDatabase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from ui.sellerProfileView_ui import UI_sellerprofileView  # Make sure to import the UI class

class SellerProfileView(QtWidgets.QWidget):

    def __init__(self, seller_name, phone, address, session, user_role, parent=None):
        super(SellerProfileView, self).__init__(parent)
        self.setup_database()  # First setup database
        self.seller_name = seller_name
        self.phone = phone
        self.address = address
        self.session = session
        self.ui = UI_sellerprofileView()  # Instantiate the UI class
        self.ui.setupUi(self)
        self.setup_ui()
        self.user_role = user_role



    def setup_database(self):
        self.Base = declarative_base()
        self.engine = create_engine('sqlite:///business.db')  # change db url
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()


    def setup_ui(self):
        self.setWindowTitle(f"{self.seller_name} - এর জন্য লেনদেন")
        self.setWindowIcon(QIcon("images/logo.png"))
        self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.ui.tableWidget.horizontalHeader().setMinimumSectionSize(170)
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

        self.ui.nameLabel.setText(self.seller_name)

        self.ui.printBtn.clicked.connect(self.openPrintMemo)
        self.ui.saveBtn.clicked.connect(self.save_xlsx)

        self.apply_bangla_font()

    def apply_bangla_font(self):
        font_id = QFontDatabase.addApplicationFont("font/nato.ttf")
        custom_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font = QFont(custom_font_family, 13)  # Font size 14
        self.ui.tableWidget.horizontalHeader().setFont(custom_font)
        self.ui.tableWidget.setStyleSheet("""QHeaderView::section, QHeaderView{
                                             background-color: #2D221B;
                                             color: white;
                                             font-size: 11pt; 
                                             text-align: center;
                                             height:35px;
                                             }
                                       """)
        self.ui.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.tableWidget.setFont(custom_font)
        self.ui.tableWidget.verticalHeader().setFont(custom_font)
        self.ui.startDateLabel.setFont(custom_font)
        self.ui.endDateLabel.setFont(custom_font)
        self.ui.filterLabel.setFont(custom_font)
        self.ui.filterBtn.setFont(custom_font)
        self.ui.saveBtn.setFont(custom_font)
        self.ui.printBtn.setFont(custom_font)
        self.ui.amount.setFont(custom_font)
        self.ui.tableWidget.viewport().update()

    def filter_data(self):
        try:
            def custom_int(data):
                try:
                    data = int(data)
                    return data
                except:
                    return 0

            start_date = self.ui.startDateInput.date().toPyDate()
            end_date = self.ui.endDateInput.date().toPyDate()

            # Retrieve data from the database
            sellers = (self.session.query(SellingModel).filter(
                SellingModel.seller_name == self.seller_name,  # Match seller name
                SellingModel.date.between(start_date, end_date)  # Date range filter
            ).all())

            # Clear existing table data
            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.setRowCount(0)

            # Populate the table with queried data
            row = 0
            for seller in sellers:
                print(f"Filtering for seller: {self.seller_name}, Start Date: {start_date}, End Date: {end_date}")
                self.ui.tableWidget.insertRow(row)
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(seller.vouchar_no)))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(seller.seller_name)))
                self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(seller.date)))
                self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(seller.sell_amount)))
                self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(seller.commission_amount)))
                self.ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(seller.total_cost_amount)))
                self.ui.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(seller.entry_by)))

                cash_memo_print_btn = QtWidgets.QPushButton("")
                print_icon = QtGui.QIcon("./images/printer.png" )
                cash_memo_print_btn.setIcon(print_icon)
                cash_memo_print_btn.setIconSize(QtCore.QSize(24, 24))
                cash_memo_print_btn.setStyleSheet(
                    "background-color: white; border: none; margin-left: 50px;")  # Set background color and border
                cash_memo_print_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                cash_memo_print_btn.clicked.connect(lambda: self.print_cash_memo(
                    seller.vouchar_no,
                    seller.seller_name,
                    seller.sell_amount,
                    seller.commission_amount,
                    seller.total_cost_amount,
                    seller.date
                ))
                self.ui.tableWidget.setCellWidget(row, 7, cash_memo_print_btn)

                old_amount = custom_int(self.ui.amount.text())
                self.ui.amount.setText(str(old_amount + custom_int(seller.sell_amount)))

                delete_button = QtWidgets.QPushButton("")
                delete_icon = QtGui.QIcon("./images/delete.png")  # Path to your delete icon
                delete_button.setIcon(delete_icon)
                delete_button.setIconSize(QtCore.QSize(24, 24))  # Set icon size if needed
                delete_button.setStyleSheet("background-color: white; border: none;margin-left:50px;")  # Set wh
                delete_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                delete_button.clicked.connect(lambda _, r=row: self.delete_row(r))
                self.ui.tableWidget.setCellWidget(row, 8, delete_button)
                row += 1
        except Exception as e:
            print(f"seller Profile View Error in filter_data: {e}")
            QtWidgets.QMessageBox.critical(None, "seller Profile View Error",
                                           f"An error occurred while filtering data: {e}")

    def delete_row(self, row):
        def custom_int(data):
            try:
                data = int(data)
                return data
            except:
                return 0
        if self.user_role == "editor":
            QtWidgets.QMessageBox.warning(None, "Delete Error", "এই প্রোফাইলে ডিলিট করার একসেস নেই..")
            return

        try:
            reply = QtWidgets.QMessageBox.question(
                None,
                'মুছে ফেলা নিশ্চিত করুন',
                'আপনি কি নিশ্চিত মুছে ফেলতে চান?',
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                QtWidgets.QMessageBox.StandardButton.No
            )

            # If the user confirms, proceed with deletion
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                session = self.Session()
                vouchar_no = self.ui.tableWidget.item(row, 0).text()
                seller_name = self.ui.tableWidget.item(row, 1).text()
                sell_amount = int(self.ui.tableWidget.item(row, 3).text())
                commission = int(self.ui.tableWidget.item(row, 4).text())
                total_cost_amount = int(self.ui.tableWidget.item(row, 5).text())

                # Fetch the seller profile
                seller_profile = session.query(SellerProfileModel).filter(
                    SellerProfileModel.seller_name == seller_name).first()

                if seller_profile:
                    seller_profile.total_commission -= commission
                    seller_profile.total_receivable -= (sell_amount - total_cost_amount)
                else:
                    QtWidgets.QMessageBox.warning(None, "Not Found", "Seller Profile Not Found")
                    return

                # Delete related BuyingModel records and update BuyerProfileModel.total_payable
                buying_model = session.query(BuyingModel).filter(BuyingModel.vouchar_no == vouchar_no).all()
                for buying in buying_model:
                    buyer_profile = session.query(BuyerProfileModel).filter(
                        BuyerProfileModel.buyer_name == buying.buyer_name).first()

                    if buyer_profile:
                        buyer_profile.total_payable -= buying.buying_amount
                    else:
                        QtWidgets.QMessageBox.warning(None, "Not Found",
                                                      f"Buyer Profile Not Found for {buying.buyer_name}")

                    session.delete(buying)

                # Delete related SellingModel records
                session.query(SellingModel).filter(SellingModel.vouchar_no == vouchar_no).delete()

                session.commit()
                self.ui.tableWidget.removeRow(row)
                old_amount = custom_int(self.ui.amount.text())
                self.ui.amount.setText(str(old_amount - sell_amount))

        except Exception as ops:
            print(f'Error in delete of buyer profile: ({ops})')
        finally:
            data_save_signals.data_saved.emit()

    def print_cash_memo(self, vouchar_no, seller_name, sell_amount, commission_amount, total_cost_amount, date):
        print(vouchar_no, seller_name, sell_amount, commission_amount, total_cost_amount)
        session = self.Session()
        seller_data = session.query(SellerProfileModel).filter(SellerProfileModel.seller_name == seller_name).one_or_none()

        # Fetch all buyers for the given voucher number
        buying_model = session.query(BuyingModel).filter(BuyingModel.vouchar_no == vouchar_no)
        buyers = buying_model.all()

        total_rows = len(buyers)
        rows_per_page = 13
        total_pages = math.ceil(total_rows / rows_per_page)
        total_pages = 1 if total_pages == 0 else total_pages

        try:
            for page in range(total_pages):
                # ✅ Create the print window
                self.ui_print_form = Print_Form()
                self.ui_print_form.ui.tableWidget.horizontalHeader().setMinimumSectionSize(121)
                self.ui_print_form.ui.tableWidget.horizontalHeader().setSectionResizeMode(
                    QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

                # ✅ Set up labels with corresponding values
                self.ui_print_form.ui.memoLabel.setText("বিক্রেতার ক্যাশমেমো")
                self.ui_print_form.ui.name.setText(seller_name)
                self.ui_print_form.ui.date.setText(str(date))
                self.ui_print_form.ui.address.setText(str(seller_data.address))
                self.ui_print_form.ui.mobile.setText(str(seller_data.phone))
                self.ui_print_form.ui.commission.setText(str(commission_amount))
                self.ui_print_form.ui.totalTaka.setText(str(total_cost_amount+sell_amount))
                self.ui_print_form.ui.totalCost_raw.setText(str(total_cost_amount))
                self.ui_print_form.ui.totalCost.setText(str(total_cost_amount))
                self.ui_print_form.ui.finalTaka.setText(str(sell_amount))
                self.ui_print_form.ui.recevied_frame.setVisible(False)

                headers = ["ক্রেতার নাম", "মাছের নাম", "রেট", "কাঁচা ওজন", "পাকা ওজন", "দাম"]

                self.ui_print_form.ui.tableWidget.verticalHeader().setVisible(False)
                self.ui_print_form.ui.tableWidget.setColumnCount(len(headers))
                self.ui_print_form.ui.tableWidget.setHorizontalHeaderLabels(headers)

                # ✅ Set up rows for the current page
                start_index = page * rows_per_page
                end_index = min(start_index + rows_per_page, total_rows)
                page_buyers = buyers[start_index:end_index]

                self.ui_print_form.ui.tableWidget.setRowCount(len(page_buyers))

                # ✅ Copy table data for the current page
                row = 0
                for buyer in page_buyers:
                    self.ui_print_form.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(buyer.buyer_name)))
                    self.ui_print_form.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(buyer.fish_name)))
                    self.ui_print_form.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(buyer.fish_rate)))
                    self.ui_print_form.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(buyer.raw_weight)))
                    self.ui_print_form.ui.tableWidget.setItem(row, 4,
                                                              QtWidgets.QTableWidgetItem(str(buyer.final_weight)))
                    self.ui_print_form.ui.tableWidget.setItem(row, 5,
                                                              QtWidgets.QTableWidgetItem(str(buyer.buying_amount)))
                    row += 1

                # ✅ Show the print window
                self.ui_print_form.show()

                # ✅ Set up the printer
                printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterMode.HighResolution)
                printer.setPageSize(QtGui.QPageSize(QtGui.QPageSize.PageSizeId.A4))

                # ✅ Open print preview dialog
                preview_dialog = QtPrintSupport.QPrintPreviewDialog(printer)
                preview_dialog.paintRequested.connect(self.renderPrintPreview)
                preview_dialog.exec()

        except Exception as e:
            print(f"An error occurred: {e}")

    def openPrintMemo(self):
        total_rows = self.ui.tableWidget.rowCount()
        rows_per_page = 13
        total_pages = math.ceil(total_rows / rows_per_page)
        total_pages = 1 if total_pages == 0 else total_pages
        for page in range(total_pages):
            try:
                # ✅ Create the print window
                self.ui_print_form = Print_Form()
                self.ui_print_form.ui.memoLabel.setText("বিক্রেতার ক্যাশমেমো")
                self.ui_print_form.ui.name.setText(str(self.ui.nameLabel.text()))
                self.ui_print_form.ui.date.setText(str(self.ui.startDateInput.text()))
                self.ui_print_form.ui.finalTaka.setText(str(self.ui.amount.text()))
                self.ui_print_form.ui.mobile.setText(str(self.phone))
                self.ui_print_form.ui.address.setText(str(self.address))

                self.ui_print_form.ui.recevied_frame.setVisible(False)

                # ✅ Define columns to exclude
                excluded_columns = {0, 6, 7, 8}
                column_count = self.ui.tableWidget.columnCount()
                headers = [self.ui.tableWidget.horizontalHeaderItem(i).text() for i in range(column_count) if
                           i not in excluded_columns]

                self.ui_print_form.ui.tableWidget.verticalHeader().setVisible(False)
                self.ui_print_form.ui.tableWidget.setColumnCount(len(headers))
                self.ui_print_form.ui.tableWidget.setHorizontalHeaderLabels(headers)
                # ✅ Set the row count for current page
                start_row = page * rows_per_page
                end_row = min(start_row + rows_per_page, total_rows)
                self.ui_print_form.ui.tableWidget.setRowCount(end_row - start_row)

                # ✅ Copy table data excluding specified columns
                for row_idx in range(start_row, end_row):
                    new_col_idx = 0
                    for col_idx in range(column_count):
                        if col_idx in excluded_columns:
                            continue  # Skip excluded columns
                        item = self.ui.tableWidget.item(row_idx, col_idx)
                        if item:
                            self.ui_print_form.ui.tableWidget.setItem(row_idx-start_row, new_col_idx,
                                                                      QtWidgets.QTableWidgetItem(item.text()))
                        new_col_idx += 1

                # ✅ Show the print window
                self.ui_print_form.show()

                # ✅ Set up the printer
                printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterMode.HighResolution)
                printer.setPageSize(QtGui.QPageSize(QtGui.QPageSize.PageSizeId.A4))  # Set paper size to A4

                # ✅ Open print preview dialog
                preview_dialog = QtPrintSupport.QPrintPreviewDialog(printer)
                preview_dialog.paintRequested.connect(self.renderPrintPreview)  # Connect to the custom render function
                preview_dialog.exec()

            except Exception as e:
                print(f"An error occurred: {e}")

    def renderPrintPreview(self, printer):
        """
        Custom function to render the print window content for the preview.
        """
        try:
            # ✅ Use QPainter to render the print content
            painter = QtGui.QPainter(printer)

            # ✅ Improve rendering quality
            painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)

            # ✅ Calculate the scaling factor
            dpi_x = printer.logicalDpiX()  # Printer DPI in X direction
            dpi_y = printer.logicalDpiY()  # Printer DPI in Y direction
            scale_x = dpi_x / 96.0  # Assume screen DPI is 96
            scale_y = dpi_y / 96.0

            # ✅ Apply scaling to the painter
            painter.scale(scale_x, scale_y)

            # ✅ Render the print window content
            self.ui_print_form.render(painter)

            # ✅ Finish painting
            painter.end()

        except Exception as e:
            print(f"An error occurred during print preview: {e}")



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
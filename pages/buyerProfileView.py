import math
from PyQt6 import QtCore
from models import BuyingModel
from datetime import datetime
from PyQt6.QtCore import QDate
from features.data_save_signals import data_save_signals
from PyQt6.QtGui import QIcon
from features.printmemo import Print_Form
from PyQt6 import QtWidgets, QtGui, QtPrintSupport
from PyQt6.QtWidgets import QFileDialog, QHeaderView
import xlsxwriter
from PyQt6.QtGui import QFont, QFontDatabase
from ui.buyerProfileView_ui import UI_buyerprofileView

class BuyerProfileView(QtWidgets.QWidget):

    def __init__(self, buyer_name, phone, session, parent=None):
        super(BuyerProfileView, self).__init__(parent)
        self.buyer_name = buyer_name
        self.phone = phone
        self.session = session
        self.ui = UI_buyerprofileView()  # Instantiate the UI class
        self.ui.setupUi(self)  # Pass self to the setupUi method
        self.setup_ui()


    def setup_ui(self):
        self.setWindowTitle(f"{self.buyer_name} - এর জন্য লেনদেন")
        self.setWindowIcon(QIcon("images/logo.png"))
        self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.ui.tableWidget.horizontalHeader().setMinimumSectionSize(150)
        self.ui.tableWidget.verticalHeader().setVisible(False)
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
        self.ui.printBtn.clicked.connect(self.openPrintMemo)
        self.ui.saveBtn.clicked.connect(self.save_xlsx)
        self.ui.nameLabel.setText(self.buyer_name)
        self.apply_bangla_font()

    def apply_bangla_font(self):
        font_id = QFontDatabase.addApplicationFont("font/nato.ttf")
        custom_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font = QFont(custom_font_family, 13)  # Font size 13
        # Apply font to table headers
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
        # Apply font to table and other widgets
        self.ui.tableWidget.setFont(custom_font)
        self.ui.tableWidget.verticalHeader().setFont(custom_font)
        self.ui.startDateLabel.setFont(custom_font)
        self.ui.endDateLabel.setFont(custom_font)
        self.ui.filterLabel.setFont(custom_font)
        self.ui.filterBtn.setFont(custom_font)
        self.ui.saveBtn.setFont(custom_font)
        self.ui.printBtn.setFont(custom_font)
        self.ui.nameLabel.setFont(custom_font)
        self.setFont(custom_font)
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
            # buyers= self.session.query(BuyingModel).filter_by(buyer_name=self.buyer_name).all()
            print("Buyer name : ", self.buyer_name)
            buyers = (self.session.query(BuyingModel).filter(
                    BuyingModel.buyer_name == self.buyer_name
                ).all()
            )
            print("buyers 0 : ", buyers)

            buyers = (self.session.query(BuyingModel).filter(
                    BuyingModel.buyer_name == self.buyer_name,  # Match buyer name
                    BuyingModel.date.between(start_date, end_date)  # Date range filter
                ).all()
            )

            # Log retrieved data for debugging

            print("Buyers : ", buyers)

            # Clear existing table data
            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.setRowCount(0)

            # Populate the table with queried data
            row = 0
            for buyer in buyers:
                self.ui.tableWidget.insertRow(row)
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(buyer.vouchar_no)))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(buyer.seller_name)))
                self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(buyer.date)))
                self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(buyer.fish_name)))
                self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(buyer.fish_rate)))
                self.ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(buyer.raw_weight)))
                self.ui.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(buyer.final_weight)))
                self.ui.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(buyer.buying_amount)))
                self.ui.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(buyer.buyer_name)))
                self.ui.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(str(buyer.entry_by)))
                old_amount = custom_int(self.ui.amount.text())
                self.ui.amount.setText(str(old_amount+custom_int(buyer.buying_amount)))
                row += 1
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Buyer Profile View Error", f"An error occurred while filtering data: {e}")

    def openPrintMemo(self):
        total_rows = self.ui.tableWidget.rowCount()
        rows_per_page = 13
        total_pages = math.ceil(total_rows / rows_per_page)
        total_pages = 1 if total_pages == 0 else total_pages

        for page in range(total_pages):
            try:
                # ✅ Create the print window
                self.ui_print_form = Print_Form(min_section_size=120)
                self.ui_print_form.ui.memoLabel.setText("ক্রেতার ক্যাশমেমো")
                self.ui_print_form.ui.name.setText(str(self.ui.nameLabel.text()))
                self.ui_print_form.ui.date.setText(str(self.ui.startDateInput.text()))
                self.ui_print_form.ui.mobile.setText(str(self.phone))
                self.ui_print_form.ui.finalTaka.setText(str(self.ui.amount.text()))
                self.ui_print_form.ui.recevied_frame.setVisible(False)

                # ✅ Define columns to exclude
                excluded_columns = {0, 5, 8, 9}
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
                            self.ui_print_form.ui.tableWidget.setItem(row_idx - start_row, new_col_idx,
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

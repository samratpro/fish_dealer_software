from PyQt6 import QtCore
from models import SellingModel, Base
from datetime import datetime
from PyQt6.QtCore import QDate
from features.data_save_signals import data_save_signals
from PyQt6.QtGui import QIcon
from features.printmemo import Print_Form
from PyQt6 import QtWidgets, QtGui, QtPrintSupport
from PyQt6.QtWidgets import QFileDialog, QHeaderView
import xlsxwriter
from PyQt6.QtGui import QFont, QFontDatabase

class SellerProfileView(QtWidgets.QWidget):

    def __init__(self, seller_name, phone, address, session, parent=None):
        super(SellerProfileView, self).__init__(parent)
        self.seller_name = seller_name
        self.phone = phone
        self.address = address
        self.session = session
        self.setupUi()

    def setupUi(self):
        try:
            self.setWindowTitle(f"{self.seller_name} - এর জন্য লেনদেন")
            self.setWindowIcon(QIcon("images/logo.png"))
            self.resize(935, 570)
            self.setMinimumSize(QtCore.QSize(300, 0))
            self.setStyleSheet("""*{text-align: left;}
                                     QLineEdit{border-radius:10px;border:1px solid #B8B8B8;padding:2px;}
                                     QPushButton{background-color:#150E0A;color:white;
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
            self.cashReportMain_Layout = QtWidgets.QVBoxLayout(self)
            self.cashReportMain_Layout.setContentsMargins(15, 15, 15, 15)
            self.cashReportMain_Layout.setSpacing(6)
            self.cashReportMain_Layout.setObjectName("cashReportMain_Layout")

            self.cashReportHeader = QtWidgets.QWidget(parent=self)
            self.cashReportHeader.setMaximumSize(QtCore.QSize(16777215, 80))
            font = QtGui.QFont()
            font.setFamily("Arial")
            self.cashReportHeader.setFont(font)
            self.cashReportHeader.setObjectName("cashReportHeader")
            self.cashReportHeader_Layout = QtWidgets.QHBoxLayout(self.cashReportHeader)
            self.cashReportHeader_Layout.setContentsMargins(0, 0, 0, 0)
            self.cashReportHeader_Layout.setSpacing(0)

            # Add components to the header
            self.startDateFrame = QtWidgets.QFrame(parent=self.cashReportHeader)
            self.startDateFrame.setMinimumSize(QtCore.QSize(140, 0))
            self.startDateFrame.setMaximumSize(QtCore.QSize(250, 16777215))
            font = QtGui.QFont()
            font.setFamily("Arial")
            self.startDateFrame.setFont(font)
            self.startDateFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.startDateFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.startDateFrame.setObjectName("startDateFrame")
            self.startDateFrame_Layout = QtWidgets.QVBoxLayout(self.startDateFrame)
            self.startDateFrame_Layout.setContentsMargins(0, 0, 0, 0)
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
            self.cashReportHeader_Layout.addWidget(self.startDateFrame, 0, QtCore.Qt.AlignmentFlag.AlignLeft)

            self.endDateFrame = QtWidgets.QFrame(parent=self.cashReportHeader)
            self.endDateFrame.setMinimumSize(QtCore.QSize(140, 0))
            self.endDateFrame.setMaximumSize(QtCore.QSize(250, 16777215))
            font = QtGui.QFont()
            font.setFamily("Arial")
            self.endDateFrame.setFont(font)
            self.endDateFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.endDateFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.endDateFrame.setObjectName("endDateFrame")
            self.endDateFrame_Layout = QtWidgets.QVBoxLayout(self.endDateFrame)
            self.endDateFrame_Layout.setContentsMargins(0, 0, 0, 0)
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
            self.endDateInput.setObjectName("endDateInput")
            self.endDateFrame_Layout.addWidget(self.endDateInput)
            self.cashReportHeader_Layout.addWidget(self.endDateFrame, 0, QtCore.Qt.AlignmentFlag.AlignLeft)

            self.filterActionFrame = QtWidgets.QFrame(parent=self.cashReportHeader)
            self.filterActionFrame.setMinimumSize(QtCore.QSize(100, 0))
            self.filterActionFrame.setMaximumSize(QtCore.QSize(100, 16777215))
            font = QtGui.QFont()
            font.setFamily("Arial")
            self.filterActionFrame.setFont(font)
            self.filterActionFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.filterActionFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.filterActionFrame.setObjectName("filterActionFrame")
            self.filterActionFrame_Layout = QtWidgets.QVBoxLayout(self.filterActionFrame)
            self.filterActionFrame_Layout.setContentsMargins(0, 0, 0, 0)
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
            self.cashReportHeader_Layout.addWidget(self.filterActionFrame)

            self.cashReportMain_Layout.addWidget(self.cashReportHeader)

            self.cashReportBody = QtWidgets.QWidget(parent=self)
            font = QtGui.QFont()
            font.setFamily("Arial")
            self.cashReportBody.setFont(font)
            self.cashReportBody.setObjectName("cashReportBody")
            self.cashReportBody_Layout = QtWidgets.QHBoxLayout(self.cashReportBody)
            self.cashReportBody_Layout.setContentsMargins(0, 10, 0, 0)
            self.cashReportBody_Layout.setSpacing(0)
            self.cashReportBody_Layout.setObjectName("cashReportBody_Layout")
            self.tableWidget = QtWidgets.QTableWidget(parent=self.cashReportBody)
            font = QtGui.QFont()
            font.setFamily("Arial")
            self.tableWidget.setFont(font)
            self.tableWidget.setStyleSheet("""QHeaderView::section, QHeaderView{
                                                    background-color: #2D221B;
                                                    color: white;
                                                    font-size: 12pt;
                                                    text-align: center;
                                                    }
                                                    """)
            self.tableWidget.setObjectName("tableWidget")
            self.tableWidget.setColumnCount(7)
            self.tableWidget.setRowCount(0)
            font = QtGui.QFont()
            font.setFamily("Arial")
            self.tableWidget.setFont(font)
            font.setPointSize(12)  # Set the font size to 12 points
            self.tableWidget.setFont(font)
            self.cashReportBody_Layout.addWidget(self.tableWidget)
            self.cashReportMain_Layout.addWidget(self.cashReportBody)

            self.cashReportFooter = QtWidgets.QWidget(parent=self)
            self.cashReportFooter.setMinimumSize(QtCore.QSize(0, 60))
            font = QtGui.QFont()
            font.setFamily("Arial")
            self.cashReportFooter.setFont(font)
            self.cashReportFooter.setObjectName("cashReportFooter")
            self.cashReportFooter_Layout = QtWidgets.QHBoxLayout(self.cashReportFooter)
            self.cashReportFooter_Layout.setContentsMargins(0, 20, 0, 25)
            self.cashReportFooter_Layout.setSpacing(0)
            self.cashReportFooter_Layout.setObjectName("cashReportFooter_Layout")
            self.saveBtn = QtWidgets.QPushButton(parent=self.cashReportFooter)
            self.saveBtn.setMinimumSize(QtCore.QSize(0, 30))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(12)
            self.saveBtn.setFont(font)
            self.saveBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.saveBtn.setStyleSheet("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("./icons/save.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.saveBtn.setIcon(icon1)
            self.saveBtn.setIconSize(QtCore.QSize(22, 22))
            self.saveBtn.setCheckable(True)
            self.saveBtn.setAutoExclusive(True)
            self.saveBtn.setObjectName("saveBtn")
            self.cashReportFooter_Layout.addWidget(self.saveBtn, 0, QtCore.Qt.AlignmentFlag.AlignLeft)

            self.nameLabel = QtWidgets.QLabel(parent=self.cashReportFooter)
            self.nameLabel.setMinimumSize(QtCore.QSize(70, 0))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.nameLabel.setFont(font)
            self.nameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.nameLabel.setObjectName("nameLabel")
            self.cashReportFooter_Layout.addWidget(self.nameLabel, 0, QtCore.Qt.AlignmentFlag.AlignLeft)

            self.amount = QtWidgets.QLabel(parent=self.cashReportFooter)
            self.amount.setMinimumSize(QtCore.QSize(150, 0))
            self.amount.setStyleSheet("QLabel{border:1px solid #828282;background-color:white;border-radius:10px}")
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.amount.setFont(font)
            self.amount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.amount.setObjectName("receivedAmount")
            self.cashReportFooter_Layout.addWidget(self.amount, 0, QtCore.Qt.AlignmentFlag.AlignLeft)


            self.printBtn = QtWidgets.QPushButton(parent=self.cashReportFooter)
            self.printBtn.setMinimumSize(QtCore.QSize(90, 30))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(12)
            self.printBtn.setFont(font)
            self.printBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.printBtn.setStyleSheet("")
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("./icons/printer.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.printBtn.setIcon(icon2)
            self.printBtn.setIconSize(QtCore.QSize(22, 22))
            self.printBtn.setCheckable(True)
            self.printBtn.setAutoExclusive(True)
            self.printBtn.setObjectName("printBtn")
            self.cashReportFooter_Layout.addWidget(self.printBtn, 0, QtCore.Qt.AlignmentFlag.AlignRight)
            self.cashReportMain_Layout.addWidget(self.cashReportFooter)

            self.retranslateUi()
        except Exception as e:
            print(f"Seller Profile View Error in setupUi: {e}")
            QtWidgets.QMessageBox.critical(None, "Seller Profile View Error", f"An error occurred while setting up the UI: {e}")

    def retranslateUi(self):
        try:
            _translate = QtCore.QCoreApplication.translate
            # self.setWindowTitle(_translate("cashReportMain", "Form"))
            self.startDateLabel.setText(_translate("cashReportMain", "তারিখ"))
            self.startDateInput.setDisplayFormat(_translate("cashReportMain", "dd/mm/yyyy"))
            self.endDateLabel.setText(_translate("cashReportMain", "শেষ তারিখ"))
            self.endDateInput.setDisplayFormat(_translate("cashReportMain", "dd/mm/yyyy"))
            self.filterLabel.setText(_translate("cashReportMain", "অ্যাকশন"))
            self.filterBtn.setText(_translate("cashReportMain", "ফিল্টার"))

            # Ensure the table has the correct number of columns
            headers = [
                "ভাউচার নং", "নাম", "তারিখ", "বিক্রি পরিমান", "কমিশন",
                "মোট খরচ", "এন্ট্রি বাই"
            ]
            for i, header in enumerate(headers):
                item = self.tableWidget.horizontalHeaderItem(i)
                if item is None:
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setHorizontalHeaderItem(i, item)
                item.setText(_translate("cashReportMain", header))

            self.saveBtn.setText(_translate("cashReportMain", "সেভ এক্সেল"))
            self.printBtn.setText(_translate("cashReportMain", "প্রিন্ট"))



            self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
            self.tableWidget.horizontalHeader().setMinimumSectionSize(200)
            self.tableWidget.verticalHeader().setVisible(False)
            # Set current date ****************
            self.startDateInput.setDisplayFormat("dd/MM/yyyy")
            self.endDateInput.setDisplayFormat("dd/MM/yyyy")
            self.today_date_raw = datetime.now()
            self.today_date = self.today_date_raw.strftime("%d/%m/%Y").lstrip('0').replace('/0', '/')
            self.qdate_today = QDate.fromString(self.today_date, "d/M/yyyy")
            self.startDateInput.setDate(self.qdate_today)
            self.endDateInput.setDate(self.qdate_today)
        except Exception as ops:
            print(f'Error in retranslateUi: {ops}')

        data_save_signals.data_saved.connect(self.filter_data)
        self.filter_data()
        self.filterBtn.clicked.connect(self.filter_data)

        self.nameLabel.setText(self.seller_name)

        self.printBtn.clicked.connect(self.openPrintMemo)
        self.saveBtn.clicked.connect(self.save_xlsx)

        self.apply_bangla_font()

    def apply_bangla_font(self):
        bangla_font_path = "font/nato.ttf"
        font_id = QFontDatabase.addApplicationFont(bangla_font_path)
        custom_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font = QFont(custom_font_family, 13)  # Font size 14
        self.tableWidget.horizontalHeader().setFont(custom_font)
        self.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget.setFont(custom_font)
        self.tableWidget.verticalHeader().setFont(custom_font)
        self.startDateLabel.setFont(custom_font)
        self.endDateLabel.setFont(custom_font)
        self.filterLabel.setFont(custom_font)
        self.filterBtn.setFont(custom_font)
        self.saveBtn.setFont(custom_font)
        self.printBtn.setFont(custom_font)
        self.amount.setFont(custom_font)
        self.tableWidget.viewport().update()


    def filter_data(self):
        try:
            def custom_int(data):
                try:
                    data = int(data)
                    return data
                except:
                    return 0

            start_date = self.startDateInput.date().toPyDate()
            end_date = self.endDateInput.date().toPyDate()

            # Retrieve data from the database
            # sellers = self.session.query(SellingModel).filter_by(seller_name=self.seller_name).all()
            sellers = (self.session.query(SellingModel).filter(
                                                            SellingModel.seller_name == self.seller_name,  # Match seller name
                                                            SellingModel.date.between(start_date, end_date)  # Date range filter
                                                             ).all())

            # Log retrieved data for debugging

            # Clear existing table data
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

            # Populate the table with queried data
            row = 0
            for seller in sellers:
                print(f"Filtering for seller: {self.seller_name}, Start Date: {start_date}, End Date: {end_date}")
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(seller.vouchar_no)))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(seller.seller_name)))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(seller.date)))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(seller.sell_amount)))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(seller.commission_amount)))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(seller.total_cost_amount)))
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(seller.entry_by)))
                old_amount = custom_int(self.amount.text())
                self.amount.setText(str(old_amount+custom_int(seller.sell_amount)))
                row += 1
        except Exception as e:
            print(f"seller Profile View Error in filter_data: {e}")
            QtWidgets.QMessageBox.critical(None, "seller Profile View Error", f"An error occurred while filtering data: {e}")

    def openPrintMemo(self):
        try:
            # ✅ Create the print window
            self.ui_print_form = Print_Form()
            self.ui_print_form.ui.memoLabel.setText("বিক্রেতার ক্যাশমেমো")
            self.ui_print_form.ui.name.setText(str(self.nameLabel.text()))
            self.ui_print_form.ui.date.setText(str(self.startDateInput.text()))
            self.ui_print_form.ui.finalTaka.setText(str(self.amount.text()))
            self.ui_print_form.ui.mobile.setText(str(self.phone))
            self.ui_print_form.ui.address.setText(str(self.address))

            self.ui_print_form.ui.recevied_frame.setVisible(False)

            # ✅ Define columns to exclude
            excluded_columns = {0, 6}
            column_count = self.tableWidget.columnCount()
            row_count = self.tableWidget.rowCount()
            headers = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(column_count) if
                       i not in excluded_columns]

            self.ui_print_form.ui.tableWidget.verticalHeader().setVisible(False)
            self.ui_print_form.ui.tableWidget.setColumnCount(len(headers))
            self.ui_print_form.ui.tableWidget.setHorizontalHeaderLabels(headers)
            self.ui_print_form.ui.tableWidget.setRowCount(row_count)

            # ✅ Copy table data excluding specified columns
            for row_idx in range(row_count):
                new_col_idx = 0
                for col_idx in range(column_count):
                    if col_idx in excluded_columns:
                        continue  # Skip excluded columns
                    item = self.tableWidget.item(row_idx, col_idx)
                    if item:
                        self.ui_print_form.ui.tableWidget.setItem(row_idx, new_col_idx,
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
            row_count = self.tableWidget.rowCount()
            column_count = self.tableWidget.columnCount()

            # Write headers to the first row
            headers = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(column_count)]
            for col_idx, header in enumerate(headers):
                worksheet.write(0, col_idx, header)

            # Write table data to the worksheet
            for row_idx in range(row_count):
                for col_idx in range(column_count):
                    item = self.tableWidget.item(row_idx, col_idx)
                    worksheet.write(row_idx + 1, col_idx, item.text() if item else "")

            # Close and save the workbook
            workbook.close()
            print(f"Excel file saved successfully at {file_path}")

        except Exception as e:
            print(f"An error occurred while saving Excel file: {e}")
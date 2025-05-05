from PyQt6 import QtCore
from models import *
from features.data_save_signals import data_save_signals
from PyQt6.QtGui import QFont, QFontDatabase
from sqlalchemy.sql import extract, func, case
from features.printmemo import Print_Form
from PyQt6 import QtWidgets, QtGui, QtPrintSupport
from PyQt6.QtWidgets import QFileDialog, QHeaderView
import xlsxwriter
import math


class Ui_yearlyReportPage(object):
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
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
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
        costExpenseMain.setWindowTitle(_translate("costExpenseMain", "বছরের রিপোর্ট"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("costExpenseMain", "বছর"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("costExpenseMain", "মোট কমিশন"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("costExpenseMain", "মোট খরচ"))
        self.saveBtn.setText(_translate("costExpenseMain", "সেভ এক্সেল"))
        self.printBtn.setText(_translate("costExpenseMain", "প্রিন্ট"))

        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(250)
        self.tableWidget.verticalHeader().setVisible(False)
        self.filter_data()
        data_save_signals.data_saved.connect(self.filter_data)
        self.printBtn.clicked.connect(self.openPrintMemo)
        self.saveBtn.clicked.connect(self.save_xlsx)

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
            # Start a new session
            session = self.Session()

            # Define fiscal year calculation for SellingModel
            selling_fiscal_year = case(
                (extract('month', SellingModel.date) >= 7, extract('year', SellingModel.date)),
                else_=extract('year', SellingModel.date) - 1
            ).label('fiscal_year')

            # Query data from SellingModel (for Commission) grouped by fiscal year
            commission_data = (
                session.query(
                    selling_fiscal_year,
                    func.sum(SellingModel.commission_amount).label('total_commission')
                )
                .group_by(selling_fiscal_year)
                .all()
            )

            # Define fiscal year calculation for DealerModel
            dealer_fiscal_year = case(
                (extract('month', DealerModel.date) >= 7, extract('year', DealerModel.date)),
                else_=extract('year', DealerModel.date) - 1
            ).label('fiscal_year')

            # Query data from DealerModel (for Cost) grouped by fiscal year
            cost_data = (
                session.query(
                    dealer_fiscal_year,
                    func.sum(DealerModel.paying_amount).label('total_cost')
                )
                .group_by(dealer_fiscal_year)
                .all()
            )

            # Combine the data from both queries into a dictionary for easier handling
            yearly_data = {}
            for row in commission_data:
                fiscal_year = int(row.fiscal_year)
                if fiscal_year not in yearly_data:
                    yearly_data[fiscal_year] = {"commission": 0, "cost": 0}
                yearly_data[fiscal_year]["commission"] = row.total_commission or 0

            for row in cost_data:
                fiscal_year = int(row.fiscal_year)
                if fiscal_year not in yearly_data:
                    yearly_data[fiscal_year] = {"commission": 0, "cost": 0}
                yearly_data[fiscal_year]["cost"] = row.total_cost or 0

            # Sort data by fiscal year
            sorted_years = sorted(yearly_data.keys())

            # Clear the table
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)

            # Populate the table with the combined data
            for row_index, fiscal_year in enumerate(sorted_years):
                self.tableWidget.insertRow(row_index)
                fiscal_year_label = f"{fiscal_year}-{fiscal_year + 1}"  # Format as "2024-2025"
                self.tableWidget.setItem(row_index, 0, QtWidgets.QTableWidgetItem(fiscal_year_label))  # Fiscal Year
                self.tableWidget.setItem(row_index, 1,
                                         QtWidgets.QTableWidgetItem(
                                             str(yearly_data[fiscal_year]["commission"])))  # Commission
                self.tableWidget.setItem(row_index, 2,
                                         QtWidgets.QTableWidgetItem(str(yearly_data[fiscal_year]["cost"])))  # Cost

            # Commit and close the session
            session.close()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Yearly Report Error",
                                           f"An error occurred while filtering data: {str(e)}")

    def openPrintMemo(self):
        total_rows = self.tableWidget.rowCount()
        rows_per_page = 11
        total_pages = math.ceil(total_rows / rows_per_page)
        total_pages = 1 if total_pages == 0 else total_pages
        for page in range(total_pages):
            try:
                # ✅ Create the print window
                self.ui_print_form = Print_Form()
                self.ui_print_form.ui.memoLabel.setText("কমিশন ও খরচের রিপোর্ট")
                self.ui_print_form.ui.label_2.setVisible(False)
                self.ui_print_form.ui.label_3.setVisible(False)
                self.ui_print_form.ui.label_4.setVisible(False)
                self.ui_print_form.ui.label_5.setVisible(False)
                self.ui_print_form.ui.label_6.setVisible(False)
                self.ui_print_form.ui.label_7.setVisible(False)
                self.ui_print_form.ui.label_11.setVisible(False)
                self.ui_print_form.ui.label_12.setVisible(False)
                self.ui_print_form.ui.label_14.setVisible(False)
                self.ui_print_form.ui.name.setVisible(False)
                self.ui_print_form.ui.mobile.setVisible(False)
                self.ui_print_form.ui.address.setVisible(False)

                self.ui_print_form.ui.recevied_frame.setVisible(False)

                # ✅ Define columns to exclude
                excluded_columns = {}
                column_count = self.tableWidget.columnCount()
                headers = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(column_count)]

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
                        # if col_idx in excluded_columns:
                        #     continue  # Skip excluded columns
                        item = self.tableWidget.item(row_idx, col_idx)
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
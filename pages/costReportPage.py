import math

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from datetime import datetime
from PyQt6.QtCore import QDate
from sqlalchemy.orm import sessionmaker, declarative_base
from models import *
from sqlalchemy import and_
from features.data_save_signals import data_save_signals
from ui.costReportPage_ui import costReport_ui
from features.printmemo import Print_Form
from PyQt6 import QtWidgets, QtGui, QtPrintSupport, QtCore
from PyQt6.QtWidgets import QFileDialog, QHeaderView
import xlsxwriter
from PyQt6.QtGui import QFont, QFontDatabase
from forms.cost_profile_edit import Profile_Edit_Form
from pages.CostProfileView import CostProfileView
import os


class CostReport(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        user = session.query(UserModel).filter(UserModel.username == self.username).one()
        self.user_role = user.role
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

        self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(145)
        self.ui.tableWidget.horizontalHeader().setMinimumSectionSize(145)
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

        # self.ui.filterNameInput.textChanged.connect(lambda: self.make_capital(self.ui.filterNameInput))
        self.auto_completer()

        self.ui.printBtn.clicked.connect(self.openPrintMemo)
        self.ui.saveBtn.clicked.connect(self.save_xlsx)

        self.apply_bangla_font() #  apply bangla font first
        self.update_setting_font()
        data_save_signals.data_saved.connect(self.update_setting_font)

    def apply_bangla_font(self):
        bangla_font_path = "font/nato.ttf"
        font_id = QFontDatabase.addApplicationFont(bangla_font_path)
        if font_id == -1:
            print(f"❌ Failed to load font: {bangla_font_path}")
            return
        font_id = QFontDatabase.addApplicationFont(bangla_font_path)
        custom_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font = QFont(custom_font_family, 13)  # Font size 14

        self.ui.tableWidget.horizontalHeader().setFont(custom_font)
        self.ui.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.ui.tableWidget.setFont(custom_font)
        self.ui.startDateLabel.setFont(custom_font)
        self.ui.endDateLabel.setFont(custom_font)
        self.ui.filterLabel.setFont(custom_font)
        self.ui.filterBtn.setFont(custom_font)
        self.ui.saveBtn.setFont(custom_font)
        self.ui.printBtn.setFont(custom_font)
        self.ui.accountNameLabel.setFont(custom_font)
        self.ui.accountNameSelect.setFont(custom_font)
        self.ui.filterNameLabel.setFont(custom_font)
        self.ui.nameLabel.setFont(custom_font)
        self.ui.amount.setFont(custom_font)
        self.ui.tableWidget.viewport().update()

    def update_setting_font(self):
        session = self.Session()
        setting = session.query(SettingModel).first()
        bangla_font_path = "font/nato.ttf"
        english_font_path = "font/arial.ttf"
        font_id = QFontDatabase.addApplicationFont(bangla_font_path)
        if font_id == -1:
            print(f"❌ Failed to load font: {bangla_font_path}")
            return
        # Load the appropriate font
        if setting.font == "Bangla":
            font_id = QFontDatabase.addApplicationFont(bangla_font_path)
            custom_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            custom_font = QFont(custom_font_family, 12)  # Font size 12
        else:
            font_id = QFontDatabase.addApplicationFont(english_font_path)
            custom_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            custom_font = QFont(custom_font_family, 12)  # Font size 12

        from bangla_typing import enable_bangla_typing
        self.ui.filterNameInput.setFont(custom_font)
        enable_bangla_typing(self.ui.filterNameInput, setting.font)

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
            def custom_int(data):
                try:
                    data = int(data)
                    return data
                except:
                    return 0

            search_name = self.ui.filterNameInput.text()
            entry_index = self.ui.accountNameSelect.currentIndex()
            entry_name = {0: 'all_accounting', 1: 'salary',
                          2: 'other_cost', 3: 'mosque',
                          4: 'somiti', 5: 'other_cost_voucher'}.get(entry_index, 'all_accounting')
            start_date = self.ui.startDateInput.date().toPyDate()
            end_date = self.ui.endDateInput.date().toPyDate()

            # Retrieve data from the database
            with self.Session() as session:
                query = session.query(CostProfileModel).filter(CostProfileModel.date.between(start_date, end_date))

                if entry_name != 'all_accounting':
                    query = query.filter(CostProfileModel.cost_type.ilike(f"%{entry_name}%"))
                if search_name:
                    query = query.filter(CostProfileModel.name.ilike(f"%{search_name}%"))

                all_entries = query.all()

            # Clear existing table data
            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.setRowCount(0)

            # Populate the table with queried data
            self.ui.amount.setText(str(0))
            row = 0
            for entry in all_entries:
                cost_type = {
                              'salary': "বেতন / মজুরি প্রদান", 'other_cost': "অফিস খরচ", 'mosque': 'মসজিদ/মাদ্রাসা',
                              'somiti': 'সমিতি', 'other_cost_voucher': 'অন্যান্য(ভাউচার)'
                              }.get(entry.cost_type.strip(), "অফিস খরচ")
                self.ui.tableWidget.insertRow(row)
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(entry.id)))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(entry.date)))
                self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(cost_type)))
                self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(entry.name)))
                self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(entry.amount)))

                # View button
                view_button = QtWidgets.QPushButton("")
                view_icon = QtGui.QIcon("./images/view.png")
                view_button.setIcon(view_icon)
                view_button.setIconSize(QtCore.QSize(24, 24))
                view_button.setStyleSheet("background-color: white; border: none; padding: 5px;")
                view_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                view_button.clicked.connect(
                    (lambda _, name=entry.name, cost_type=entry.cost_type: self.view_profile(name, cost_type)))
                self.ui.tableWidget.setCellWidget(row, 5, view_button)

                # Edit button
                edit_button = QtWidgets.QPushButton("")
                edit_icon = QtGui.QIcon("./images/edit.png")
                edit_button.setIcon(edit_icon)
                edit_button.setIconSize(QtCore.QSize(24, 24))
                edit_button.setStyleSheet("background-color: white; border: none; padding: 5px;")
                edit_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                edit_button.clicked.connect(
                    (lambda _, name=entry.name, cost_type=entry.cost_type: self.profile_edit(name, cost_type))
                )
                self.ui.tableWidget.setCellWidget(row, 6, edit_button)

                # Delete button
                delete_button = QtWidgets.QPushButton("")
                delete_icon = QtGui.QIcon("./images/delete.png")
                delete_button.setIcon(delete_icon)
                delete_button.setIconSize(QtCore.QSize(24, 24))
                delete_button.setStyleSheet("background-color: white; border: none; padding: 5px;")
                delete_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                delete_button.clicked.connect((lambda _, r=row: self.delete_row(r)))
                self.ui.tableWidget.setCellWidget(row, 7, delete_button)

                old_amount = custom_int(self.ui.amount.text())
                self.ui.amount.setText(str(old_amount+custom_int(entry.amount)))
                row += 1
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "seller Profile Error", f"An error occurred while filtering data: {e}")

    def delete_row(self, row):
        if self.user_role == "editor":
            QtWidgets.QMessageBox.warning(None, "Delete Error", "এই প্রোফাইলে ডিলিট করার একসেস নেই..")
            return

        try:
            # Confirm deletion
            reply = QtWidgets.QMessageBox.question(
                None,
                'মুছে ফেলা নিশ্চিত করুন',
                'আপনি কি নিশ্চিত যে আপনি এই প্রোফাইল মুছে ফেলতে চান?',
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                QtWidgets.QMessageBox.StandardButton.No
            )

            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                # Retrieve name, cost_type, and amount from the table
                name = self.ui.tableWidget.item(row, 3).text()
                cost_type = self.ui.tableWidget.item(row, 2).text()
                amount = int(self.ui.tableWidget.item(row, 4).text())

                # Map cost_type to database format
                cost_type_mapping = {
                    "বেতন / মজুরি প্রদান": "salary",
                    "অফিস খরচ": "other_cost",
                    "মসজিদ/মাদ্রাসা": "mosque",
                    "সমিতি": "somiti",
                    "অন্যান্য(ভাউচার)": "other_cost_voucher"
                }
                cost_type_db = cost_type_mapping.get(cost_type.strip(), None)
                if not cost_type_db:
                    print(f"Error: Unable to map cost_type '{cost_type}' to a database value.")
                    QtWidgets.QMessageBox.critical(None, "Delete Error", f"Invalid cost type: {cost_type}")
                    return

                with self.Session() as session:
                    try:
                        # Retrieve and delete the CostProfileModel entry
                        cost_profile = session.query(CostProfileModel).filter(
                            and_(
                                CostProfileModel.name.ilike(name.strip()),
                                CostProfileModel.cost_type.ilike(cost_type_db.strip())
                            )
                        ).first()

                        if not cost_profile:
                            print(f"No CostProfileModel entry found for name: {name}, cost_type: {cost_type_db}")
                            QtWidgets.QMessageBox.critical(None, "Delete Error", "No matching profile found.")
                            return

                        # Retrieve and update the FinalAccounting model
                        final_accounting = session.query(FinalAccounting).first()
                        if not final_accounting:
                            # If FinalAccounting entry does not exist, create one
                            final_accounting = FinalAccounting(capital=0)
                            session.add(final_accounting)

                        # Add the amount to the FinalAccounting capital
                        final_accounting.capital += cost_profile.amount

                        # Delete the CostProfileModel entry
                        session.delete(cost_profile)

                        # Delete from DealerModel if applicable
                        session.query(DealerModel).filter(
                            and_(
                                DealerModel.name.ilike(name.strip()),
                                DealerModel.entry_name.ilike(cost_type_db.strip())
                            )
                        ).delete()

                        # Commit changes
                        session.commit()
                        print(
                            f"Deleted CostProfileModel entry and updated FinalAccounting capital by {cost_profile.amount}.")

                        # Remove row from the table
                        self.ui.tableWidget.removeRow(row)
                        data_save_signals.data_saved.emit()
                    except Exception as e:
                        print(f"Error during deletion: {e}")
                        QtWidgets.QMessageBox.critical(None, "Delete Error", f"An error occurred while deleting: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            QtWidgets.QMessageBox.critical(None, "Delete Error", f"Unexpected error: {e}")

    def view_profile(self, name, cost_type):
        try:
            session = self.Session()
            self.transactions_window = CostProfileView(name, cost_type, session)
            self.transactions_window.show()
        except Exception as e:
            print(f' err o : {str(e)}')

    def profile_edit(self, receiver_name, cost_type):
        print(" receiver_name : ", receiver_name)
        print(" cost_type : ", cost_type)
        if self.user_role == "editor":
            QtWidgets.QMessageBox.warning(None, "Delete Error", f"এই প্রোফাইলে এডিট করার একসেস নেই..")
            return
        try:
            # Create and show the SellerInformation dialog
            self.profile_edit_form_ui = Profile_Edit_Form(receiver_name, cost_type)
            self.profile_edit_form_ui.setWindowTitle("Profile Edit")

            # Connect buttons with proper lambda or partial
            self.profile_edit_form_ui.ui.update.clicked.connect(
                lambda: self.handle_profile_edit_information(receiver_name, cost_type))
            self.profile_edit_form_ui.ui.cancel.clicked.connect(self.profile_edit_form_ui.close)

            # Show the dialog
            self.profile_edit_form_ui.exec()
        except Exception as e:
            import traceback
            print(f"Error in profile_edit: {traceback.format_exc()}")
            QtWidgets.QMessageBox.critical(None, "Error", f"An unexpected error occurred: {e}")

    def handle_profile_edit_information(self, receiver_name, cost_type):
        try:
            success, error_message = self.profile_edit_form_ui.handle_entry()
            if success:
                self.accept_profile_edit_information(receiver_name, cost_type)
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

    def accept_profile_edit_information(self, receiver_name, cost_type):
        try:
            # Retrieve the data from the input fields
            name = self.profile_edit_form_ui.ui.name.text().strip()
            if name:
                with self.Session() as session:
                    # Query CostProfileModel
                    profile = session.query(CostProfileModel).filter(
                        and_(
                            CostProfileModel.name.ilike(receiver_name.strip()),
                            CostProfileModel.cost_type.ilike(cost_type.strip())
                        )
                    ).first()

                    # Query DealerModel and fetch all matching profiles
                    dealer_profiles = session.query(DealerModel).filter(
                        and_(
                            DealerModel.name.ilike(receiver_name.strip()),
                            DealerModel.entry_name.ilike(cost_type.strip())
                        )
                    ).all()

                    # Update profiles if found
                    if profile:
                        profile.name = name
                    if dealer_profiles:
                        for dealer_profile in dealer_profiles:
                            dealer_profile.name = name

                    # Commit changes if any profile is found
                    if profile or dealer_profiles:
                        session.commit()
                        self.filter_data()
                        self.profile_edit_form_ui.close()
                    else:
                        # No profiles found
                        error_dialog = QtWidgets.QMessageBox(self.profile_edit_form_ui)
                        error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                        error_dialog.setWindowTitle("Not Found")
                        error_dialog.setText("No profiles found to update.")
                        error_dialog.exec()
            else:
                # Input validation error
                error_dialog = QtWidgets.QMessageBox(self.profile_edit_form_ui)
                error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                error_dialog.setWindowTitle("Input Error")
                error_dialog.setText("All fields must be filled.")
                error_dialog.exec()
        except Exception as e:
            import traceback
            print(f"Error in accept_profile_edit_information: {traceback.format_exc()}")
            error_dialog = QtWidgets.QMessageBox(self.profile_edit_form_ui)
            error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Error")
            error_dialog.setText("An unexpected error occurred while updating profiles.")
            error_dialog.exec()

    def openPrintMemo(self):
        total_rows = self.ui.tableWidget.rowCount()
        rows_per_page = 11
        total_pages = math.ceil(total_rows / rows_per_page)
        total_pages = 1 if total_pages == 0 else total_pages
        for page in range(total_pages):
            try:
                # ✅ Create the print window
                self.ui_print_form = Print_Form()
                self.ui_print_form.ui.memoLabel.setText("খরচের রিপোর্ট")
                self.ui_print_form.ui.finalTaka.setText(str(self.ui.amount.text()))
                self.ui_print_form.ui.date.setText(str(self.ui.startDateInput.text()))
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
                excluded_columns = {0, 5, 6, 7}
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
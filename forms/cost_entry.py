from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import Qt, QDate
from datetime import datetime
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from features.data_save_signals import data_save_signals
from PyQt6.QtGui import QFont, QFontDatabase  # for font file load
from ui.cost_entry_ui import Ui_CostEntry
import os


class CostEntry_Form(QDialog):
    def __init__(self, username):
        super().__init__()
        self.ui = Ui_CostEntry()
        self.ui.setupUi(self)  # Call setupUi to apply the design to this dialog
        self.entry_by = username
        self.setup_database()
        self.setup_ui()

    def setup_database(self):
        self.Base = declarative_base()
        self.engine = create_engine('sqlite:///business.db')
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def setup_ui(self):
        # Set current date
        self.ui.entryDate.setDisplayFormat("dd/MM/yyyy")
        self.today_date_raw = datetime.now()
        self.today_date = self.today_date_raw.strftime("%d/%m/%Y").lstrip('0').replace('/0', '/')
        self.qdate_today = QDate.fromString(self.today_date, "d/M/yyyy")
        self.ui.entryDate.setDate(self.qdate_today)

        # Set up autocompletion
        self.update_autocomplete()

        # Connect signals to dynamically update completers
        self.ui.entryName.currentIndexChanged.connect(self.update_autocomplete)
        self.ui.payerName.textChanged.connect(self.update_autocomplete)
        self.ui.receiverName.textChanged.connect(self.update_autocomplete)

        # Connect completer activated signals to autofill_amount
        self.ui.payerName.textChanged.connect(self.handle_payer_autocomplete)
        self.ui.receiverName.textChanged.connect(self.handle_receiver_autocomplete)

        # Disable entry fields based on entry name selection
        self.ui.entryName.currentIndexChanged.connect(lambda: self.entry_disable(self.ui.entryName.currentIndex()))
        self.ui.entryName.currentIndexChanged.connect(self.autofill_cost_of_index_change)

        # By default, disable payer name input field
        self.ui.payerName.setDisabled(True)
        self.ui.payerName.setStyleSheet("background-color: #F0F0F0;")

        self.apply_bangla_font()
        self.update_setting_font()
        data_save_signals.data_saved.connect(self.update_setting_font)

    def update_autocomplete(self):
        """Update autocomplete data for payer and receiver names based on the selected entry."""
        print("Updating autocomplete...")

        payer_names = self.get_all_payer_names()
        receiver_names = self.get_all_receiver_names()

        # Debugging: Log fetched names
        print(f"Payer Names: {payer_names}")
        print(f"Receiver Names: {receiver_names}")

        # Update payer completer
        self.payerCompleter = QtWidgets.QCompleter(payer_names, self)
        self.payerCompleter.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ui.payerName.setCompleter(self.payerCompleter)

        # Update receiver completer
        self.receiverCompleter = QtWidgets.QCompleter(receiver_names, self)
        self.receiverCompleter.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ui.receiverName.setCompleter(self.receiverCompleter)

    def handle_payer_autocomplete(self, text):
        """Handle autofill when a payer is selected."""
        print(f"Payer selected: {text}")
        self.autofill_amount(text)

    def handle_receiver_autocomplete(self, text):
        """Handle autofill when a receiver is selected."""
        print(f"Receiver selected: {text}")
        self.autofill_amount(text)

    def get_all_payer_names(self):
        """Fetch all payer names from the database for autocomplete."""
        session = self.Session()
        try:
            selected_entry = self.ui.entryName.currentIndex()
            print(f"Fetching payer names for selected_entry: {selected_entry}")

            if selected_entry == 1:  # Buyer Profile
                return [name_entry.buyer_name for name_entry in session.query(BuyerProfileModel).all()]
            elif selected_entry == 4:  # Loan Payer
                return [name_entry.loan_payer_name for name_entry in session.query(LoanProfileModel).all()]
            elif selected_entry == 12:  # Loan Receiver
                return [name_entry.loan_receiver_name for name_entry in session.query(PayingLoanProfileModel).all()]
            else:
                return []
        except Exception as e:
            print(f"Error fetching payer names: {e}")
            return []
        finally:
            session.close()

    def get_all_receiver_names(self):
        """Fetch all receiver names from the database for autocomplete."""
        session = self.Session()
        try:
            selected_entry = self.ui.entryName.currentIndex()
            print(f"Fetching receiver names for selected_entry: {selected_entry}")

            if selected_entry == 0:  # Seller Profile
                return [name_entry.seller_name for name_entry in session.query(SellerProfileModel).all()]
            elif selected_entry == 5:  # Loan Payer
                return [name_entry.loan_payer_name for name_entry in session.query(LoanProfileModel).all()]
            elif selected_entry == 11:  # Loan Receiver
                return [name_entry.loan_receiver_name for name_entry in session.query(PayingLoanProfileModel).all()]
            elif selected_entry == 6:  # Salary Receiver
                return [name_entry.name for name_entry in
                        session.query(CostProfileModel).filter_by(cost_type="salary").all()]
            elif selected_entry == 7:  # Other Cost Receiver
                return [name_entry.name for name_entry in
                        session.query(CostProfileModel).filter_by(cost_type="other_cost").all()]
            elif selected_entry == 8:  # mosque
                return [name_entry.name for name_entry in
                        session.query(CostProfileModel).filter_by(cost_type="mosque").all()]
            elif selected_entry == 9:  # somiti
                return [name_entry.name for name_entry in
                        session.query(CostProfileModel).filter_by(cost_type="somiti").all()]
            elif selected_entry == 10:  # other_cost vouchar
                return [name_entry.name for name_entry in
                        session.query(CostProfileModel).filter_by(cost_type="other_cost_voucher").all()]
            else:
                return []
        except Exception as e:
            print(f"Error fetching receiver names: {e}")
            return []
        finally:
            session.close()

    def autofill_amount(self, name):
        """Autofill the amount field based on the selected name."""
        session = self.Session()
        try:
            entry_index = self.ui.entryName.currentIndex()
            print(f"Autofill triggered for name: '{name}', entry_index: {entry_index}")

            if entry_index == 0:  # Seller Profile
                seller = session.query(SellerProfileModel).filter_by(seller_name=name).first()
                if seller:
                    self.ui.amount.setText(str(seller.total_receivable))
            elif entry_index == 1:  # Buyer Profile
                buyer = session.query(BuyerProfileModel).filter_by(buyer_name=name).first()
                if buyer:
                    self.ui.amount.setText(str(buyer.total_payable))
            elif entry_index == 5:  # Loan Payer
                loan_payer = session.query(LoanProfileModel).filter_by(loan_payer_name=name).first()
                if loan_payer:
                    self.ui.amount.setText(str(loan_payer.amount))
            elif entry_index == 12:  # Loan Receiver
                loan_receiver = session.query(PayingLoanProfileModel).filter_by(loan_receiver_name=name).first()
                if loan_receiver:
                    self.ui.amount.setText(str(loan_receiver.amount))
        except Exception as e:
            print(f"Error autofilling amount: {e}")
        finally:
            session.close()

    def entry_disable(self, entry_index):
        if entry_index in [0, 2, 5, 6, 7, 8, 9, 10, 11]:
            self.ui.payerName.clear()
            self.ui.amount.clear()
            self.ui.payerName.setDisabled(True)
            self.ui.payerName.setStyleSheet("background-color: #F0F0F0;")
            self.ui.receiverName.setDisabled(False)
            self.ui.receiverName.setStyleSheet("background-color: #FFFFFF;")
        else:
            self.ui.payerName.setDisabled(False)
            self.ui.payerName.setStyleSheet("background-color: #FFFFFF;")
            self.ui.receiverName.clear()
            self.ui.amount.clear()
            self.ui.receiverName.setDisabled(True)
            self.ui.receiverName.setStyleSheet("background-color: #F0F0F0")

    def autofill_cost_of_index_change(self):
        entry_index = self.ui.entryName.currentIndex()
        session = self.Session()
        try:
            if entry_index == 8:
                mosque = session.query(CostModel.mosque).first()
                if mosque:
                    self.ui.amount.setText(str(mosque[0]))
            elif entry_index == 9:
                somiti = session.query(CostModel.somiti).first()
                if somiti:
                    self.ui.amount.setText(str(somiti[0]))
            elif entry_index == 10:
                other_cost = session.query(CostModel.other_cost).first()
                if other_cost:
                    self.ui.amount.setText(str(other_cost[0]))
            else:
                self.ui.receiverName.setText("")
                self.ui.payerName.setText("")
        except Exception as e:
            print(f"Error autofilling cost: {e}")
        finally:
            session.close()

    def apply_bangla_font(self):
        bangla_font_path = "font/nato.ttf"
        font_id = QFontDatabase.addApplicationFont(bangla_font_path)
        custom_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        print("✅[Cost Entry] font_family : ", custom_font_family)
        custom_font = QFont(custom_font_family, 13)
        self.ui.label_3.setFont(custom_font)
        self.ui.label_4.setFont(custom_font)
        self.ui.label_5.setFont(custom_font)
        self.ui.label_7.setFont(custom_font)
        self.ui.label_8.setFont(custom_font)
        self.ui.label_9.setFont(custom_font)
        self.ui.cancelBtn.setFont(custom_font)
        self.ui.addBtn.setFont(custom_font)
        self.ui.entryName.setFont(custom_font)

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
        self.ui.payerName.setFont(custom_font)
        self.ui.receiverName.setFont(custom_font)
        self.ui.description.setFont(custom_font)
        enable_bangla_typing(self.ui.payerName, setting.font)
        enable_bangla_typing(self.ui.receiverName, setting.font)
        enable_bangla_typing(self.ui.description, setting.font)
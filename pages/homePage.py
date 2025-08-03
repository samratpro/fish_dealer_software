from PyQt6.QtWidgets import QWidget
from datetime import datetime, timedelta
from PyQt6.QtCore import QDate
from features.data_save_signals import data_save_signals
from sqlalchemy import create_engine, not_
from sqlalchemy.orm import sessionmaker, declarative_base
from ui.homePage_ui import Ui_HomePageMain
from PyQt6 import QtWidgets
from models import *
from PyQt6.QtGui import QFont, QFontDatabase
from datetime import date, timedelta


class homepage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_database()  # First setup database
        self.ui = Ui_HomePageMain()
        self.ui.setupUi(self)
        self.setup_ui()

    def setup_database(self):
        self.Base = declarative_base()
        self.engine = create_engine('sqlite:///business.db')  # change db url
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def setup_ui(self):
        self.ui.startDateInput.setDisplayFormat("dd/MM/yyyy")
        self.ui.endDateInput.setDisplayFormat("dd/MM/yyyy")
        self.today_date_raw = datetime.now()
        seven_days_ago = self.today_date_raw - timedelta(days=7)
        # Convert both dates to QDate
        qdate_today = QDate(self.today_date_raw.year, self.today_date_raw.month, self.today_date_raw.day)
        qdate_seven_days_ago = QDate(seven_days_ago.year, seven_days_ago.month, seven_days_ago.day)
        # Set the dates
        self.ui.startDateInput.setDate(qdate_today)
        self.ui.endDateInput.setDate(qdate_today)
        data_save_signals.data_saved.connect(self.filter_data) # self.filter_data
        self.filter_data()
        self.ui.filterBtn.clicked.connect(self.filter_data) # self.filter_data
        self.apply_bangla_font()

    def apply_bangla_font(self):
        bangla_font_path = "font/nato.ttf"
        font_id = QFontDatabase.addApplicationFont(bangla_font_path)
        if font_id == -1:
            print(f"❌ Failed to load font: {bangla_font_path}")
            return
        font_id = QFontDatabase.addApplicationFont(bangla_font_path)
        custom_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font = QFont(custom_font_family, 13)
        custom_font_low = QFont(custom_font_family, 12)
        custom_font_high = QFont(custom_font_family, 18)
        # Recursively apply font to all child widgets
        self.setFont(custom_font)
        amount_font = QFont(custom_font_family, 22)
        self.ui.capitalAmount.setFont(amount_font)
        self.ui.receivedLoanAmount.setFont(amount_font)
        self.ui.receivedAmount.setFont(amount_font)
        self.ui.paidLoanAmount.setFont(amount_font)
        self.ui.payableAmount.setFont(amount_font)
        self.ui.receivableAmount.setFont(amount_font)
        self.ui.costAmount.setFont(amount_font)
        self.ui.commisionAmount.setFont(amount_font)
        self.ui.label.setFont(custom_font_high)
        self.ui.label_2.setFont(custom_font_low)

    def filter_data(self):
        try:
            # Get the start and end dates from the input fields
            start_date = self.ui.startDateInput.date().toPyDate()
            end_date = self.ui.endDateInput.date().toPyDate()

            # Retrieve data from the database
            session = self.Session()
            capital = session.query(FinalAccounting).first()

            received_loan_all = session.query(LoanProfileModel).filter(LoanProfileModel.amount > 0)
            received_loan_amount = sum(loan.amount for loan in received_loan_all)

            paid_loan_all = session.query(PayingLoanProfileModel).filter(PayingLoanProfileModel.amount > 0)
            paid_loan_amount = sum(loan.amount for loan in paid_loan_all)

            # Calculate the start and end dates for the fiscal year (July 1 to June 30)
            from datetime import date
            today = date.today()
            fiscal_year_start = date(today.year if today.month >= 7 else today.year - 1, 7, 1)
            fiscal_year_end = date(fiscal_year_start.year + 1, 6, 30)

            # Filter commission_amount within the fiscal year (July 1 to June 30)


            # commission_all = session.query(SellerProfileModel).filter(
            #     SellerProfileModel.total_commission != 0,
            #     SellerProfileModel.date.between(fiscal_year_start, fiscal_year_end)
            # ).all()
            # commission_amount = sum(commision.total_commission for commision in commission_all)

            commission_all = session.query(SellingModel).filter(
                SellingModel.commission_amount != 0,
                SellingModel.date.between(fiscal_year_start, fiscal_year_end)
            ).all()
            commission_amount = sum(commision.commission_amount for commision in commission_all)

            # Filter cost_amount within the fiscal year (July 1 to June 30)
            cost_all = session.query(DealerModel).filter(
                DealerModel.paying_amount != 0,
                DealerModel.entry_name.in_(['salary', 'other_cost']),
                DealerModel.date.between(fiscal_year_start, fiscal_year_end)
            ).all()
            cost_amount = sum(cost.paying_amount for cost in cost_all)

            # Filter received amounts within the input date range
            received_all = session.query(DealerModel).filter(
                DealerModel.receiving_amount != 0,
                not_(DealerModel.entry_name.in_(['capital_deposit', 'borrowing'])),
                DealerModel.date.between(start_date, end_date)
            ).all()
            received_amount = sum(received.receiving_amount for received in received_all)

            # Get total payable amounts within the input date range
            cost_entry = session.query(CostModel).first()
            total_payable = session.query(SellerProfileModel).filter(
                SellerProfileModel.date.between(start_date, end_date)).all()
            payable_amount = sum(payable.total_receivable for payable in total_payable)
            payable_amount += (cost_entry.other_cost + cost_entry.somiti + cost_entry.mosque)

            # Get total receivable amounts within the input date range
            total_receivable = session.query(BuyerProfileModel).filter(
                BuyerProfileModel.date.between(start_date, end_date)).all()
            receivable_amount = sum(receivable.total_payable for receivable in total_receivable)

            # Update the UI with the filtered data
            self.ui.capitalAmount.setText(str(capital.capital))
            self.ui.receivedLoanAmount.setText(str(received_loan_amount))
            self.ui.receivedAmount.setText(str(received_amount))
            self.ui.paidLoanAmount.setText(str(paid_loan_amount))
            self.ui.payableAmount.setText(str(payable_amount))
            self.ui.receivableAmount.setText(str(receivable_amount))
            self.ui.commisionAmount.setText(str(commission_amount))
            self.ui.costAmount.setText(str(cost_amount))

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Seller Profile Error", f"An error occurred while filtering data: {e}")

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    HomePageMain = QtWidgets.QWidget()
    ui = Ui_HomePageMain()
    ui.setupUi(HomePageMain)
    HomePageMain.show()
    sys.exit(exec())

